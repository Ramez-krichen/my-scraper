"""
product_detection — Product List Detection and Extraction for e-commerce pages.

Public API
----------
from product_detection import ProductListDetector, ScoringConfig

detector = ProductListDetector()
result = detector.detect(html=raw_html, page_url="https://example.com/shop")
print(result.to_dict())
"""
from .detector import ProductListExtractor
from extractors.product_list import BaseExtractor, HeuristicExtractor, PlatformHintAdapter
from .models import ClusterScore, DetectionResult, ProductItem, ScoringConfig
from .scorer import HeuristicScorer

__all__ = [
    # Main entry point
    "ProductListExtractor",
    # Models
    "DetectionResult",
    "ProductItem",
    "ScoringConfig",
    "ClusterScore",
    # Extensibility
    "BaseExtractor",
    "HeuristicExtractor",
    "HeuristicScorer",
    "PlatformHintAdapter",
]
