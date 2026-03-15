"""
product_detail.py — Heuristic extraction for product detail pages.
"""
from __future__ import annotations

import json
from typing import Any, Dict, Iterable, List, Optional

try:
    from bs4 import BeautifulSoup  # type: ignore
except ImportError as exc:  # pragma: no cover
    raise ImportError("beautifulsoup4 is required: pip install beautifulsoup4 lxml") from exc

from product_detection.models import ScoringConfig
from product_detection.utils import extract_price_text, normalize_url

from .models import ProductDetail


def _parse_html(html: str) -> BeautifulSoup:
    try:
        return BeautifulSoup(html, "lxml")
    except Exception:
        return BeautifulSoup(html, "html.parser")


def _iter_jsonld_nodes(data: Any) -> Iterable[Dict[str, Any]]:
    if isinstance(data, dict):
        yield data
        for value in data.values():
            yield from _iter_jsonld_nodes(value)
    elif isinstance(data, list):
        for item in data:
            yield from _iter_jsonld_nodes(item)


def _is_product_type(type_value: Any) -> bool:
    if isinstance(type_value, list):
        return any(_is_product_type(v) for v in type_value)
    return isinstance(type_value, str) and "product" in type_value.lower()


def _find_jsonld_product(soup: BeautifulSoup) -> Optional[Dict[str, Any]]:
    for script in soup.find_all("script", attrs={"type": "application/ld+json"}):
        raw = script.string or script.get_text(strip=True)
        if not raw:
            continue
        try:
            data = json.loads(raw)
        except Exception:
            continue

        for node in _iter_jsonld_nodes(data):
            if _is_product_type(node.get("@type")):
                return node

    return None


def _get_meta(soup: BeautifulSoup, *keys: str) -> Optional[str]:
    for key in keys:
        tag = soup.find("meta", attrs={"property": key}) or soup.find(
            "meta", attrs={"name": key}
        )
        if tag and tag.get("content"):
            return str(tag.get("content")).strip()
    return None


def _clean_text(value: Optional[str]) -> Optional[str]:
    if not value:
        return None
    text = " ".join(str(value).split())
    return text[:2000] if text else None


def _extract_offer_fields(offers: Any) -> Dict[str, Optional[str]]:
    if isinstance(offers, list) and offers:
        offers = offers[0]
    if not isinstance(offers, dict):
        return {"price": None, "currency": None, "availability": None, "url": None}

    price = offers.get("price")
    price_spec = offers.get("priceSpecification") or {}
    if not price and isinstance(price_spec, dict):
        price = price_spec.get("price")

    currency = offers.get("priceCurrency")
    if not currency and isinstance(price_spec, dict):
        currency = price_spec.get("priceCurrency")

    availability = offers.get("availability")
    offer_url = offers.get("url")

    return {
        "price": _clean_text(str(price)) if price else None,
        "currency": _clean_text(str(currency)) if currency else None,
        "availability": _clean_text(str(availability)) if availability else None,
        "url": _clean_text(str(offer_url)) if offer_url else None,
    }


def extract_product_detail(
    html: str,
    url: str = "",
    *,
    config: Optional[ScoringConfig] = None,
) -> ProductDetail:
    """
    Extract product detail fields from a page.
    Returns a ProductDetail object with best-effort fields.
    """
    if not html:
        return ProductDetail(url=url)

    soup = _parse_html(html)
    cfg = config or ScoringConfig()

    product_json = _find_jsonld_product(soup) or {}

    title = _clean_text(product_json.get("name"))
    description = _clean_text(product_json.get("description"))

    images: List[str] = []
    raw_images = product_json.get("image")
    if isinstance(raw_images, str):
        images = [raw_images]
    elif isinstance(raw_images, list):
        images = [str(x) for x in raw_images if x]
    elif isinstance(raw_images, dict) and raw_images.get("url"):
        images = [str(raw_images.get("url"))]

    brand = product_json.get("brand")
    if isinstance(brand, dict):
        brand = brand.get("name")
    if brand is not None:
        brand = _clean_text(str(brand))

    sku = product_json.get("sku") or product_json.get("mpn")
    if sku is not None:
        sku = _clean_text(str(sku))

    offer_fields = _extract_offer_fields(product_json.get("offers"))

    # Fallbacks from meta / itemprop / title tags
    if not title:
        title = _get_meta(soup, "og:title", "twitter:title", "title")
    if not title:
        h1 = soup.find("h1")
        title = _clean_text(h1.get_text(" ", strip=True) if h1 else None)
    if not title:
        title_tag = soup.find("title")
        title = _clean_text(title_tag.get_text(" ", strip=True) if title_tag else None)

    if not description:
        description = _get_meta(soup, "og:description", "description")
    if not description:
        desc_tag = soup.select_one('[itemprop="description"]')
        if desc_tag:
            description = _clean_text(desc_tag.get_text(" ", strip=True))

    if not images:
        og_image = _get_meta(soup, "og:image", "twitter:image")
        if og_image:
            images = [og_image]
    if not images:
        img_tag = soup.select_one('[itemprop="image"]')
        if img_tag and img_tag.get("src"):
            images = [str(img_tag.get("src"))]

    price = offer_fields.get("price")
    currency = offer_fields.get("currency")
    availability = offer_fields.get("availability")

    if not price:
        price = _get_meta(
            soup,
            "product:price:amount",
            "og:price:amount",
            "product:price",
        )
    if not currency:
        currency = _get_meta(
            soup,
            "product:price:currency",
            "og:price:currency",
        )
    if not price:
        price_tag = soup.select_one('[itemprop="price"]')
        if price_tag:
            price = _clean_text(
                price_tag.get("content") or price_tag.get_text(" ", strip=True)
            )
    if not currency:
        currency_tag = soup.select_one('[itemprop="priceCurrency"]')
        if currency_tag:
            currency = _clean_text(
                currency_tag.get("content") or currency_tag.get_text(" ", strip=True)
            )

    if not price:
        page_text = soup.get_text(" ", strip=True)
        price = extract_price_text(page_text, cfg.compiled_price_patterns())

    if not sku:
        sku_tag = soup.select_one('[itemprop="sku"], [data-sku]')
        if sku_tag:
            sku = _clean_text(
                sku_tag.get("content")
                or sku_tag.get("data-sku")
                or sku_tag.get_text(" ", strip=True)
            )

    if not brand:
        brand_tag = soup.select_one('[itemprop="brand"], [data-brand]')
        if brand_tag:
            brand = _clean_text(
                brand_tag.get("content")
                or brand_tag.get("data-brand")
                or brand_tag.get_text(" ", strip=True)
            )

    if availability:
        availability = availability.split("/")[-1]

    # Normalize URLs
    images = [normalize_url(img, url) or img for img in images]

    return ProductDetail(
        url=url,
        title=title,
        price=price,
        currency=currency,
        description=description,
        images=images,
        sku=sku,
        brand=brand,
        availability=availability,
    )
