from typing import Callable
from core.constants import INFO
from core.results import SearchResult
from core.data_structures import Stack
from core.algorithm_metrics import AlgorithmMetricsManager
from core.data_structure_algorithm_registry import DataStructureOption, DataStructureAlgorithmRegistry, SearchAlgorithmOption


class StackSearchAlgorithmRegistry(DataStructureAlgorithmRegistry):
    def __init__(self, data: list[dict] = [], value_getter: Callable[[dict], int] = lambda: 0):
        self._value_getter = value_getter
        self._data: Stack[dict] = Stack(data)

    def register(self):
        return DataStructureOption(
            key=INFO['STACK']['key'],
            name=INFO['STACK']['name'],
            description=INFO['STACK']['description'],
            algorithms=[
                SearchAlgorithmOption(
                    key=INFO['STACK']['search_algorithms']['LINEAR_SEARCH']['key'],
                    name=INFO['STACK']['search_algorithms']['LINEAR_SEARCH']['name'],
                    needs_sort=INFO['STACK']['search_algorithms']['LINEAR_SEARCH']['needs_sort'],
                    description=INFO['STACK']['search_algorithms']['LINEAR_SEARCH']['description'],
                    space_complexity=INFO['STACK']['search_algorithms']['LINEAR_SEARCH']['space_complexity'],
                    best_time_complexity=INFO['STACK']['search_algorithms']['LINEAR_SEARCH']['best_time_complexity'],
                    worst_time_complexity=INFO['STACK']['search_algorithms']['LINEAR_SEARCH']['worst_time_complexity'],
                    average_time_complexity=INFO['STACK']['search_algorithms']['LINEAR_SEARCH']['average_time_complexity'],
                ),
            ]
        )

    def linear_search(self, value: int):
        metrics_manager = AlgorithmMetricsManager()
        metrics_manager.start()

        data_copy = self._data.copy()
        item_count = data_copy.size()

        for _ in range(item_count):
            item = data_copy.pop()
            item_value = self._value_getter(item)
            metrics_manager.increment_comparisons()

            if item_value == value:
                metrics_manager.end()

                return SearchResult(
                    data_structure=INFO['STACK']['name'],
                    algorithm=INFO['STACK']['search_algorithms']['LINEAR_SEARCH']['name'],
                    needs_sort=INFO['STACK']['search_algorithms']['LINEAR_SEARCH']['needs_sort'],
                    item_count=item_count,
                    item_found=item,
                    metrics=metrics_manager.get_metrics()
                )

        metrics_manager.end()

        return SearchResult(
            data_structure=INFO['STACK']['name'],
            algorithm=INFO['STACK']['search_algorithms']['LINEAR_SEARCH']['name'],
            needs_sort=INFO['STACK']['search_algorithms']['LINEAR_SEARCH']['needs_sort'],
            item_count=item_count,
            item_found=None,
            metrics=metrics_manager.get_metrics()
        )
