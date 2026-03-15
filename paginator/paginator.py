from bs4 import BeautifulSoup

from product_detection import ProductListExtractor
import logging
from typing import List, Literal

from seleniumbase.core.sb_cdp import Chrome

from . import constants, detection, handlers, utils
from extractors.product_list import extract_product_list_items
from product_detection.models import ClusterScore, ProductItem

logger = logging.getLogger(__name__)


class HybridPaginator:
    """
    Production-ready Hybrid Pagination Engine using SeleniumBase (CDP mode).
    Handles URL pagination, Load More buttons, Next buttons, and Infinite Scroll.
    """

    def __init__(self, sb: Chrome, start_url: str, max_pages: int = 50):
        self.sb = sb
        self.start_url = start_url
        self.max_pages = max_pages
        self.current_page_count = 0
        self.product_selector = None

    def _random_sleep(self, min_sec: float = 1.0, max_sec: float = 3.0) -> None:
        utils.random_sleep(min_sec, max_sec)

    def detect_pagination_type(self) -> dict:
        """
        Detect the type of pagination present on the current page.
        Returns a dictionary with type, pattern, and selector.
        """
        return detection.detect_pagination_type(self.sb)

    def handle_url_pagination(self, base_url: str, param_name: str) -> int:
        return handlers.handle_url_pagination(
            self.sb, base_url, param_name, self.max_pages, self.product_selector
        )

    def handle_load_more(self, button_selector: str) -> int:
        return handlers.handle_load_more(
            self.sb, button_selector, self.max_pages, self.product_selector
        )

    def handle_next_button(self, selector: str) -> int:
        return handlers.handle_next_button(
            self.sb, selector, self.max_pages, self.product_selector
        )

    def handle_infinite_scroll(self) -> int:
        return handlers.handle_infinite_scroll(self.sb, self.max_pages)

    def extract_products_while_paginating(
        self, winner_blocks: ClusterScore | None
    ) -> List[ProductItem]:
        """
        Extract products from the current page, then paginate (scroll/load more/next/url)
        and keep extracting until exhaustion or max_pages.
        """

        if winner_blocks is None:
            logger.warning(
                "No product blocks detected. Falling back to generic extraction."
            )
            return []

        logger.info(f"Starting extract+paginate for {self.start_url}")

        extractor = ProductListExtractor()

        self._random_sleep(2.0, 4.0)

        pagination_info = self.detect_pagination_type()
        p_type = pagination_info.get("type")

        collected: List[ProductItem] = []

        products = extractor.extractor.extract_products(
            winner_blocks.blocks, base_url=self.sb.get_current_url() or self.start_url
        )
        collected.extend(products)

        pages_crawled = 1

        def run_url_pagination(param_name: str, target_signature: str) -> int:
            nonlocal pages_crawled
            from urllib.parse import urlparse, parse_qs

            parsed = urlparse(self.start_url)
            params = parse_qs(parsed.query)
            current_page = 1
            if param_name in params:
                try:
                    current_page = int(params[param_name][0])
                except ValueError:
                    pass

            last_url = self.start_url
            while pages_crawled < self.max_pages:
                current_page += 1
                next_url = utils.get_next_page_url(
                    self.start_url, param_name, current_page
                )
                logger.info(f"Navigating to next page: {next_url}")
                try:
                    self.sb.open(next_url)
                    self._random_sleep(*constants.WAIT_SEC_BETWEEN_PAGE_SCRAPE)

                    real_url = self.sb.get_current_url()
                    if real_url == last_url or real_url == self.start_url:
                        logger.info("Redirected to a previously seen URL. Stopping.")
                        break
                    last_url = real_url

                    soup = BeautifulSoup(self.sb.get_page_source() or "", "lxml")
                    winner_blocks = extractor.get_container_block(
                        soup=soup,
                        page_url=self.sb.get_current_url() or self.start_url,
                        target_signature=target_signature
                    )
                    if winner_blocks is None:
                        logger.info(
                            "No product blocks detected after loading more. Stopping."
                        )
                        break

                    products = extractor.extractor.extract_products(
                        winner_blocks.blocks,
                        base_url=self.sb.get_current_url() or self.start_url,
                    )
                    collected.extend(products)
                    pages_crawled += 1

                except Exception as exc:
                    logger.error(f"Error during URL pagination: {exc}")
                    break
            return pages_crawled

        def run_next_button(selector: str, target_signature: str) -> int:
            nonlocal pages_crawled

            while pages_crawled < self.max_pages:
                try:
                    if not self.sb.is_element_present(selector):
                        logger.info("Next button not present. Stopping.")
                        break

                    el = self.sb.find_element(selector)
                    cls = el.get_attribute("class") or ""
                    if "disabled" in cls.lower() or el.get_attribute("disabled"):
                        logger.info("Next button disabled. Stopping.")
                        break

                    logger.debug("Clicking Next button...")
                    try:
                        self.sb.click(selector)
                    except Exception:
                        safe_sel = selector.replace('"', '\\"')
                        self.sb.execute_script(
                            f'document.querySelector("{safe_sel}").click();'
                        )

                    self._random_sleep(*constants.WAIT_SEC_BETWEEN_PAGE_SCRAPE)

                    soup = BeautifulSoup(self.sb.get_page_source() or "", "lxml")
                    winner_blocks = extractor.get_container_block(
                        soup=soup,
                        page_url=self.sb.get_current_url() or self.start_url,
                        target_signature=target_signature
                    )
                    if winner_blocks is None:
                        logger.info(
                            "No product blocks detected after loading more. Stopping."
                        )
                        break

                    products = extractor.extractor.extract_products(
                        winner_blocks.blocks,
                        base_url=self.sb.get_current_url() or self.start_url,
                    )
                    collected.extend(products)
                    pages_crawled += 1

                except Exception as exc:
                    logger.error(f"Error interacting with Next button: {exc}")
                    break

            return pages_crawled

        def run_load_more(selector: str) -> int:
            nonlocal pages_crawled

            while pages_crawled < self.max_pages:
                try:
                    if not self.sb.is_element_visible(selector):
                        logger.info("Load More button not visible. Stopping.")
                        break

                    logger.debug("Clicking Load More button...")
                    self.sb.click(selector)
                    self._random_sleep(*constants.WAIT_SEC_BETWEEN_PAGE_SCRAPE)

                    soup = BeautifulSoup(self.sb.get_page_source() or "", "lxml")
                    winner_blocks = extractor.get_container_block(
                        soup, page_url=self.sb.get_current_url() or self.start_url
                    )
                    if winner_blocks is None:
                        logger.info(
                            "No product blocks detected after loading more. Stopping."
                        )
                        break

                    products = extractor.extractor.extract_products(
                        winner_blocks.blocks,
                        base_url=self.sb.get_current_url() or self.start_url,
                        index=len(collected),
                    )
                    collected.extend(products)
                    pages_crawled += 1

                except Exception as exc:
                    logger.error(f"Error interacting with Load More button: {exc}")
                    break
            return pages_crawled

        def run_infinite_scroll() -> int:
            nonlocal pages_crawled
            attempts = 0
            max_stable_attempts = 3
            last_height = self.sb.execute_script("return document.body.scrollHeight")

            while pages_crawled < self.max_pages:
                try:
                    self.sb.execute_script(
                        "window.scrollTo(0, document.body.scrollHeight);"
                    )
                    self._random_sleep(*constants.WAIT_SEC_BETWEEN_PAGE_SCRAPE)

                    new_height = self.sb.execute_script(
                        "return document.body.scrollHeight"
                    )
                    if new_height == last_height:
                        attempts += 1
                        if attempts >= max_stable_attempts:
                            logger.info(
                                "Document height stable. Stopping infinite scroll."
                            )
                            break
                    else:
                        attempts = 0
                        last_height = new_height
                        soup = BeautifulSoup(self.sb.get_page_source() or "", "lxml")
                        winner_blocks = extractor.get_container_block(
                            soup, page_url=self.sb.get_current_url() or self.start_url
                        )
                        if winner_blocks is None:
                            logger.info(
                                "No product blocks detected after loading more. Stopping."
                            )
                            break

                        products = extractor.extractor.extract_products(
                            winner_blocks.blocks,
                            base_url=self.sb.get_current_url() or self.start_url,
                            index=len(collected),
                        )
                        collected.extend(products)
                        pages_crawled += 1

                except Exception as exc:
                    logger.error(f"Error during infinite scroll: {exc}")
                    break
            return pages_crawled

        # Execute pagination strategy with fallbacks
        if p_type == "url":
            param = pagination_info.get("pattern")
            run_url_pagination(param, winner_blocks.class_signature)  # type: ignore
            if pages_crawled <= 1:
                logger.info("URL pagination failed. Trying Next Button fallback...")
                p_type = "next_button"

        if p_type == "next_button":
            sel = (
                pagination_info.get("selector")
                if pagination_info.get("type") == "next_button"
                else 'a[rel="next"]'
            )
            run_next_button(sel, winner_blocks.class_signature)  # type: ignore
            if pages_crawled <= 1:
                logger.info("Next Button failed. Trying Load More fallback...")
                p_type = "load_more"

        if p_type == "load_more":
            sel = (
                pagination_info.get("selector")
                if pagination_info.get("type") == "load_more"
                else 'button[class*="load"]'
            )
            run_load_more(sel)  # type: ignore
            if pages_crawled <= 1:
                logger.info("Load More failed. Trying Infinite Scroll fallback...")
                p_type = "infinite_scroll"

        if p_type == "infinite_scroll":
            run_infinite_scroll()

        return collected

    # def run(self) -> int:
    #     """
    #     Main execution loop.
    #     Detect product container, pagination type, and dispatch to the right handler.
    #     """
    #     logger.info(f"Starting HybridPaginator for {self.start_url}")

    #     try:
    #         self._random_sleep(2.0, 4.0)

    #         self.detect_product_container()

    #         pagination_info = self.detect_pagination_type()
    #         p_type = pagination_info.get("type")

    #         pages = 1

    #         if p_type == "url":
    #             param = pagination_info.get("pattern")
    #             pages = self.handle_url_pagination(self.start_url, param)  # type: ignore
    #             if pages <= 1:
    #                 logger.info("URL pagination failed. Trying Next Button fallback...")
    #                 p_type = "next_button"

    #         if p_type == "next_button":
    #             if pagination_info.get("type") == "next_button":
    #                 sel = pagination_info.get("selector")
    #             else:
    #                 sel = 'a[rel="next"]'

    #             pages = self.handle_next_button(sel)  # type: ignore

    #             # if pages <= 1:
    #             #     logger.info("Next Button failed. Trying Load More fallback...")
    #             #     p_type = "load_more"

    #         if p_type == "load_more":
    #             if pagination_info.get("type") == "load_more":
    #                 sel = pagination_info.get("selector")
    #             else:
    #                 sel = 'button[class*="load"]'

    #             pages = self.handle_load_more(sel)  # type: ignore

    #             if pages <= 1:
    #                 logger.info("Load More failed. Trying Infinite Scroll fallback...")
    #                 p_type = "infinite_scroll"

    #         if p_type == "infinite_scroll":
    #             pages = self.handle_infinite_scroll()

    #         return pages

    #     except Exception as e:
    #         logger.error(f"Fatal error in HybridPaginator: {e}")
    #         return self.current_page_count
