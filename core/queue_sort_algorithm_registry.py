from typing import Callable
from core.constants import INFO
from core.results import SortResult
from core.data_structures import Queue
from core.algorithm_metrics import AlgorithmMetricsManager
from core.data_structure_algorithm_registry import AlgorithmOption, DataStructureOption, DataStructureAlgorithmRegistry


class QueueSortAlgorithmRegistry(DataStructureAlgorithmRegistry):
    def __init__(self, data: list[dict] = [], value_getter: Callable[[dict], int] = lambda: 0):
        self._value_getter = value_getter
        self._data: Queue[dict] = Queue(data)

    def register(self):
        return DataStructureOption(
            key=INFO['QUEUE']['key'],
            name=INFO['QUEUE']['name'],
            description=INFO['QUEUE']['description'],
            algorithms=[
                AlgorithmOption(
                    key=INFO['QUEUE']['sort_algorithms']['SELECTION_SORT']['key'],
                    name=INFO['QUEUE']['sort_algorithms']['SELECTION_SORT']['name'],
                    description=INFO['QUEUE']['sort_algorithms']['SELECTION_SORT']['description'],
                    space_complexity=INFO['QUEUE']['sort_algorithms']['SELECTION_SORT']['space_complexity'],
                    best_time_complexity=INFO['QUEUE']['sort_algorithms']['SELECTION_SORT']['best_time_complexity'],
                    worst_time_complexity=INFO['QUEUE']['sort_algorithms']['SELECTION_SORT']['worst_time_complexity'],
                    average_time_complexity=INFO['QUEUE']['sort_algorithms']['SELECTION_SORT']['average_time_complexity'],
                ),
                AlgorithmOption(
                    key=INFO['QUEUE']['sort_algorithms']['MERGE_SORT']['key'],
                    name=INFO['QUEUE']['sort_algorithms']['MERGE_SORT']['name'],
                    description=INFO['QUEUE']['sort_algorithms']['MERGE_SORT']['description'],
                    space_complexity=INFO['QUEUE']['sort_algorithms']['MERGE_SORT']['space_complexity'],
                    best_time_complexity=INFO['QUEUE']['sort_algorithms']['MERGE_SORT']['best_time_complexity'],
                    worst_time_complexity=INFO['QUEUE']['sort_algorithms']['MERGE_SORT']['worst_time_complexity'],
                    average_time_complexity=INFO['QUEUE']['sort_algorithms']['MERGE_SORT']['average_time_complexity'],
                ),
            ]
        )

    def selection_sort(self):
        metrics_manager = AlgorithmMetricsManager()
        metrics_manager.start()

        sorted_data = Queue[dict]()
        aux_queue = self._data.copy()
        item_count = self._data.size()

        for _ in range(item_count):
            min_item = None
            min_value = None
            aux_queue_size = aux_queue.size()

            for __ in range(aux_queue_size):
                item = aux_queue.dequeue()
                item_value = self._value_getter(item)
                metrics_manager.increment_comparisons()

                if min_value is None:
                    min_item = item
                    min_value = item_value
                else:
                    if item_value < min_value:
                        if min_item is not None:
                            aux_queue.enqueue(min_item)
                        min_item = item
                        min_value = item_value
                    else:
                        aux_queue.enqueue(item)

            if min_item is not None:
                sorted_data.enqueue(min_item)

        metrics_manager.end()

        return SortResult(
            data_structure=INFO['QUEUE']['name'],
            algorithm=INFO['QUEUE']['sort_algorithms']['SELECTION_SORT']['name'],
            item_count=item_count,
            sorted_data=sorted_data.to_list(),
            metrics=metrics_manager.get_metrics()
        )

    def merge_sort(self):
        metrics_manager = AlgorithmMetricsManager()
        metrics_manager.start()

        sorted_data = self._recursive_merge_sort(
            self._data.copy(), metrics_manager)

        metrics_manager.end()

        return SortResult(
            data_structure=INFO['QUEUE']['name'],
            algorithm=INFO['QUEUE']['sort_algorithms']['MERGE_SORT']['name'],
            item_count=self._data.size(),
            sorted_data=sorted_data.to_list(),
            metrics=metrics_manager.get_metrics()
        )

    def _recursive_merge_sort(self, queue: Queue[dict], metrics_manager: AlgorithmMetricsManager) -> Queue[dict]:
        n = queue.size()

        if n <= 1:
            return queue

        left = Queue[dict]()
        right = Queue[dict]()

        mid = n // 2
        for _ in range(mid):
            left.enqueue(queue.dequeue())

        while not queue.is_empty():
            right.enqueue(queue.dequeue())

        left_sorted = self._recursive_merge_sort(left, metrics_manager)
        right_sorted = self._recursive_merge_sort(right, metrics_manager)

        return self._merge(left_sorted, right_sorted, metrics_manager)

    def _merge(self, left: Queue[dict], right: Queue[dict], metrics_manager: AlgorithmMetricsManager) -> Queue[dict]:
        merged_queue = Queue[dict]()

        while not left.is_empty() and not right.is_empty():
            a = left.peek()
            b = right.peek()
            a_value = self._value_getter(a)
            b_value = self._value_getter(b)

            metrics_manager.increment_comparisons()

            if a_value <= b_value:
                merged_queue.enqueue(left.dequeue())
            else:
                merged_queue.enqueue(right.dequeue())

        while not left.is_empty():
            merged_queue.enqueue(left.dequeue())

        while not right.is_empty():
            merged_queue.enqueue(right.dequeue())

        return merged_queue
