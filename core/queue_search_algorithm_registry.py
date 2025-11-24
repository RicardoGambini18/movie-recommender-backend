from typing import Callable
from core.constants import INFO
from core.results import SearchResult
from core.data_structures import Queue
from core.algorithm_metrics import AlgorithmMetricsManager
from core.data_structure_algorithm_registry import DataStructureOption, DataStructureAlgorithmRegistry, SearchAlgorithmOption


class QueueSearchAlgorithmRegistry(DataStructureAlgorithmRegistry):
    def __init__(self, data: list[dict] = [], value_getter: Callable[[dict], int] = lambda: 0):
        self._value_getter = value_getter
        self._data: Queue[dict] = Queue(data)

    def register(self):
        return DataStructureOption(
            key=INFO['QUEUE']['key'],
            name=INFO['QUEUE']['name'],
            description=INFO['QUEUE']['description'],
            algorithms=[
                SearchAlgorithmOption(
                    key=INFO['QUEUE']['search_algorithms']['LINEAR_SEARCH']['key'],
                    name=INFO['QUEUE']['search_algorithms']['LINEAR_SEARCH']['name'],
                    needs_sort=INFO['QUEUE']['search_algorithms']['LINEAR_SEARCH']['needs_sort'],
                    description=INFO['QUEUE']['search_algorithms']['LINEAR_SEARCH']['description'],
                    space_complexity=INFO['QUEUE']['search_algorithms']['LINEAR_SEARCH']['space_complexity'],
                    best_time_complexity=INFO['QUEUE']['search_algorithms']['LINEAR_SEARCH']['best_time_complexity'],
                    worst_time_complexity=INFO['QUEUE']['search_algorithms']['LINEAR_SEARCH']['worst_time_complexity'],
                    average_time_complexity=INFO['QUEUE']['search_algorithms']['LINEAR_SEARCH']['average_time_complexity'],
                ),
            ]
        )

    def linear_search(self, value: int):
        metrics_manager = AlgorithmMetricsManager()
        metrics_manager.start()

        item_found = None
        item_count = self._data.size()
        metrics_manager.increment_operations(2)

        for _ in range(item_count):
            metrics_manager.increment_iterations()
            item = self._data.dequeue()
            metrics_manager.increment_operations(3)

            if item_found is None:
                item_value = self._value_getter(item)
                metrics_manager.increment_operations(2)

                if item_value == value:
                    item_found = item
                    metrics_manager.increment_operations(1)

            self._data.enqueue(item)
            metrics_manager.increment_operations(1)

        metrics_manager.end()

        return SearchResult(
            data_structure=INFO['QUEUE']['name'],
            algorithm=INFO['QUEUE']['search_algorithms']['LINEAR_SEARCH']['name'],
            needs_sort=INFO['QUEUE']['search_algorithms']['LINEAR_SEARCH']['needs_sort'],
            item_count=item_count,
            item_found=item_found,
            metrics=metrics_manager.get_metrics()
        )
