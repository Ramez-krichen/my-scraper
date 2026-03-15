"""Temporary debug script for cluster analysis."""
import sys
sys.path.insert(0, '.')
from bs4 import BeautifulSoup
from extractors.product_list import HeuristicExtractor, PlatformHintAdapter
from product_detection.scorer import HeuristicScorer
from product_detection.models import ScoringConfig
from product_detection.tests.test_detector import _woocommerce_html, _blog_post_list_html

config = ScoringConfig()
extractor = HeuristicExtractor(config)
scorer = HeuristicScorer(config)
adapter = PlatformHintAdapter(config)

# --- WooCommerce ---
print("\n=== WooCommerce ===")
html = _woocommerce_html(n_products=9)
soup = BeautifulSoup(html, 'lxml')
working_soup = adapter.narrow(soup, '')
clusters = extractor.find_candidate_clusters(working_soup)
print(f"Clusters found: {len(clusters)}")
for blocks, parent, key in clusters[:10]:
    cs = scorer.score_cluster(blocks, parent, key)
    print(f"  key={key!r}, count={len(blocks)}, "
          f"avg_score={cs.avg_block_score:.2f}, composite={cs.composite_score:.3f}, "
          f"url_consistency={cs.url_consistency:.2f}")

# --- Blog ---
print("\n=== Blog (false positive) ===")
html2 = _blog_post_list_html(n_posts=7)
soup2 = BeautifulSoup(html2, 'lxml')
working_soup2 = adapter.narrow(soup2, '')
clusters2 = extractor.find_candidate_clusters(working_soup2)
print(f"Clusters found: {len(clusters2)}")
for blocks, parent, key in clusters2[:10]:
    cs = scorer.score_cluster(blocks, parent, key)
    print(f"  key={key!r}, count={len(blocks)}, "
          f"avg_score={cs.avg_block_score:.2f}, composite={cs.composite_score:.3f}, "
          f"has_img={any(b.find('img') for b in blocks)}")
