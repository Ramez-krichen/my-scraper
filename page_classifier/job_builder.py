from __future__ import annotations

from typing import Any, Dict

from bs4 import BeautifulSoup

from .classifier import classify_page
from .models import PageType, ScrapeJob


_JOB_TYPE_MAP = {
    PageType.PRODUCT_LIST: "product_list",
    PageType.PRODUCT_DETAIL: "product_detail",
    PageType.CONTENT_LIST: "content_list",
    PageType.HOMEPAGE: "homepage_discovery",
    PageType.UNKNOWN: "unknown",
}


def build_job_from_html(
    html: str,
    url: str,
    *,
    extra_metadata: Dict[str, Any] | None = None,
) -> ScrapeJob:
    """
    Analyze HTML and return a scraper job object with a job_type aligned
    to the detected page type.

    Accepts either raw HTML (str) or a SeleniumBase instance that can
    provide HTML via get_document(), get_page_source(), or page_source.
    """

    soup = BeautifulSoup(html, "lxml")
    classification = classify_page(soup, url)
    page_type = classification.page_type

    job_type = _JOB_TYPE_MAP.get(page_type, "unknown")
    if page_type == PageType.PRODUCT_LIST and classification.pagination.has_pagination:
        job_type = "product_list_paginated"

    metadata = {
        "page_type": page_type.value,
        "confidence": classification.confidence,
        "pagination": classification.pagination.to_dict(),
        "signals": classification.signals,
        "notes": classification.notes,
        "winner_blocks": classification.winner_blocks,
    }
    if extra_metadata:
        metadata.update(extra_metadata)

    return ScrapeJob(job_type=job_type, url=url, page_type=page_type, metadata=metadata)
