import logging
from urllib.parse import urlparse, parse_qs

from seleniumbase.core.sb_cdp import Chrome

from .constants import (
    MAX_STABLE_ATTEMPTS,
    NO_CHANGE_LIMIT,
    PAGE_LOAD_WAIT_SEC,
    WAIT_SEC_BEFORE_ACTION,
)
from .utils import count_products, get_next_page_url, random_sleep

logger = logging.getLogger(__name__)


def handle_url_pagination(
    sb: Chrome,
    base_url: str,
    param_name: str,
    max_pages: int,
    product_selector: str | None,
) -> int:
    """Handle pagination by directly modifying the URL parameter."""
    logger.info(f"Executing URL pagination strategy (param: {param_name}).")

    parsed = urlparse(base_url)
    params = parse_qs(parsed.query)
    current_page = 1
    if param_name in params:
        try:
            current_page = int(params[param_name][0])
        except ValueError:
            pass

    pages_crawled = 1
    last_url = base_url

    while pages_crawled < max_pages:
        current_page += 1
        next_url = get_next_page_url(base_url, param_name, current_page)

        logger.info(f"Navigating to next page: {next_url}")
        try:
            sb.open(next_url)
            random_sleep(*WAIT_SEC_BEFORE_ACTION)

            real_url = sb.get_current_url()

            if real_url == last_url or real_url == base_url:
                logger.info("Redirected to a previously seen URL. Stopping.")
                break

            last_url = real_url

            if product_selector:
                count = count_products(sb, product_selector)
                if count == 0:
                    logger.info("No products found on new page. Stopping.")
                    break

            pages_crawled += 1

        except Exception as e:
            logger.error(f"Error during URL navigation: {e}")
            break

    return pages_crawled


def handle_load_more(
    sb: Chrome, button_selector: str, max_pages: int, product_selector: str | None
) -> int:
    """Handle pagination by repeatedly clicking a Load More button."""
    logger.info(f"Executing Load More strategy (selector: {button_selector}).")

    pages_crawled = 1
    no_change_count = 0
    last_count = count_products(sb, product_selector) if product_selector else 0

    while pages_crawled < max_pages:
        try:
            if not sb.is_element_visible(button_selector):
                logger.info("Load More button is no longer visible. Stopping.")
                break

            logger.debug("Clicking Load More button...")
            sb.click(button_selector)
            random_sleep(*PAGE_LOAD_WAIT_SEC)

            if product_selector:
                current_count = count_products(sb, product_selector)
                logger.debug(f"Product count: {current_count} (was {last_count})")

                if current_count == last_count:
                    no_change_count += 1
                    if no_change_count >= NO_CHANGE_LIMIT:
                        logger.info(
                            f"Product count unchanged for {NO_CHANGE_LIMIT} consecutive attempts. Stopping."
                        )
                        break
                else:
                    no_change_count = 0
                    pages_crawled += 1
                    last_count = current_count
            else:
                pages_crawled += 1

        except Exception as e:
            logger.error(f"Error interacting with Load More button: {e}")
            break

    return pages_crawled


def handle_next_button(
    sb: Chrome, selector: str, max_pages: int, product_selector: str | None
) -> int:
    """Handle pagination by clicking a Next page link/button."""
    logger.info(f"Executing Next Button strategy (selector: {selector}).")

    pages_crawled = 1
    no_change_count = 0
    last_url = sb.get_current_url()

    while pages_crawled < max_pages:
        try:
            if not sb.is_element_present(selector):
                logger.info("Next button is no longer present in DOM. Stopping.")
                break

            el = sb.find_element(selector)
            cls = el.get_attribute("class") or ""
            if "disabled" in cls.lower() or el.get_attribute("disabled"):
                logger.info("Next button is disabled. Stopping.")
                break

            logger.debug("Clicking Next button...")
            try:
                sb.click(selector)
            except Exception:
                safe_sel = selector.replace('"', '\\"')
                sb.execute_script(f'document.querySelector("{safe_sel}").click();')

            random_sleep(*PAGE_LOAD_WAIT_SEC)

            current_url = sb.get_current_url()
            if current_url == last_url:
                no_change_count += 1
                if no_change_count >= NO_CHANGE_LIMIT:
                    logger.info(
                        f"URL and page state unchanged for {NO_CHANGE_LIMIT} attempts. Stopping."
                    )
                    break
            else:
                no_change_count = 0
                last_url = current_url

            pages_crawled += 1

        except Exception as e:
            logger.error(f"Error interacting with Next button: {e}")
            break

    return pages_crawled


def handle_infinite_scroll(sb: Chrome, max_pages: int) -> int:
    """Handle infinite scroll by scrolling down repeatedly."""
    logger.info("Executing Infinite Scroll strategy.")

    attempts = 0
    pages_crawled = 1

    last_height = sb.execute_script("return document.body.scrollHeight")

    while pages_crawled < max_pages:
        try:
            sb.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            random_sleep(*PAGE_LOAD_WAIT_SEC)

            new_height = sb.execute_script("return document.body.scrollHeight")

            if new_height == last_height:
                attempts += 1
                if attempts >= MAX_STABLE_ATTEMPTS:
                    logger.info(
                        f"Document height stable for {MAX_STABLE_ATTEMPTS} attempts. Stopping."
                    )
                    break
            else:
                attempts = 0
                last_height = new_height
                pages_crawled += 1

        except Exception as e:
            logger.error(f"Error during infinite scroll: {e}")
            break

    return pages_crawled
