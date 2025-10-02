from dataclasses import dataclass
from core.algorithm_metrics import AlgorithmMetrics


@dataclass
class SearchResult:
    data_structure: str
    algorithm: str
    item_count: int
    item_found: dict | None
    metrics: AlgorithmMetrics
