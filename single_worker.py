import os
import time
import uuid
import yaml
import psutil
import logging
from extractors.product_list import extract_product_list_items
from extractors.product_detail import extract_product_detail
from page_classifier.job_builder import build_job_from_html
from seleniumbase import sb_cdp
from paginator import HybridPaginator
from pathlib import Path
from webhook_notifier import WebhookNotifier

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [%(processName)s] %(message)s",
)
logger = logging.getLogger(__name__)


def load_config(path=Path.cwd() / "config.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)

config = load_config()

class WorkerProcess():
    def __init__(self, config, worker_id):
        self.config = config
        self.worker_id = worker_id

        # Queue Connection (Redis)

        # Browser Lifecycle state
        self.page_count = 0
        self.browser_proc = None
        self.sb = None

    def _check_memory(self):
        """Check if current process and children exceed memory limit."""
        try:
            current_process = psutil.Process(os.getpid())
            mem_info = current_process.memory_info().rss
            children = current_process.children(recursive=True)
            for child in children:
                mem_info += child.memory_info().rss

            mem_mb = mem_info / (1024 * 1024)
            return mem_mb
        except Exception as e:
            logger.error(f"Error checking memory: {e}")
            return 0

    def _init_browser(self):
        """Start SeleniumBase CDP Chrome + Playwright passive listener."""
        logger.info("Initializing fresh browser instance...")
        b_cfg = self.config["browser"]

        # 1. SeleniumBase acts as the master DOM controller
        # CDP mode brings stealth, hides webdriver flags, randomizes UAs, etc.
        args = []
        if b_cfg.get("disable_images"):
            args.append("--blink-settings=imagesEnabled=false")

        self.sb = sb_cdp.Chrome(
            headless=b_cfg.get("headless", True),
            locale=b_cfg.get("locale", "fr-TN"),
            proxy=b_cfg.get("proxy"),
            user_data_dir=b_cfg.get("user_data_dir"),
            args=args,
        )

        time.sleep(1)

        self.page_count = 0

    def _close_browser(self):
        """Clean teardown."""
        logger.info("Tearing down browser instance...")

        if self.sb:
            try:
                self.sb.close_active_tab()
            except:
                pass

        self.sb = None

        # Aggressive cleanup of any zombie chrome processes belonging to this worker
        current_process = psutil.Process(os.getpid())
        for child in current_process.children(recursive=True):
            if "chrome" in child.name().lower():
                try:
                    child.terminate()
                except psutil.NoSuchProcess:
                    pass

    def perform_scrape(self, job):
        if not self.sb:
            return

        url = job["url"]
        logger.info(f"Scraping URL: {url}")

        try:
            # We use the new HybridPaginator for orchestration
            # Use max_pages from config or default to 50
            max_pages = self.config["worker"].get("max_pages_per_job", 50)

            self.sb.open(url)

            builded_job = build_job_from_html(self.sb.get_page_source(), url)
            extracted_data = {
                "job_type": builded_job.job_type,
                "metadata": builded_job.metadata
            }

            if builded_job.job_type == "product_list_paginated":
                paginator = HybridPaginator(self.sb, url, max_pages=max_pages)
                extracted_data["products"] = paginator.extract_products_while_paginating(builded_job.metadata.get("winner_blocks"))
            elif builded_job.job_type == "product_list":
                extracted_data["products"] = extract_product_list_items(self.sb.get_page_source(), url, builded_job.metadata.get("winner_blocks"))
            elif builded_job.job_type == "product_detail":
                extracted_data["product"] = extract_product_detail(self.sb.get_page_source(), url)
            elif builded_job.job_type == "homepage_discovery":
                # TODO: implement
                pass
            elif builded_job.job_type == "content_list":
                # TODO: implement
                pass
            else:
                raise Exception(f"Unknown job type: {builded_job.job_type}")
                

            # After paginator finishes, extraction could happen sequentially or after each page.
            # Here we just record the overall result stat.
            # In a real pipeline, the paginator itself could yield data or save to DB per page.

            extracted_data["title"] = self.sb.get_title() # type: ignore
            job["result"] = extracted_data
            
            # Send Webhook
            notifier = WebhookNotifier()
            notifier.send_payload(job)

        except Exception as e:
            logger.error(f"Error scraping {url}: {e}")

    def run(self, job):
        """Main worker loop."""
        logger.info("Worker process started.")

        try:
            if not job:
                # No jobs, sleep and check again
                return

            # Ensure browser is alive
            if not self.sb:
                self._init_browser()

            # Process job
            self.perform_scrape(job)

            # Check limits
            mem_mb = self._check_memory()
            max_pages = self.config["worker"]["max_pages_per_browser"]
            max_mem = self.config["worker"]["max_memory_mb"]

            if self.page_count >= max_pages:
                logger.info(f"Reached max pages ({max_pages}). Restarting browser.")
                self._close_browser()
            elif mem_mb > max_mem:
                logger.warning(
                    f"Memory threshold exceeded ({mem_mb:.1f}MB > {max_mem}MB). Restarting browser."
                )
                self._close_browser()

        except KeyboardInterrupt:
            logger.info("Worker shutting down gracefully...")
            self._close_browser()
        except Exception as e:
            logger.error(f"Fatal worker exception: {e}")
            self._close_browser()
            time.sleep(self.config["worker"]["retry_backoff_sec"])


# https://emtop.tn/bricolage/outillage-electroportatif.html
# https://arkan.tn/bricolage-et-quincaillerie/outillage-electroportatif.html
# https://www.technoquip-tn.com/categorie-produit/equipement-industriel/pneumatique-tunisie/outillage-pneumatique/
# https://sovaq.tn/97-outillage-pneumatique
# https://totaltunisia.com/collections/outils-pneumatiques
# https://egb-benyedder.com.tn/product-category/pneumatique/
# https://www.simdriss.com/produits/12/MACHINE+PNEUMATIQUE.html
# https://bigdepot.tn/32-outillage-pneumatique
# https://brico-direct.tn/502-accessoires-pneumatiques
# https://www.10000articles.shop/compresseur-tuyaux-comprim%C3%A9-et-accessoires-2

if __name__ == "__main__":
    job = {
        "id": str(uuid.uuid4()),
        "url": "https://bricola.tn/boulon-tunisie/2486-lot-de-2-boulon-hexagonale-m10120mm-acier-zingue-bricola-6141750301031.html",
        "metadata": {},
        "retries": 0,
        "status": "pending",
        "created_at": time.time(),
    }
    p = WorkerProcess(config, "1")
    p.run(job)
