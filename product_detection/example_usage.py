"""
example_usage.py — Demonstrates the three primary usage modes
of the ProductListDetector module.

Run from the project root:
    .venv\\Scripts\\python.exe product_detection\\example_usage.py
"""
from __future__ import annotations

import json
import sys
import textwrap

# ---------------------------------------------------------------------------
# Ensure the project root is on the path when running directly
# ---------------------------------------------------------------------------
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from product_detection import ProductListExtractor, ScoringConfig


# ---------------------------------------------------------------------------
# Shared pretty-printer
# ---------------------------------------------------------------------------

def print_result(label: str, result) -> None:
    d = result.to_dict()
    print(f"\n{'='*60}")
    print(f"  {label}")
    print(f"{'='*60}")
    print(f"  is_product_list   : {d['is_product_list']}")
    print(f"  confidence_score  : {d['confidence_score']}")
    print(f"  container_selector: {d['container_selector']}")
    print(f"  products found    : {len(d['products'])}")
    if d["products"]:
        print("\n  Sample products:")
        for p in d["products"][:3]:
            print(f"    URL  : {p['url']}")
            print(f"    Title: {p['title']}")
            print(f"    Price: {p['price']}")
            print()


# ---------------------------------------------------------------------------
# Mode 1 — From raw HTML string
# ---------------------------------------------------------------------------

SAMPLE_HTML = textwrap.dedent("""\
    <!DOCTYPE html>
    <html lang="en">
    <body>
      <main>
        <ul class="products columns-4">
          <li class="product post-101">
            <a href="/product/blue-sneaker-101/">
              <img src="/img/101.jpg" alt="Blue Sneaker" />
              <h2 class="woocommerce-loop-product__title">Blue Sneaker</h2>
              <span class="price">$59.99</span>
            </a>
            <a href="/product/blue-sneaker-101/?add-to-cart=101"
               class="button add_to_cart_button">Add to cart</a>
          </li>
          <li class="product post-102">
            <a href="/product/red-trainer-102/">
              <img src="/img/102.jpg" alt="Red Trainer" />
              <h2 class="woocommerce-loop-product__title">Red Trainer</h2>
              <span class="price">$74.99</span>
            </a>
            <a href="/product/red-trainer-102/?add-to-cart=102"
               class="button add_to_cart_button">Add to cart</a>
          </li>
          <li class="product post-103">
            <a href="/product/green-boot-103/">
              <img src="/img/103.jpg" alt="Green Boot" />
              <h2 class="woocommerce-loop-product__title">Green Boot</h2>
              <span class="price">$89.00</span>
            </a>
            <a href="/product/green-boot-103/?add-to-cart=103"
               class="button add_to_cart_button">Add to cart</a>
          </li>
          <li class="product post-104">
            <a href="/product/white-runner-104/">
              <img src="/img/104.jpg" alt="White Runner" />
              <h2 class="woocommerce-loop-product__title">White Runner</h2>
              <span class="price">$65.50</span>
            </a>
            <a href="/product/white-runner-104/?add-to-cart=104"
               class="button add_to_cart_button">Add to cart</a>
          </li>
          <li class="product post-105">
            <a href="/product/black-hiker-105/">
              <img src="/img/105.jpg" alt="Black Hiker" />
              <h2 class="woocommerce-loop-product__title">Black Hiker</h2>
              <span class="price">$110.00</span>
            </a>
            <a href="/product/black-hiker-105/?add-to-cart=105"
               class="button add_to_cart_button">Add to cart</a>
          </li>
        </ul>
      </main>
    </body>
    </html>
""")


def demo_from_raw_html():
    """Mode 1: Detect from a raw HTML string."""
    detector = ProductListExtractor()
    result = detector.detect(html=SAMPLE_HTML, page_url="https://mystore.example.com/shop/")
    print_result("Mode 1 — From raw HTML string", result)
    return result


# ---------------------------------------------------------------------------
# Mode 2 — From a pre-parsed BeautifulSoup object
# ---------------------------------------------------------------------------

def demo_from_soup():
    """Mode 2: Detect from a pre-parsed BeautifulSoup object."""
    try:
        from bs4 import BeautifulSoup
    except ImportError:
        print("beautifulsoup4 not installed — skipping Mode 2 demo")
        return

    soup = BeautifulSoup(SAMPLE_HTML, "lxml")
    detector = ProductListExtractor()
    result = detector.detect(soup=soup, page_url="https://mystore.example.com/shop/")
    print_result("Mode 2 — From pre-parsed BeautifulSoup", result)
    return result


# ---------------------------------------------------------------------------
# Mode 3 — Custom config with injected regex rules
# ---------------------------------------------------------------------------

def demo_custom_config():
    """Mode 3: Inject a custom ScoringConfig with extra URL patterns."""
    custom_config = ScoringConfig(
        min_cluster_size=3,            # Accept smaller grids
        weight_price_match=2.0,        # Prioritise price signal
        product_url_patterns=[
            r"/product[s]?/",
            r"/produit[s]?/",
            r"/shop/",
            r"[/-]\d+[/-]",
            r"-\d+\.html$",
            r"/catalogue/ref-\d+",    # Custom pattern for a specific platform
            r"/items/\w+-\d+",        # Another custom pattern
        ],
    )
    detector = ProductListExtractor(config=custom_config)
    result = detector.detect(html=SAMPLE_HTML, page_url="https://mystore.example.com/shop/")
    print_result("Mode 3 — Custom ScoringConfig", result)
    return result


# ---------------------------------------------------------------------------
# Mode 4 — SeleniumBase adapter (requires running browser, shown as snippet)
# ---------------------------------------------------------------------------

SELENIUMBASE_SNIPPET = """
# Mode 4 — SeleniumBase adapter (requires active SB instance):

from seleniumbase import sb_cdp
from product_detection import ProductListDetector

detector = ProductListDetector()

with sb_cdp.Chrome(headless=True) as sb:
    result = detector.detect_from_sb(sb=sb, url="https://example.com/shop")
    print(result.to_dict())
"""

# ---------------------------------------------------------------------------
# Mode 5 — Playwright adapter (shown as snippet)
# ---------------------------------------------------------------------------

PLAYWRIGHT_SNIPPET = """
# Mode 5 — Playwright adapter (requires active Playwright page):

from playwright.sync_api import sync_playwright
from product_detection import ProductListDetector

detector = ProductListDetector()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://example.com/shop")
    result = detector.detect_from_playwright(page=page, url=page.url)
    print(result.to_dict())
    browser.close()
"""


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("\n" + "="*60)
    print("  Product List Detector — Example Usage")
    print("="*60)

    r1 = demo_from_raw_html()
    r2 = demo_from_soup()
    r3 = demo_custom_config()

    print("\n" + "="*60)
    print("  SeleniumBase Adapter (code snippet only — needs live browser)")
    print("="*60)
    print(SELENIUMBASE_SNIPPET)

    print("\n" + "="*60)
    print("  Playwright Adapter (code snippet only — needs live browser)")
    print("="*60)
    print(PLAYWRIGHT_SNIPPET)

    # JSON dump for integration testing
    if r1:
        print("\nFull JSON output (Mode 1):")
        print(json.dumps(r1.to_dict(), indent=2, ensure_ascii=False))
