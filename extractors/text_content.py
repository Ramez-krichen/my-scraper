"""
text_content.py — Heuristic extraction for readable text content.
"""
from __future__ import annotations

from typing import Optional

try:
    from bs4 import BeautifulSoup  # type: ignore
except ImportError as exc:  # pragma: no cover
    raise ImportError("beautifulsoup4 is required: pip install beautifulsoup4 lxml") from exc

from .models import TextContent


def _parse_html(html: str) -> BeautifulSoup:
    try:
        return BeautifulSoup(html, "lxml")
    except Exception:
        return BeautifulSoup(html, "html.parser")


def _clean_text(value: Optional[str]) -> Optional[str]:
    if not value:
        return None
    text = " ".join(str(value).split())
    return text if text else None


def _get_meta(soup: BeautifulSoup, *keys: str) -> Optional[str]:
    for key in keys:
        tag = soup.find("meta", attrs={"property": key}) or soup.find(
            "meta", attrs={"name": key}
        )
        if tag and tag.get("content"):
            return _clean_text(str(tag.get("content")))
    return None


def _select_best_container(soup: BeautifulSoup) -> BeautifulSoup:
    selectors = [
        "article",
        "main",
        "section#content",
        "div#content",
        "div.content",
        "section.article",
    ]
    best = None
    best_len = 0
    for selector in selectors:
        for tag in soup.select(selector):
            text_len = len(tag.get_text(" ", strip=True))
            if text_len > best_len:
                best_len = text_len
                best = tag

    if best is not None:
        return best

    return soup.body or soup


def extract_text_content(html: str, url: str = "") -> TextContent:
    """
    Extract readable text content from a page.
    Returns a TextContent object with best-effort fields.
    """
    if not html:
        return TextContent(url=url)

    soup = _parse_html(html)
    title = _get_meta(soup, "og:title", "twitter:title", "title")
    if not title:
        h1 = soup.find("h1")
        title = _clean_text(h1.get_text(" ", strip=True) if h1 else None)
    if not title:
        title_tag = soup.find("title")
        title = _clean_text(title_tag.get_text(" ", strip=True) if title_tag else None)

    lang = None
    html_tag = soup.find("html")
    if html_tag and html_tag.get("lang"):
        lang = _clean_text(html_tag.get("lang"))

    container = _select_best_container(soup)

    # Remove common non-content elements
    for tag in container.find_all(
        ["script", "style", "noscript", "nav", "header", "footer", "aside", "form"]
    ):
        tag.decompose()

    text = _clean_text(container.get_text(" ", strip=True)) or ""

    excerpt = None
    if text:
        excerpt = text[:300] + ("..." if len(text) > 300 else "")

    return TextContent(url=url, title=title, text=text, excerpt=excerpt, language=lang)
