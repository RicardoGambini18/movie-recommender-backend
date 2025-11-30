from typing import Callable
from core.constants import INFO
from core.results import SearchResult
from core.data_structures import DoublyLinkedList
from core.algorithm_metrics import AlgorithmMetricsManager
from core.data_structure_algorithm_registry import DataStructureOption, DataStructureAlgorithmRegistry, SearchAlgorithmOption


class DoublyLinkedListSearchAlgorithmRegistry(DataStructureAlgorithmRegistry):
    def __init__(self, data: list[dict] = [], value_getter: Callable[[dict], int] = lambda: 0):
        self._value_getter = value_getter
        self._data: DoublyLinkedList[dict] = DoublyLinkedList(data)

    def register(self):
        return DataStructureOption(
            key=INFO['DOUBLY_LINKED_LIST']['key'],
            name=INFO['DOUBLY_LINKED_LIST']['name'],
            description=INFO['DOUBLY_LINKED_LIST']['description'],
            algorithms=[
                SearchAlgorithmOption(
                    key=INFO['DOUBLY_LINKED_LIST']['search_algorithms']['LINEAR_SEARCH']['key'],
                    name=INFO['DOUBLY_LINKED_LIST']['search_algorithms']['LINEAR_SEARCH']['name'],
                    needs_sort=INFO['DOUBLY_LINKED_LIST']['search_algorithms']['LINEAR_SEARCH']['needs_sort'],
                    description=INFO['DOUBLY_LINKED_LIST']['search_algorithms']['LINEAR_SEARCH']['description'],
                    time_complexity=INFO['DOUBLY_LINKED_LIST']['search_algorithms']['LINEAR_SEARCH']['time_complexity'],
                    space_complexity=INFO['DOUBLY_LINKED_LIST']['search_algorithms']['LINEAR_SEARCH']['space_complexity'],
                    time_complexity_level=INFO['DOUBLY_LINKED_LIST'][
                        'search_algorithms']['LINEAR_SEARCH']['time_complexity_level'],
                    space_complexity_level=INFO['DOUBLY_LINKED_LIST'][
                        'search_algorithms']['LINEAR_SEARCH']['space_complexity_level'],
                ),
            ]
        )

    def linear_search(self, value: int):
        metrics_manager = AlgorithmMetricsManager()
        metrics_manager.start()

        current = self._data.get_head()
        item_found = None

        metrics_manager.increment_operations(2)

        while current is not None:
            metrics_manager.increment_iterations()

            node_data = current.get_data()
            node_value = self._value_getter(node_data)
            metrics_manager.increment_operations(3)

            if node_value == value:
                item_found = node_data
                metrics_manager.increment_operations(1)
                break

            current = current.get_next()
            metrics_manager.increment_operations(1)

        metrics_manager.increment_operations(1)

        metrics_manager.end()

        return SearchResult(
            data_structure=INFO['DOUBLY_LINKED_LIST']['name'],
            algorithm=INFO['DOUBLY_LINKED_LIST']['search_algorithms']['LINEAR_SEARCH']['name'],
            needs_sort=INFO['DOUBLY_LINKED_LIST']['search_algorithms']['LINEAR_SEARCH']['needs_sort'],
            time_complexity=INFO['DOUBLY_LINKED_LIST']['search_algorithms']['LINEAR_SEARCH']['time_complexity'],
            time_complexity_level=INFO['DOUBLY_LINKED_LIST']['search_algorithms']['LINEAR_SEARCH']['time_complexity_level'],
            space_complexity=INFO['DOUBLY_LINKED_LIST']['search_algorithms']['LINEAR_SEARCH']['space_complexity'],
            space_complexity_level=INFO['DOUBLY_LINKED_LIST']['search_algorithms']['LINEAR_SEARCH']['space_complexity_level'],
            item_count=self._data.size(),
            item_found=item_found,
            metrics=metrics_manager.get_metrics()
        )
