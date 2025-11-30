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
                    time_complexity=INFO['STACK']['search_algorithms']['LINEAR_SEARCH']['time_complexity'],
                    space_complexity=INFO['STACK']['search_algorithms']['LINEAR_SEARCH']['space_complexity'],
                    time_complexity_level=INFO['STACK']['search_algorithms']['LINEAR_SEARCH']['time_complexity_level'],
                    space_complexity_level=INFO['STACK']['search_algorithms']['LINEAR_SEARCH']['space_complexity_level'],
                ),
            ]
        )

    def linear_search(self, value: int):
        metrics_manager = AlgorithmMetricsManager()
        metrics_manager.start()

        item_found = None
        aux_stack = Stack[dict]()
        metrics_manager.increment_operations(2)

        while not self._data.is_empty():
            metrics_manager.increment_iterations()
            item = self._data.pop()
            aux_stack.push(item)
            metrics_manager.increment_operations(3)

            if item_found is None:
                item_value = self._value_getter(item)
                metrics_manager.increment_operations(2)

                if item_value == value:
                    item_found = item
                    metrics_manager.increment_operations(1)
                    break

        metrics_manager.increment_operations(1)

        while not aux_stack.is_empty():
            metrics_manager.increment_iterations()
            item = aux_stack.pop()
            self._data.push(item)
            metrics_manager.increment_operations(3)

        metrics_manager.increment_operations(1)

        metrics_manager.end()

        return SearchResult(
            data_structure=INFO['STACK']['name'],
            algorithm=INFO['STACK']['search_algorithms']['LINEAR_SEARCH']['name'],
            needs_sort=INFO['STACK']['search_algorithms']['LINEAR_SEARCH']['needs_sort'],
            time_complexity=INFO['STACK']['search_algorithms']['LINEAR_SEARCH']['time_complexity'],
            time_complexity_level=INFO['STACK']['search_algorithms']['LINEAR_SEARCH']['time_complexity_level'],
            space_complexity=INFO['STACK']['search_algorithms']['LINEAR_SEARCH']['space_complexity'],
            space_complexity_level=INFO['STACK']['search_algorithms']['LINEAR_SEARCH']['space_complexity_level'],
            item_found=item_found,
            item_count=self._data.size(),
            metrics=metrics_manager.get_metrics()
        )
