from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional


class PageType(str, Enum):
    HOMEPAGE = "homepage"
    PRODUCT_LIST = "product_list"
    PRODUCT_DETAIL = "product_detail"
    CONTENT_LIST = "content_list"
    UNKNOWN = "unknown"


@dataclass
class PaginationInfo:
    has_pagination: bool
    hints: List[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {"has_pagination": self.has_pagination, "hints": list(self.hints)}


@dataclass
class PageClassification:
    page_type: PageType
    confidence: float
    pagination: PaginationInfo = field(default_factory=lambda: PaginationInfo(False, []))
    signals: Dict[str, Any] = field(default_factory=dict)
    notes: str = ""
    winner_blocks: Optional[Any] = None

    def to_dict(self) -> dict:
        return {
            "page_type": self.page_type.value,
            "confidence": round(float(self.confidence), 4),
            "pagination": self.pagination.to_dict(),
            "signals": self.signals,
            "notes": self.notes,
        }


@dataclass
class ScrapeJob:
    job_type: str
    url: str
    page_type: PageType
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict:
        return {
            "job_type": self.job_type,
            "url": self.url,
            "page_type": self.page_type.value,
            "metadata": self.metadata,
        }
