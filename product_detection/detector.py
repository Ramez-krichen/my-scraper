"""
detector.py — ProductListDetector: orchestrator for the detection pipeline.

This is the main entry point for the product_detection module.
"""
from __future__ import annotations

import logging
from typing import List, Optional, Tuple

try:
    from bs4 import BeautifulSoup, Tag  # type: ignore
except ImportError as exc:  # pragma: no cover
    raise ImportError("beautifulsoup4 is required: pip install beautifulsoup4 lxml") from exc

from extractors.product_list import HeuristicExtractor, PlatformHintAdapter
from .models import ClusterScore, DetectionResult, ProductItem, ScoringConfig
from .scorer import HeuristicScorer
from .utils import describe_selector

logger = logging.getLogger(__name__)


class ProductListExtractor:
    """
    Orchestrates the full product-list detection pipeline.

    Pipeline
    --------
    1. Normalise input  → BeautifulSoup
    2. Optional platform-hint narrowing (PlatformHintAdapter)
    3. Find candidate clusters  (HeuristicExtractor)
    4. Score each cluster        (HeuristicScorer)
    5. Select winning cluster    (highest composite score)
    6. Compute public confidence score
    7. Extract products          (HeuristicExtractor)
    8. Return DetectionResult

    Usage
    -----
    detector = ProductListDetector()
    """

    NEGATIVE_RESULT = DetectionResult(
        is_product_list=False,
        confidence_score=0.0,
        container_selector=None,
        products=[],
    )

    def __init__(
        self,
        config: Optional[ScoringConfig] = None,
        use_platform_hints: bool = True,
    ) -> None:
        self.config = config or ScoringConfig()
        self.extractor = HeuristicExtractor(self.config)
        self.scorer = HeuristicScorer(self.config)
        self._adapter = PlatformHintAdapter(self.config) if use_platform_hints else None

    # ------------------------------------------------------------------
    # Main entry points
    # ------------------------------------------------------------------

    def detect(
        self,
        html: Optional[str] = None,
        soup: Optional[BeautifulSoup] = None,
        page_url: str = "",
        target_signature: Optional[str] = None,
    ) -> DetectionResult:
        """
        Detect product listings from raw HTML or a pre-parsed BeautifulSoup.

        Parameters
        ----------
        html             : Raw HTML string (provide this or soup, not both).
        soup             : Pre-parsed BeautifulSoup object.
        page_url         : Source URL of the page — used for URL normalization
                           and relative→absolute resolution.
        target_signature : Structural signature from a previous page's winner
                           to enforce selection across pagination.

        Returns
        -------
        DetectionResult (always safe to use; is_product_list=False on failure)
        """
        if soup is None and html is None:
            logger.warning("detect() called with neither html nor soup — returning negative")
            return self.NEGATIVE_RESULT

        if soup is None:
            try:
                soup = BeautifulSoup(html or "", "lxml")
            except Exception:
                soup = BeautifulSoup(html or "", "html.parser")

        return self._run_pipeline(soup, page_url, target_signature)

    def detect_from_sb(self, sb, url: str = "", target_signature: Optional[str] = None) -> DetectionResult:
        """
        Adapter: extract HTML via a SeleniumBase CDP instance and run detection.

        Parameters
        ----------
        sb               : An active `seleniumbase.core.sb_cdp.Chrome` instance
                           (or any object with a `get_page_source()` / `get_current_page_source()`
                           / `execute_script` method).
        url              : Page URL (used for absolute URL resolution).
        target_signature : Structural signature to enforce selection.
        """
        html = self._get_html_from_sb(sb, url)
        if not html:
            logger.warning("detect_from_sb: could not retrieve page source")
            return self.NEGATIVE_RESULT
        return self.detect(html=html, page_url=url, target_signature=target_signature)

    def detect_from_playwright(self, page, url: str = "", target_signature: Optional[str] = None) -> DetectionResult:
        """
        Adapter: extract HTML from a Playwright Page object and run detection.

        Parameters
        ----------
        page             : A `playwright.sync_api.Page` (sync) or
                           `playwright.async_api.Page` (async — caller must await content()).
        url              : Page URL (used for absolute URL resolution).
        target_signature : Structural signature to enforce selection.
        """
        try:
            html = page.content()
        except Exception as exc:
            logger.warning("detect_from_playwright: failed to get content — %s", exc)
            return self.NEGATIVE_RESULT
        return self.detect(html=html, page_url=url, target_signature=target_signature)

    # ------------------------------------------------------------------
    # Internal pipeline
    # ------------------------------------------------------------------

    def get_container_block(self, soup: BeautifulSoup, page_url: str, target_signature: Optional[str] = None) -> Optional[ClusterScore]:
        # Step 1 — Optional platform narrowing
        working_soup = soup
        if self._adapter is not None:
            working_soup = self._adapter.narrow(soup, page_url)

        # Step 2 — Find candidate clusters
        raw_candidates = self.extractor.find_candidate_clusters(working_soup, target_signature=target_signature)
        if not raw_candidates:
            logger.debug("No repeating clusters found")
            return None

        # Step 3 — Score every cluster
        scored: List[ClusterScore] = []
        for blocks, parent_tag, child_key in raw_candidates:
            cs = self.scorer.score_cluster(blocks, parent_tag, child_key)
            scored.append(cs)

        if not scored:
            return None

        # Step 4 — Select winner (highest composite score or target_signature)
        winner = None
        if target_signature:
            for cs in scored:
                if cs.class_signature == target_signature:
                    winner = cs
                    break

        if not winner:
            winner = max(scored, key=lambda s: s.composite_score)

        logger.debug(
            "Winning cluster: key=%s, blocks=%d, composite=%.3f",
            winner.class_signature, winner.block_count, winner.composite_score,
        )

        return winner

    def _run_pipeline(self, soup: BeautifulSoup, page_url: str, target_signature: Optional[str] = None) -> DetectionResult:
        """Core detection pipeline (runs on an already-parsed soup)."""

        winner = self.get_container_block(soup, page_url, target_signature)

        if winner is None:
            return self.NEGATIVE_RESULT

        # Step 5 — Compute public confidence
        confidence = self.scorer.compute_confidence(winner)

        # Step 6 — Threshold check
        if confidence < self.config.min_confidence_to_declare:
            if target_signature and winner.class_signature == target_signature:
                logger.debug("Confidence %.3f below threshold but matching target_signature — keeping it.", confidence)
                confidence = max(confidence, self.config.min_confidence_to_declare)
            else:
                logger.debug("Confidence %.3f below threshold %.3f — not a product list",
                             confidence, self.config.min_confidence_to_declare)
                return DetectionResult(
                    is_product_list=False,
                    confidence_score=confidence,
                    container_selector=None,
                    products=[],
                )

        # Step 7 — Extract products
        products = self.extractor.extract_products(winner.blocks, base_url=page_url)

        # Step 8 — Build container selector descriptor
        # Retrieve the actual parent Tag object for describe_selector
        parent_tag_obj = winner.blocks[0].parent if winner.blocks else None
        container_selector = describe_selector(parent_tag_obj, winner.class_signature)

        logger.info(
            "Product list detected: confidence=%.3f, products=%d, selector=%s",
            confidence, len(products), container_selector,
        )

        return DetectionResult(
            is_product_list=True,
            confidence_score=confidence,
            container_selector=container_selector,
            products=products,
        )

    # ------------------------------------------------------------------
    # SeleniumBase HTML retrieval helper
    # ------------------------------------------------------------------

    @staticmethod
    def _get_html_from_sb(sb, url: str) -> Optional[str]:
        """
        Try multiple SB API surfaces to retrieve the rendered page HTML.
        Compatible with both older and newer SeleniumBase CDP API versions.
        """
        # Navigate first if URL is provided and sb has an open() method
        if url:
            try:
                if hasattr(sb, "open"):
                    sb.open(url)
                elif hasattr(sb, "get"):
                    sb.get(url)
            except Exception as exc:
                logger.warning("_get_html_from_sb: navigation failed — %s", exc)

        # Try various extraction methods in order of preference
        for method_name in (
            "get_page_source",
            "get_current_page_source",
        ):
            if hasattr(sb, method_name):
                try:
                    return getattr(sb, method_name)()
                except Exception:
                    continue

        # Fallback: JS evaluation
        if hasattr(sb, "execute_script"):
            try:
                return sb.execute_script("return document.documentElement.outerHTML;")
            except Exception:
                pass

        return None
