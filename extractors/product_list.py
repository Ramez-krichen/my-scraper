"""
product_list.py — BaseExtractor ABC + HeuristicExtractor + PlatformHintAdapter.

This module hosts product list extraction logic and can be used directly
or via ProductListDetector.
"""
from __future__ import annotations

import logging
import re
from abc import ABC, abstractmethod
from collections import defaultdict
from typing import Dict, List, Optional, Tuple

try:
    from bs4 import BeautifulSoup, NavigableString, Tag  # type: ignore
except ImportError as exc:  # pragma: no cover
    raise ImportError("beautifulsoup4 is required: pip install beautifulsoup4 lxml") from exc

from product_detection.models import ClusterScore, ProductItem, ScoringConfig
from product_detection.utils import (
    describe_selector,
    extract_price_text,
    extract_title_from_tag,
    get_tag_key,
    is_excluded_url,
    matches_product_url,
    normalize_url,
)

logger = logging.getLogger(__name__)

# Tags that are unlikely to produce semantic product containers
_STRUCTURAL_TAGS = frozenset(
    ["html", "head", "body", "main", "header", "footer",
     "nav", "script", "style", "meta", "link", "noscript",
     "br", "svg", "span", "path", "i", "input", "option", "stop",
     "button", "a", "img"]
)


# ---------------------------------------------------------------------------
# Abstract base
# ---------------------------------------------------------------------------

class BaseExtractor(ABC):
    """
    Abstract interface for product block extractors.

    Subclass and override `find_candidate_clusters` and/or `extract_products`
    to plug in platform-specific logic while keeping the orchestration layer
    (product_detection.detector) unchanged.
    """

    @abstractmethod
    def find_candidate_clusters(
        self, soup: BeautifulSoup, target_signature: Optional[str] = None
    ) -> List[Tuple[List[Tag], Tag, str]]:
        """
        Traverse the DOM and return candidate clusters of repeating blocks.

        Returns
        -------
        List of (blocks, parent_tag, child_key) tuples, where:
          - blocks     : list of sibling Tag objects forming the cluster
          - parent_tag : the common parent Tag
          - child_key  : the structural key string (tag::classes)
        """
        ...

    @abstractmethod
    def extract_products(
        self,
        blocks: List[Tag],
        base_url: str = "",
    ) -> List[ProductItem]:
        """Extract ProductItem objects from a validated cluster of blocks."""
        ...


# ---------------------------------------------------------------------------
# Heuristic extractor
# ---------------------------------------------------------------------------

class HeuristicExtractor(BaseExtractor):
    """
    Platform-agnostic extractor that groups sibling elements by their
    structural signature (tag name + CSS class set) and treats large
    groups as repeating product blocks.

    Detection is intentionally structural — it does NOT rely on specific
    class names and works on unseen e-commerce platforms.
    """

    def __init__(self, config: ScoringConfig) -> None:
        self.config = config
        self._product_url_re = config.compiled_product_url_patterns()
        self._price_re = config.compiled_price_patterns()

    # ------------------------------------------------------------------
    # Cluster detection
    # ------------------------------------------------------------------

    def find_candidate_clusters(
        self, soup: BeautifulSoup, target_signature: Optional[str] = None
    ) -> List[Tuple[List[Tag], Tag, str]]:
        """
        Walk every non-structural parent and group its direct children
        by (tag_name, sorted_classes).  Groups with >= min_cluster_size
        elements are returned as candidates.
        """
        min_size = 2 or self.config.min_cluster_size
        candidates: List[Tuple[List[Tag], Tag, str]] = []

        for parent in soup.find_all(True):
            if getattr(parent, "name", None) in _STRUCTURAL_TAGS:
                continue

            # Map child key -> list of direct child Tags
            groups: Dict[str, List[Tag]] = defaultdict(list)
            for child in parent.children:
                if isinstance(child, NavigableString):
                    continue
                if getattr(child, "name", None) in _STRUCTURAL_TAGS:
                    continue
                key = get_tag_key(child)
                groups[key].append(child) # type: ignore

            for key, group in groups.items():
                if len(group) >= min_size or (target_signature and key == target_signature):
                    candidates.append((group, parent, key))

        # Deduplicate: remove clusters that are subsets of a larger one
        candidates = self._deduplicate_clusters(candidates)
        logger.debug("Found %d candidate clusters", len(candidates))
        return candidates

    def _deduplicate_clusters(
        self, clusters: List[Tuple[List[Tag], Tag, str]]
    ) -> List[Tuple[List[Tag], Tag, str]]:
        """
        Remove redundant sub-clusters.  If cluster A's block IDs are a
        strict subset of cluster B's block IDs, A is dropped.
        """
        # Build sets of element ids for each cluster
        id_sets = [frozenset(id(b) for b in c[0]) for c in clusters]
        keep = []
        for i, (cluster, id_set) in enumerate(zip(clusters, id_sets)):
            dominated = False
            for j, other_set in enumerate(id_sets):
                if i != j and id_set < other_set:
                    dominated = True
                    break
            if not dominated:
                keep.append(cluster)
        return keep

    # ------------------------------------------------------------------
    # Product extraction from a validated cluster
    # ------------------------------------------------------------------

    def extract_products(
        self,
        blocks: List[Tag],
        base_url: str = "",
        index: int = 0,
    ) -> List[ProductItem]:
        """
        Extract a ProductItem for each block in *blocks*.
        Blocks that yield no valid product URL are silently skipped.
        """
        seen_urls: set = set()
        products: List[ProductItem] = []

        for i in range(index, len(blocks)):
            url = self.extract_product_url(blocks[i], base_url)
            if not url or url in seen_urls:
                continue
            seen_urls.add(url)

            title = extract_title_from_tag(blocks[i])
            price = extract_price_text(blocks[i].get_text(" ", strip=True), self._price_re)

            products.append(ProductItem(url=url, title=title, price=price))

        return products

    def extract_product_url(self, block: Tag, base_url: str = "") -> Optional[str]:
        """
        Find the best product anchor in *block*.

        Preference order:
          1. Anchor whose href matches a product URL pattern (not excluded)
          2. Any non-excluded, non-trivial anchor
        """
        cfg = self.config
        candidates = []

        for a in block.find_all("a", href=True):
            raw_href = a.get("href")
            href = str(raw_href).strip() if raw_href else ""
            if not href:
                continue
            if is_excluded_url(href, cfg.excluded_url_fragments, cfg.excluded_url_exact):
                continue
            norm = normalize_url(href, base_url)
            if not norm:
                continue
            is_product = matches_product_url(href, self._product_url_re)
            candidates.append((norm, is_product))

        if not candidates:
            return None

        # Prefer a confirmed product URL
        for url, is_product in candidates:
            if is_product:
                return url

        # Fall back to first non-excluded anchor
        return candidates[0][0]


# ---------------------------------------------------------------------------
# Optional PlatformHintAdapter
# ---------------------------------------------------------------------------

class PlatformHintAdapter:
    """
    Optional pre-filter that narrows the search scope to a platform-specific
    sub-tree before running the HeuristicExtractor.

    This is NOT required — the heuristic extractor works without it.
    Providing platform hints can improve recall on well-known platforms
    and reduce false positives on complex page layouts.
    """

    # Platform hint table: (platform_name, container_selector_hint)
    # These are optional hints, not hard requirements.
    PLATFORM_HINTS: List[Tuple[str, str]] = [
        ("prestashop",  "#products"),
        ("prestashop",  "#js-product-list"),
        ("woocommerce", "ul.products"),
        ("woocommerce", "div.products"),
        ("woocommerce", ".woocommerce-loop-product"),
        ("woocommerce", "div[class*=wd-products-holder]"),
        ("shopify",     ".collection-grid"),
        ("shopify",     ".product-grid"),
        ("shopify",     "[id*='product-grid']"),
        ("magento",     ".products-grid"),
        ("magento",     ".product-items"),
        ("opencart",    "#product-category"),
        ("opencart",    ".product-layout"),
        ("bigcommerce", ".productGrid"),
        ("bigcommerce", "[id^='product-listing-container']"),
        ("wix",         "[data-mesh-id*='container']"),
        ("squarespace", ".sqs-shop-style-inline"),
        ("squarespace", ".ProductList-grid"),
        ("generic",     'ol[class*="produit"]'),
        ("generic",     '[class*="product-list"]'),
        ("generic",     'ul[class*="product_list"]'),
        ("generic",     '[class*="product-grid"]'),
        ("generic",     '[class*="product_grid"]'),
        ("generic",     '[class*="catalog-grid"]'),
        ("generic",     '[class*="catalog_grid"]'),
        ("generic",     '[class*="item-list"]'),
        ("generic",     '[id*="product-list"]'),
        ("generic",     'main ul[class*="grid"]'),
    ]

    def __init__(self, config: ScoringConfig) -> None:
        self.config = config
        self._price_re = config.compiled_price_patterns()
        self._product_url_re = config.compiled_product_url_patterns()
        self._anti_product_url_re = config.compiled_anti_product_patterns()
        self._add_to_cart_text_re = re.compile(
            "|".join(re.escape(k) for k in config.add_to_cart_keywords),
            re.IGNORECASE,
        )
        self._add_to_cart_class_re = re.compile(
            "|".join(re.escape(k) for k in config.add_to_cart_class_fragments),
            re.IGNORECASE,
        )
        self._schema_product_re = re.compile(r"schema\.org/Product|Product", re.IGNORECASE)

    def narrow(self, soup: BeautifulSoup, base_url: str = "") -> BeautifulSoup:
        """
        Try each platform hint selector. Return a minimal soup wrapping
        the best matching sub-tree based on product indicators, or the
        original soup if nothing matches.
        """
        best_container: Optional[Tag] = None
        best_score: Optional[Tuple[float, float, int, int, int, int, int]] = None
        best_platform: Optional[str] = None
        best_selector: Optional[str] = None
        best_order: Optional[int] = None

        for order, (_platform, selector) in enumerate(self.PLATFORM_HINTS):
            try:
                containers = soup.select(selector)
                if not containers:
                    continue

                candidates = self._expand_candidates(containers)
                for container in candidates:
                    if not self._is_meaningful(container):
                        continue
                    score = self._score_container(container, base_url)
                    if (
                        best_score is None
                        or score > best_score
                        or (score == best_score and (best_order is None or order < best_order))
                    ):
                        best_container = container
                        best_score = score
                        best_platform = _platform
                        best_selector = selector
                        best_order = order
            except Exception:
                continue

        if best_container is not None:
            logger.debug(
                "PlatformHintAdapter matched selector '%s' for '%s' (score=%s)",
                best_selector, best_platform, best_score,
            )
            # Wrap in a minimal soup so HeuristicExtractor's parent
            # traversal still works correctly.
            wrapper = BeautifulSoup(str(best_container), "lxml")
            return wrapper
        return soup

    def _is_meaningful(self, tag: Tag) -> bool:
        """A container is meaningful if it has at least min_cluster_size children."""
        children = [c for c in tag.children if isinstance(c, Tag)]
        return len(children) >= self.config.min_cluster_size

    def _expand_candidates(self, containers: List[Tag]) -> List[Tag]:
        """
        Expand raw selector matches into a candidate list.
        If many items share the same parent (common in item-level selectors),
        consider the parent as a candidate container as well.
        """
        if not containers:
            return []

        seed_candidates: List[Tag] = []
        if len(containers) > 1:
            parents = {c.parent for c in containers if isinstance(c.parent, Tag)}
            if len(parents) == 1:
                parent = next(iter(parents))
                if getattr(parent, "name", None) not in _STRUCTURAL_TAGS:
                    seed_candidates.append(parent)

        # Preserve original order, de-duplicate by identity
        candidates: List[Tag] = []
        seen: set = set()
        for container in seed_candidates + containers:
            cid = id(container)
            if cid in seen:
                continue
            seen.add(cid)
            candidates.append(container)
        return candidates

    def _score_container(self, tag: Tag, base_url: str = "") -> Tuple[float, float, int, int, int, int, int]:
        """
        Score a candidate container using lightweight product-list indicators.
        Higher is better. Uses add-to-cart signals, product-like URLs, and prices.
        """
        add_to_cart_hits = self._count_add_to_cart(tag)
        product_url_hits = self._count_product_urls(tag, base_url)
        price_hits = self._count_price_hits(tag)
        schema_hits = 1 if self._has_schema_product(tag) else 0
        children = [c for c in tag.children if isinstance(c, Tag)]
        child_count = len(children)
        descendant_count = len(tag.find_all(True))

        indicator_score = add_to_cart_hits * 3 + product_url_hits * 2 + price_hits + schema_hits
        density = indicator_score / max(descendant_count, 1)
        return (
            float(indicator_score),
            float(density),
            add_to_cart_hits,
            product_url_hits,
            price_hits,
            child_count,
            -descendant_count,
        )

    def _count_add_to_cart(self, tag: Tag) -> int:
        """Count add-to-cart indicators within a container."""
        hits = 0
        for el in tag.find_all(["button", "a", "input"]):
            text = el.get_text(strip=True)
            if text and self._add_to_cart_text_re.search(text):
                hits += 1
                continue
            classes = " ".join(el.get("class") or [])
            if classes and self._add_to_cart_class_re.search(classes):
                hits += 1
                continue
            for attr in ("data-action", "aria-label", "title", "value"):
                val = el.get(attr, "")
                if val and self._add_to_cart_text_re.search(str(val)):
                    hits += 1
                    break
        return hits

    def _count_product_urls(self, tag: Tag, base_url: str = "") -> int:
        """Count distinct product-like URLs within a container."""
        cfg = self.config
        hits: set = set()
        for a in tag.find_all("a", href=True):
            href = str(a.get("href") or "").strip()
            if not href:
                continue
            if is_excluded_url(href, cfg.excluded_url_fragments, cfg.excluded_url_exact):
                continue
            if not matches_product_url(href, self._product_url_re, self._anti_product_url_re):
                continue
            norm = normalize_url(href, base_url) or href
            hits.add(norm)
        return len(hits)

    def _count_price_hits(self, tag: Tag) -> int:
        """Count price-like text matches in a container (capped)."""
        text = tag.get_text(" ", strip=True)
        if not text:
            return 0
        hits = 0
        for regex in self._price_re:
            hits += len(regex.findall(text))
            if hits >= 20:
                return 20
        return hits

    def _has_schema_product(self, tag: Tag) -> bool:
        """True if the container has schema.org Product markup."""
        if tag.find(attrs={"itemtype": self._schema_product_re}):
            return True
        if tag.find(attrs={"itemscope": True, "itemtype": self._schema_product_re}):
            return True
        return False


# ---------------------------------------------------------------------------
# Convenience API
# ---------------------------------------------------------------------------

def extract_product_list_items(
    html: str,
    url: str = "",
    winner_blocks: Optional[ClusterScore] = None,
    config: Optional[ScoringConfig] = None,
) -> List[ProductItem]:
    """
    Extract product list items from a page using the full detection pipeline.
    Returns an empty list if no list is detected.
    """
    # Local import to avoid circular dependency at module load time.
    from product_detection.detector import ProductListExtractor

    productListExtractor = ProductListExtractor(config=config)

    target_sig = winner_blocks.class_signature if winner_blocks else None

    if target_sig:
        logger.debug("Using provided winner blocks pattern: %s", target_sig)

    result = productListExtractor.detect(html=html, page_url=url, target_signature=target_sig)
    return result.products
