from dataclasses import dataclass
from core.algorithm_metrics import AlgorithmMetrics


@dataclass
class AlgorithmResult:
    data_structure: str
    algorithm: str
    item_count: int
    metrics: AlgorithmMetrics


@dataclass
class SortResult(AlgorithmResult):
    sorted_data: list[dict]


@dataclass
class SearchResult(AlgorithmResult):
    needs_sort: bool
    item_found: dict | None
