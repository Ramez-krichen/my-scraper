"""
test_detector.py — Unit tests for ProductListDetector.

All tests are fully self-contained (no network, no browser).
HTML fixtures are inline and represent real-world structural patterns.
"""
from __future__ import annotations

import pytest
from product_detection import ProductListExtractor, ScoringConfig


# ---------------------------------------------------------------------------
# Fixture builders
# ---------------------------------------------------------------------------

def _prestashop_html(n_products: int = 8) -> str:
    """
    Simulate a PrestaShop 1.7/8 category page structure.
    Products live in <div id="js-product-list"> > <div class="products row"> > <article>
    URLs follow the /-ID.html pattern.
    """
    items = ""
    for i in range(1, n_products + 1):
        items += f"""
        <article class="product-miniature js-product-miniature" itemscope
                 itemtype="http://schema.org/Product">
          <div class="thumbnail-container">
            <a href="/fr/vetements/chemises/{i}-chemise-slim-bleue.html" class="thumbnail product-thumbnail">
              <img src="/img/p/{i}/{i}-medium_default.jpg" alt="Chemise slim bleue" />
            </a>
          </div>
          <div class="product-description">
            <h2 class="h3 product-title">
              <a href="/fr/vetements/chemises/{i}-chemise-slim-bleue.html">Chemise slim bleue</a>
            </h2>
            <div class="product-price-and-shipping">
              <span class="price">
                <span class="product-price">39,90 €</span>
              </span>
            </div>
            <div class="product-list-actions">
              <button class="btn btn-primary add-to-cart" data-button-action="add-to-cart"
                      type="button">
                Ajouter au panier
              </button>
            </div>
          </div>
        </article>
        """
    return f"""<!DOCTYPE html>
<html lang="fr">
<head><title>Catégorie — Ma Boutique PrestaShop</title></head>
<body>
  <main id="main">
    <section id="products">
      <div id="js-product-list">
        <div class="products row">{items}</div>
      </div>
    </section>
  </main>
</body>
</html>"""


def _woocommerce_html(n_products: int = 9) -> str:
    """
    Simulate a WooCommerce shop archive page.
    Products live in <ul class="products columns-3"> > <li class="product">
    URLs follow /product/<slug>/ pattern.
    """
    items = ""
    for i in range(1, n_products + 1):
        items += f"""
        <li class="product type-product post-{1000+i} status-publish instock product_cat-shoes">
          <a href="/product/running-shoe-model-{i}/" class="woocommerce-LoopProduct-link">
            <img src="/wp-content/uploads/shoe-{i}.jpg"
                 class="attachment-woocommerce_thumbnail" alt="Running Shoe {i}" />
            <h2 class="woocommerce-loop-product__title">Running Shoe Model {i}</h2>
            <span class="price">
              <span class="woocommerce-Price-amount amount">
                <bdi>$<span class="woocommerce-Price-currencySymbol">$</span>89.99</bdi>
              </span>
            </span>
          </a>
          <a href="/product/running-shoe-model-{i}/?add-to-cart={1000+i}"
             class="button product_type_simple add_to_cart_button ajax_add_to_cart"
             data-action="add-to-cart">
            Add to cart
          </a>
        </li>
        """
    return f"""<!DOCTYPE html>
<html lang="en-US">
<head><title>Shop — WooCommerce Store</title></head>
<body class="woocommerce">
  <main id="main" class="site-main">
    <div class="woocommerce-notices-wrapper"></div>
    <ul class="products columns-3">{items}</ul>
  </main>
</body>
</html>"""


def _custom_grid_html(n_products: int = 6) -> str:
    """
    Simulate a custom-built e-commerce grid with no platform-specific markers.
    Products are in <div class="catalog"> > <div class="item-card">.
    URLs use /boutique/item/<id> pattern.
    """
    items = ""
    for i in range(1, n_products + 1):
        items += f"""
        <div class="item-card">
          <a href="/boutique/item/{i}" class="item-card__link">
            <img src="/static/items/{i}.jpg" alt="Produit {i}" class="item-card__img" />
          </a>
          <div class="item-card__body">
            <h3 class="item-card__title">
              <a href="/boutique/item/{i}">Super Produit No.{i}</a>
            </h3>
            <p class="item-card__price">{(i * 15) + 9} DT</p>
            <button class="item-card__btn btn-cart" type="button">
              Ajouter au panier
            </button>
          </div>
        </div>
        """
    return f"""<!DOCTYPE html>
<html lang="fr">
<head><title>Boutique — Catalogue</title></head>
<body>
  <div class="container">
    <h1 class="page-title">Notre Catalogue</h1>
    <div class="catalog grid-3">{items}</div>
  </div>
</body>
</html>"""


def _blog_post_list_html(n_posts: int = 7) -> str:
    """
    False-positive scenario: a blog index page with repeated article cards.
    These look structurally like product blocks but should score low because:
      - No price patterns
      - URLs do not match product patterns
      - No add-to-cart signals
      - No schema.org/Product
    """
    items = ""
    for i in range(1, n_posts + 1):
        items += f"""
        <article class="post-card">
          <a href="/blog/2024/post-titre-numero-{i}/" class="post-card__link">
            <img src="/images/blog/{i}.jpg" alt="Article {i}" class="post-card__img" />
          </a>
          <div class="post-card__content">
            <span class="post-card__category">Technology</span>
            <h2 class="post-card__title">
              <a href="/blog/2024/post-titre-numero-{i}/">Titre de l'article No.{i}</a>
            </h2>
            <p class="post-card__excerpt">
              Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod
              tempor incididunt ut labore et dolore magna aliqua.
            </p>
            <a href="/blog/2024/post-titre-numero-{i}/" class="post-card__read-more">
              Lire la suite →
            </a>
          </div>
        </article>
        """
    return f"""<!DOCTYPE html>
<html lang="fr">
<head><title>Blog — Actualités</title></head>
<body>
  <main>
    <h1>Derniers articles</h1>
    <div class="blog-grid">{items}</div>
  </main>
</body>
</html>"""


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestProductListDetector:
    """Unit tests for the full detection pipeline — no browser, no network."""

    def setup_method(self):
        """Create a fresh detector for each test."""
        self.detector = ProductListExtractor()

    # --- PrestaShop ---------------------------------------------------------

    def test_prestashop_like_html(self):
        """Should detect a PrestaShop product grid with high confidence."""
        html = _prestashop_html(n_products=8)
        result = self.detector.detect(html=html, page_url="https://example.com/fr/vetements/")

        assert result.is_product_list is True, (
            f"Expected is_product_list=True, got False (confidence={result.confidence_score:.3f})"
        )
        assert result.confidence_score >= 0.45, (
            f"Confidence too low: {result.confidence_score:.3f}"
        )
        assert len(result.products) >= 4, (
            f"Expected ≥4 products, got {len(result.products)}"
        )
        assert result.container_selector is not None

        # All product URLs should be absolute (page_url provided)
        for p in result.products:
            assert p.url.startswith("http"), f"Non-absolute URL: {p.url}"

    # --- WooCommerce --------------------------------------------------------

    def test_woocommerce_like_html(self):
        """Should detect a WooCommerce products archive with high confidence."""
        html = _woocommerce_html(n_products=9)
        result = self.detector.detect(html=html, page_url="https://shop.example.com/shop/")

        assert result.is_product_list is True, (
            f"Expected is_product_list=True, got False (confidence={result.confidence_score:.3f})"
        )
        assert result.confidence_score >= 0.45, (
            f"Confidence too low: {result.confidence_score:.3f}"
        )
        assert len(result.products) >= 4
        # At least one product should carry a price
        prices = [p.price for p in result.products if p.price]
        assert len(prices) >= 1, "Expected at least one extracted price"

    # --- Custom grid --------------------------------------------------------

    def test_custom_grid_html(self):
        """
        Should detect a custom-built product grid even with no platform markers.
        Validates that the module is not brittle on unseen structures.
        """
        html = _custom_grid_html(n_products=6)
        result = self.detector.detect(html=html, page_url="https://myshop.tn/boutique/")

        assert result.is_product_list is True, (
            f"Custom grid not detected (confidence={result.confidence_score:.3f})"
        )
        assert len(result.products) >= 4
        # Prices in DT should be extracted
        prices = [p.price for p in result.products if p.price]
        assert len(prices) >= 1, "Expected at least one DT price to be extracted"

    # --- False positive: blog list ------------------------------------------

    def test_false_positive_blog_post_list(self):
        """
        A blog post listing should NOT be classified as a product list.
        Must either return is_product_list=False OR confidence < 0.30.
        """
        html = _blog_post_list_html(n_posts=7)
        result = self.detector.detect(html=html, page_url="https://example.com/blog/")

        not_detected = (not result.is_product_list) or (result.confidence_score < 0.30)
        assert not_detected, (
            f"False positive: blog detected as product list "
            f"(confidence={result.confidence_score:.3f}, products={len(result.products)})"
        )

    # --- API surface --------------------------------------------------------

    def test_detect_with_none_inputs_returns_negative(self):
        """Calling detect() with no arguments should not raise but return negative."""
        result = self.detector.detect()
        assert result.is_product_list is False
        assert result.confidence_score == 0.0
        assert result.products == []

    def test_to_dict_schema(self):
        """The to_dict() output must match the required JSON schema."""
        html = _prestashop_html(n_products=5)
        result = self.detector.detect(html=html, page_url="https://example.com/")
        d = result.to_dict()

        assert "is_product_list" in d
        assert "confidence_score" in d
        assert "container_selector" in d
        assert "products" in d

        for product in d["products"]:
            assert "url" in product
            assert "title" in product
            assert "price" in product

    def test_custom_config_injection(self):
        """
        Verify that custom ScoringConfig is honoured — raising min_cluster_size
        to a very high value should make it impossible to declare a product list.
        """
        strict_config = ScoringConfig(min_cluster_size=100)  # impossible threshold
        detector = ProductListExtractor(config=strict_config)
        html = _prestashop_html(n_products=8)
        result = detector.detect(html=html)
        # With cluster size of 100, nothing should pass
        assert result.is_product_list is False

    def test_no_duplicates_in_product_urls(self):
        """Product URL deduplication must remove exact duplicates."""
        html = _woocommerce_html(n_products=9)
        result = self.detector.detect(html=html, page_url="https://example.com/shop/")
        urls = [p.url for p in result.products]
        assert len(urls) == len(set(urls)), "Duplicate product URLs found"
