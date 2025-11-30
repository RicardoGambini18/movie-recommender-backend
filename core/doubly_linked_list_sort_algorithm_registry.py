from typing import Callable
from core.constants import INFO
from core.results import SortResult
from core.data_structures import DoublyLinkedList, Node
from core.algorithm_metrics import AlgorithmMetricsManager
from core.data_structure_algorithm_registry import AlgorithmOption, DataStructureOption, DataStructureAlgorithmRegistry


class DoublyLinkedListSortAlgorithmRegistry(DataStructureAlgorithmRegistry):
    def __init__(self, data: list[dict] = [], value_getter: Callable[[dict], int] = lambda: 0):
        self._value_getter = value_getter
        self._data: DoublyLinkedList[dict] = DoublyLinkedList(data)

    def register(self):
        return DataStructureOption(
            key=INFO['DOUBLY_LINKED_LIST']['key'],
            name=INFO['DOUBLY_LINKED_LIST']['name'],
            description=INFO['DOUBLY_LINKED_LIST']['description'],
            algorithms=[
                AlgorithmOption(
                    key=INFO['DOUBLY_LINKED_LIST']['sort_algorithms']['MERGE_SORT']['key'],
                    name=INFO['DOUBLY_LINKED_LIST']['sort_algorithms']['MERGE_SORT']['name'],
                    description=INFO['DOUBLY_LINKED_LIST']['sort_algorithms']['MERGE_SORT']['description'],
                    time_complexity=INFO['DOUBLY_LINKED_LIST']['sort_algorithms']['MERGE_SORT']['time_complexity'],
                    space_complexity=INFO['DOUBLY_LINKED_LIST']['sort_algorithms']['MERGE_SORT']['space_complexity'],
                    time_complexity_level=INFO['DOUBLY_LINKED_LIST']['sort_algorithms']['MERGE_SORT']['time_complexity_level'],
                    space_complexity_level=INFO['DOUBLY_LINKED_LIST']['sort_algorithms']['MERGE_SORT']['space_complexity_level'],
                ),
            ]
        )

    def merge_sort(self):
        metrics_manager = AlgorithmMetricsManager()
        metrics_manager.start()

        sorted_list = self._data.copy()
        head: Node[dict] | None = sorted_list.get_head()

        metrics_manager.increment_operations(self._data.size() + 2)

        if head is None or head.get_next() is None:
            metrics_manager.end()
            return SortResult(
                data_structure=INFO['DOUBLY_LINKED_LIST']['name'],
                algorithm=INFO['DOUBLY_LINKED_LIST']['sort_algorithms']['MERGE_SORT']['name'],
                time_complexity=INFO['DOUBLY_LINKED_LIST']['sort_algorithms']['MERGE_SORT']['time_complexity'],
                time_complexity_level=INFO['DOUBLY_LINKED_LIST']['sort_algorithms']['MERGE_SORT']['time_complexity_level'],
                space_complexity=INFO['DOUBLY_LINKED_LIST']['sort_algorithms']['MERGE_SORT']['space_complexity'],
                space_complexity_level=INFO['DOUBLY_LINKED_LIST']['sort_algorithms']['MERGE_SORT']['space_complexity_level'],
                item_count=self._data.size(),
                sorted_data=sorted_list.to_list(),
                metrics=metrics_manager.get_metrics()
            )

        sorted_list.head = self._recursive_merge_sort(head, metrics_manager)

        current: Node[dict] | None = sorted_list.get_head()
        prev_node: Node[dict] | None = None

        metrics_manager.increment_operations(2)

        while current is not None:
            metrics_manager.increment_iterations()
            current.set_prev(prev_node)
            prev_node = current
            current = current.get_next()
            metrics_manager.increment_operations(4)

        sorted_list.tail = prev_node
        metrics_manager.increment_operations(2)

        metrics_manager.end()

        return SortResult(
            data_structure=INFO['DOUBLY_LINKED_LIST']['name'],
            algorithm=INFO['DOUBLY_LINKED_LIST']['sort_algorithms']['MERGE_SORT']['name'],
            time_complexity=INFO['DOUBLY_LINKED_LIST']['sort_algorithms']['MERGE_SORT']['time_complexity'],
            time_complexity_level=INFO['DOUBLY_LINKED_LIST']['sort_algorithms']['MERGE_SORT']['time_complexity_level'],
            space_complexity=INFO['DOUBLY_LINKED_LIST']['sort_algorithms']['MERGE_SORT']['space_complexity'],
            space_complexity_level=INFO['DOUBLY_LINKED_LIST']['sort_algorithms']['MERGE_SORT']['space_complexity_level'],
            item_count=self._data.size(),
            sorted_data=sorted_list.to_list(),
            metrics=metrics_manager.get_metrics()
        )

    def _recursive_merge_sort(self, head: Node[dict] | None, metrics_manager: AlgorithmMetricsManager) -> Node[dict] | None:
        metrics_manager.increment_iterations()
        metrics_manager.increment_operations(2)

        if head is None or head.get_next() is None:
            return head

        middle: Node[dict] = self._get_middle(head, metrics_manager)
        next_to_middle: Node[dict] | None = middle.get_next()
        middle.set_next(None)

        metrics_manager.increment_operations(2)

        left = self._recursive_merge_sort(head, metrics_manager)
        right = self._recursive_merge_sort(next_to_middle, metrics_manager)

        return self._merge(left, right, metrics_manager)

    def _merge(self, left: Node[dict] | None, right: Node[dict] | None, metrics_manager: AlgorithmMetricsManager) -> Node[dict] | None:
        dummy = Node(None)
        tail: Node[dict] = dummy
        metrics_manager.increment_operations(2)

        while left is not None and right is not None:
            metrics_manager.increment_iterations()

            val_left = self._value_getter(left.get_data())
            val_right = self._value_getter(right.get_data())
            metrics_manager.increment_operations(5)

            if val_left <= val_right:
                tail.set_next(left)
                left = left.get_next()
                metrics_manager.increment_operations(2)
            else:
                tail.set_next(right)
                right = right.get_next()
                metrics_manager.increment_operations(2)

            metrics_manager.increment_operations(1)

            if tail.get_next():
                tail = tail.get_next()
                metrics_manager.increment_operations(1)

        metrics_manager.increment_operations(3)

        if left is not None:
            tail.set_next(left)
            metrics_manager.increment_operations(1)
        elif right is not None:
            tail.set_next(right)
            metrics_manager.increment_operations(1)

        return dummy.get_next()

    def _get_middle(self, head: Node[dict] | None, metrics_manager: AlgorithmMetricsManager) -> Node[dict] | None:
        metrics_manager.increment_operations(1)

        if head is None:
            return head

        slow: Node[dict] = head
        fast: Node[dict] | None = head

        metrics_manager.increment_operations(2)

        while fast is not None and fast.get_next() is not None and fast.get_next().get_next() is not None:
            metrics_manager.increment_iterations()
            metrics_manager.increment_operations(4)

            if slow.get_next():
                slow = slow.get_next()
                metrics_manager.increment_operations(1)

            fast = fast.get_next().get_next()
            metrics_manager.increment_operations(1)

        metrics_manager.increment_operations(1)

        return slow
