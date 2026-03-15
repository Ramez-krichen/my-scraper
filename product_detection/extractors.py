"""
Compatibility shim for product list extractors.

Extraction logic now lives in extractors/product_list.py.
"""
from extractors.product_list import BaseExtractor, HeuristicExtractor, PlatformHintAdapter

__all__ = [
    "BaseExtractor",
    "HeuristicExtractor",
    "PlatformHintAdapter",
]
