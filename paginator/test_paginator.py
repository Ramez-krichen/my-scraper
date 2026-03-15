import logging
from seleniumbase import sb_cdp
from paginator import HybridPaginator
import os
import sys

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

def test_pagination(url: str, expected_type: str = None):
    logger.info(f"--- Testing URL: {url} ---")
    
    # Needs a context manager to ensure safe shutdown
    try:
        # Launch SB CDP instance (headless)
        page = sb_cdp.Chrome(
            headless=True,
            locale='fr-TN'
        )
        
        # Instantiate paginator
        paginator = HybridPaginator(sb=page, start_url=url, max_pages=3)
        
        # Try detection
        page.open(url)
        page.sleep(2) # Give it minimal time to render
        
        paginator.detect_product_container()
        info = paginator.detect_pagination_type()
        
        logger.info(f"Detected Info: {info}")
        if expected_type:
            if info.get('type') == expected_type:
                logger.info(f"✅ Detection matches expected ({expected_type})")
            else:
                logger.warning(f"❌ Detection ({info.get('type')}) differs from expected ({expected_type})")
        
        # Run execution engine (limited to max_pages=3)
        pages_scraped = paginator.run()
        logger.info(f"Test completed. Pages crawled: {pages_scraped}")
        
    except Exception as e:
        logger.error(f"Test failed with exception: {e}")
    finally:
        try:
            if page:
                page.close_active_tab()
        except: pass

if __name__ == "__main__":
    test_cases = [
        # Note: In a real test, these should ideally point to controlled mock HTML files
        # or robust staging environments. Pointing to live prod sites in tests can be flaky.
        ("https://www.comaf.tn/59-plaques-plafonds.html", "url"),
    ]
    
    for url, expected in test_cases:
        test_pagination(url, expected)
