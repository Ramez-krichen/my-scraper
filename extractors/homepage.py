"""
homepage.py — Extract category and product URLs from a homepage.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional, Tuple
from urllib.parse import urlparse

try:
    from bs4 import BeautifulSoup  # type: ignore
except ImportError as exc:  # pragma: no cover
    raise ImportError(
        "beautifulsoup4 is required: pip install beautifulsoup4 lxml"
    ) from exc

from .models import HomepageUrls

if TYPE_CHECKING:
    from product_detection.models import ScoringConfig

_EXCLUDED_FRAGMENTS = (
    "#",
    "javascript:",
    "mailto:",
    "tel:",
    "login",
    "signup",
    "register",
    "account",
    "cart",
    "checkout",
    "wishlist",
    "compare",
    "privacy",
    "terms",
    "cookie",
    "search",
    "contact",
    "help",
    "faq",
    "support",
    "tracking",
    "returns",
)

_CATEGORY_HINTS = (
    "category",
    "categories",
    "collection",
    "collections",
    "catalog",
    "shop",
    "store",
    "boutique",
)


def _parse_html(html: str) -> BeautifulSoup:
    try:
        return BeautifulSoup(html, "lxml")
    except Exception:
        return BeautifulSoup(html, "html.parser")


def _is_excluded_href(href: str) -> bool:
    lowered = href.lower()
    return any(fragment in lowered for fragment in _EXCLUDED_FRAGMENTS)


def _same_host(url: str, base_url: str) -> bool:
    if not base_url:
        return True
    try:
        return urlparse(url).netloc == urlparse(base_url).netloc
    except Exception:
        return True


def _anchor_context_hints(tag) -> str:
    attrs = " ".join([tag.get("id") or "", " ".join(tag.get("class") or [])]).lower()
    return attrs


def _is_category_link(url: str, anchor_text: str, context_hints: str) -> bool:
    from page_classifier.signals import url_has_category_hint

    if url_has_category_hint(url):
        return True
    if any(hint in anchor_text for hint in _CATEGORY_HINTS):
        return True
    if any(hint in context_hints for hint in _CATEGORY_HINTS):
        return True
    return False


def extract_homepage_urls(
    html: str,
    url: str = "",
    *,
    config: Optional[ScoringConfig] = None,
) -> HomepageUrls:
    """
    Extract category and product URLs from a homepage.
    Returns HomepageUrls with category_urls, product_urls, and other_urls.
    """
    if not html:
        return HomepageUrls(url=url)

    soup = _parse_html(html)
    cfg = config or ScoringConfig()
    product_patterns = cfg.compiled_product_url_patterns()
    anti_patterns = cfg.compiled_anti_product_patterns()

    selectors = [
        "nav a[href]",
        "header a[href]",
        "main a[href]",
        "a[href]",
    ]

    seen = set()
    category_urls: List[str] = []
    product_urls: List[str] = []
    other_urls: List[str] = []

    for selector in selectors:
        for a in soup.select(selector):
            href = a.get("href")
            if not href:
                continue
            if _is_excluded_href(href):
                continue

            normalized = normalize_url(href, url)
            if not normalized:
                continue
            if not _same_host(normalized, url):
                continue

            if normalized in seen:
                continue
            seen.add(normalized)

            anchor_text = (a.get_text(" ", strip=True) or "").lower()
            context_hints = _anchor_context_hints(a)

            if matches_product_url(normalized, product_patterns, anti_patterns):
                product_urls.append(normalized)
                continue

            if _is_category_link(normalized, anchor_text, context_hints):
                category_urls.append(normalized)
                continue

            other_urls.append(normalized)

    return HomepageUrls(
        url=url,
        category_urls=category_urls,
        product_urls=product_urls,
        other_urls=other_urls,
    )
