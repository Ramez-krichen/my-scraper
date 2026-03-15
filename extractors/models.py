"""
Shared extraction models for structured outputs.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class ProductDetail:
    url: str
    title: Optional[str] = None
    price: Optional[str] = None
    currency: Optional[str] = None
    description: Optional[str] = None
    images: List[str] = field(default_factory=list)
    sku: Optional[str] = None
    brand: Optional[str] = None
    availability: Optional[str] = None

    def to_dict(self) -> dict:
        return {
            "url": self.url,
            "title": self.title,
            "price": self.price,
            "currency": self.currency,
            "description": self.description,
            "images": list(self.images),
            "sku": self.sku,
            "brand": self.brand,
            "availability": self.availability,
        }


@dataclass
class TextContent:
    url: str
    title: Optional[str] = None
    text: str = ""
    excerpt: Optional[str] = None
    language: Optional[str] = None

    def to_dict(self) -> dict:
        return {
            "url": self.url,
            "title": self.title,
            "text": self.text,
            "excerpt": self.excerpt,
            "language": self.language,
        }


@dataclass
class HomepageUrls:
    url: str
    category_urls: List[str] = field(default_factory=list)
    product_urls: List[str] = field(default_factory=list)
    other_urls: List[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "url": self.url,
            "category_urls": list(self.category_urls),
            "product_urls": list(self.product_urls),
            "other_urls": list(self.other_urls),
        }
