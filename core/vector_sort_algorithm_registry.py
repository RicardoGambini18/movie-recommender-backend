from typing import Callable
from core.constants import INFO
from core.results import SortResult
from core.data_structures import Vector
from core.algorithm_metrics import AlgorithmMetricsManager
from core.data_structure_algorithm_registry import AlgorithmOption, DataStructureOption,  DataStructureAlgorithmRegistry


class VectorSortAlgorithmRegistry(DataStructureAlgorithmRegistry):
    def __init__(self, data: list[dict] = [], value_getter: Callable[[dict], int] = lambda: 0):
        self._value_getter = value_getter
        self._data: Vector[dict] = Vector(data)

    def register(self):
        return DataStructureOption(
            key=INFO['VECTOR']['key'],
            name=INFO['VECTOR']['name'],
            description=INFO['VECTOR']['description'],
            algorithms=[
                AlgorithmOption(
                    key=INFO['VECTOR']['sort_algorithms']['BUBBLE_SORT']['key'],
                    name=INFO['VECTOR']['sort_algorithms']['BUBBLE_SORT']['name'],
                    description=INFO['VECTOR']['sort_algorithms']['BUBBLE_SORT']['description'],
                    time_complexity=INFO['VECTOR']['sort_algorithms']['BUBBLE_SORT']['time_complexity'],
                    space_complexity=INFO['VECTOR']['sort_algorithms']['BUBBLE_SORT']['space_complexity'],
                    time_complexity_level=INFO['VECTOR']['sort_algorithms']['BUBBLE_SORT']['time_complexity_level'],
                    space_complexity_level=INFO['VECTOR']['sort_algorithms']['BUBBLE_SORT']['space_complexity_level'],
                ),
                AlgorithmOption(
                    key=INFO['VECTOR']['sort_algorithms']['SELECTION_SORT']['key'],
                    name=INFO['VECTOR']['sort_algorithms']['SELECTION_SORT']['name'],
                    description=INFO['VECTOR']['sort_algorithms']['SELECTION_SORT']['description'],
                    time_complexity=INFO['VECTOR']['sort_algorithms']['SELECTION_SORT']['time_complexity'],
                    space_complexity=INFO['VECTOR']['sort_algorithms']['SELECTION_SORT']['space_complexity'],
                    time_complexity_level=INFO['VECTOR']['sort_algorithms']['SELECTION_SORT']['time_complexity_level'],
                    space_complexity_level=INFO['VECTOR']['sort_algorithms']['SELECTION_SORT']['space_complexity_level'],
                ),
                AlgorithmOption(
                    key=INFO['VECTOR']['sort_algorithms']['INSERTION_SORT']['key'],
                    name=INFO['VECTOR']['sort_algorithms']['INSERTION_SORT']['name'],
                    description=INFO['VECTOR']['sort_algorithms']['INSERTION_SORT']['description'],
                    time_complexity=INFO['VECTOR']['sort_algorithms']['INSERTION_SORT']['time_complexity'],
                    space_complexity=INFO['VECTOR']['sort_algorithms']['INSERTION_SORT']['space_complexity'],
                    time_complexity_level=INFO['VECTOR']['sort_algorithms']['INSERTION_SORT']['time_complexity_level'],
                    space_complexity_level=INFO['VECTOR']['sort_algorithms']['INSERTION_SORT']['space_complexity_level'],
                ),
                AlgorithmOption(
                    key=INFO['VECTOR']['sort_algorithms']['MERGE_SORT']['key'],
                    name=INFO['VECTOR']['sort_algorithms']['MERGE_SORT']['name'],
                    description=INFO['VECTOR']['sort_algorithms']['MERGE_SORT']['description'],
                    time_complexity=INFO['VECTOR']['sort_algorithms']['MERGE_SORT']['time_complexity'],
                    space_complexity=INFO['VECTOR']['sort_algorithms']['MERGE_SORT']['space_complexity'],
                    time_complexity_level=INFO['VECTOR']['sort_algorithms']['MERGE_SORT']['time_complexity_level'],
                    space_complexity_level=INFO['VECTOR']['sort_algorithms']['MERGE_SORT']['space_complexity_level'],
                ),
                AlgorithmOption(
                    key=INFO['VECTOR']['sort_algorithms']['QUICK_SORT']['key'],
                    name=INFO['VECTOR']['sort_algorithms']['QUICK_SORT']['name'],
                    description=INFO['VECTOR']['sort_algorithms']['QUICK_SORT']['description'],
                    time_complexity=INFO['VECTOR']['sort_algorithms']['QUICK_SORT']['time_complexity'],
                    space_complexity=INFO['VECTOR']['sort_algorithms']['QUICK_SORT']['space_complexity'],
                    time_complexity_level=INFO['VECTOR']['sort_algorithms']['QUICK_SORT']['time_complexity_level'],
                    space_complexity_level=INFO['VECTOR']['sort_algorithms']['QUICK_SORT']['space_complexity_level'],
                ),
            ]
        )

    def bubble_sort(self):
        metrics_manager = AlgorithmMetricsManager()
        metrics_manager.start()

        sorted_data = self._data.copy()
        n = sorted_data.size()
        metrics_manager.increment_operations(n + 1)

        for i in range(n):
            is_sorted = True
            metrics_manager.increment_operations(2)

            for j in range(n - i - 1):
                metrics_manager.increment_iterations()
                a = sorted_data.get_item(j)
                b = sorted_data.get_item(j + 1)
                a_value = self._value_getter(a)
                b_value = self._value_getter(b)

                metrics_manager.increment_operations(6)

                if a_value > b_value:
                    sorted_data.set_item(j, b)
                    sorted_data.set_item(j + 1, a)
                    is_sorted = False
                    metrics_manager.increment_operations(3)

            metrics_manager.increment_operations(1)

            if is_sorted:
                break

        metrics_manager.end()

        return SortResult(
            data_structure=INFO['VECTOR']['name'],
            algorithm=INFO['VECTOR']['sort_algorithms']['BUBBLE_SORT']['name'],
            time_complexity=INFO['VECTOR']['sort_algorithms']['BUBBLE_SORT']['time_complexity'],
            time_complexity_level=INFO['VECTOR']['sort_algorithms']['BUBBLE_SORT']['time_complexity_level'],
            item_count=self._data.size(),
            sorted_data=sorted_data.to_list(),
            metrics=metrics_manager.get_metrics()
        )

    def selection_sort(self):
        metrics_manager = AlgorithmMetricsManager()
        metrics_manager.start()

        sorted_data = self._data.copy()
        n = sorted_data.size()
        metrics_manager.increment_operations(n + 1)

        for i in range(n):
            min_index = i
            min_value = self._value_getter(sorted_data.get_item(i))
            metrics_manager.increment_operations(4)

            for j in range(i + 1, n):
                metrics_manager.increment_iterations()
                value = self._value_getter(sorted_data.get_item(j))
                metrics_manager.increment_operations(4)

                if value < min_value:
                    min_index = j
                    min_value = value
                    metrics_manager.increment_operations(2)

            temp = sorted_data.get_item(i)
            sorted_data.set_item(i, sorted_data.get_item(min_index))
            sorted_data.set_item(min_index, temp)
            metrics_manager.increment_operations(4)

        metrics_manager.end()

        return SortResult(
            data_structure=INFO['VECTOR']['name'],
            algorithm=INFO['VECTOR']['sort_algorithms']['SELECTION_SORT']['name'],
            time_complexity=INFO['VECTOR']['sort_algorithms']['SELECTION_SORT']['time_complexity'],
            time_complexity_level=INFO['VECTOR']['sort_algorithms']['SELECTION_SORT']['time_complexity_level'],
            item_count=self._data.size(),
            sorted_data=sorted_data.to_list(),
            metrics=metrics_manager.get_metrics()
        )

    def insertion_sort(self):
        metrics_manager = AlgorithmMetricsManager()
        metrics_manager.start()

        sorted_data = self._data.copy()
        n = sorted_data.size()
        metrics_manager.increment_operations(n + 1)

        for i in range(1, n):
            item = sorted_data.get_item(i)
            item_value = self._value_getter(item)

            j = i - 1
            previous_item = sorted_data.get_item(j)
            previous_item_value = self._value_getter(previous_item)

            metrics_manager.increment_operations(6)

            while j >= 0 and previous_item_value > item_value:
                metrics_manager.increment_iterations()
                sorted_data.set_item(j + 1, previous_item)

                j -= 1
                previous_item = sorted_data.get_item(j)
                previous_item_value = self._value_getter(previous_item)

                metrics_manager.increment_operations(6)

            sorted_data.set_item(j + 1, item)
            metrics_manager.increment_operations(3)

        metrics_manager.end()

        return SortResult(
            data_structure=INFO['VECTOR']['name'],
            algorithm=INFO['VECTOR']['sort_algorithms']['INSERTION_SORT']['name'],
            time_complexity=INFO['VECTOR']['sort_algorithms']['INSERTION_SORT']['time_complexity'],
            time_complexity_level=INFO['VECTOR']['sort_algorithms']['INSERTION_SORT']['time_complexity_level'],
            item_count=self._data.size(),
            sorted_data=sorted_data.to_list(),
            metrics=metrics_manager.get_metrics()
        )

    def merge_sort(self):
        metrics_manager = AlgorithmMetricsManager()
        metrics_manager.start()

        metrics_manager.increment_operations(self._data.size())
        sorted_data = self._recursive_merge_sort(
            self._data.copy(), metrics_manager)

        metrics_manager.end()

        return SortResult(
            data_structure=INFO['VECTOR']['name'],
            algorithm=INFO['VECTOR']['sort_algorithms']['MERGE_SORT']['name'],
            time_complexity=INFO['VECTOR']['sort_algorithms']['MERGE_SORT']['time_complexity'],
            time_complexity_level=INFO['VECTOR']['sort_algorithms']['MERGE_SORT']['time_complexity_level'],
            item_count=self._data.size(),
            sorted_data=sorted_data.to_list(),
            metrics=metrics_manager.get_metrics()
        )

    def _recursive_merge_sort(self, data: Vector[dict], metrics_manager: AlgorithmMetricsManager) -> Vector[dict]:
        n = data.size()
        metrics_manager.increment_operations(2)

        if n <= 1:
            return data

        mid = n // 2
        left = data.get_slice(0, mid)
        right = data.get_slice(mid, n)
        metrics_manager.increment_operations(n + 1)

        left_sorted = self._recursive_merge_sort(left, metrics_manager)
        right_sorted = self._recursive_merge_sort(right, metrics_manager)

        return self._merge(left_sorted, right_sorted, metrics_manager)

    def _merge(self, left: Vector[dict], right: Vector[dict], metrics_manager: AlgorithmMetricsManager) -> Vector[dict]:
        i = j = 0
        merged_data = Vector[dict]([])
        metrics_manager.increment_operations(2)

        while i < left.size() and j < right.size():
            metrics_manager.increment_iterations()
            a = left.get_item(i)
            b = right.get_item(j)
            a_value = self._value_getter(a)
            b_value = self._value_getter(b)

            metrics_manager.increment_operations(7)

            if a_value <= b_value:
                merged_data.append(a)
                i += 1
                metrics_manager.increment_operations(2)
            else:
                merged_data.append(b)
                j += 1
                metrics_manager.increment_operations(2)

        metrics_manager.increment_operations(3)

        if i < left.size():
            merged_data.extend(left.get_slice(i, left.size()))
            metrics_manager.increment_operations((left.size() - i) * 2)

        metrics_manager.increment_operations(1)

        if j < right.size():
            merged_data.extend(right.get_slice(j, right.size()))
            metrics_manager.increment_operations((right.size() - j) * 2)

        return merged_data

    def quick_sort(self):
        metrics_manager = AlgorithmMetricsManager()
        metrics_manager.start()

        metrics_manager.increment_operations(self._data.size())
        sorted_data = self._recursive_quick_sort(
            self._data.copy(), metrics_manager)

        metrics_manager.end()

        return SortResult(
            data_structure=INFO['VECTOR']['name'],
            algorithm=INFO['VECTOR']['sort_algorithms']['QUICK_SORT']['name'],
            time_complexity=INFO['VECTOR']['sort_algorithms']['QUICK_SORT']['time_complexity'],
            time_complexity_level=INFO['VECTOR']['sort_algorithms']['QUICK_SORT']['time_complexity_level'],
            item_count=self._data.size(),
            sorted_data=sorted_data.to_list(),
            metrics=metrics_manager.get_metrics()
        )

    def _recursive_quick_sort(self, data: Vector[dict], metrics_manager: AlgorithmMetricsManager) -> Vector[dict]:
        metrics_manager.increment_operations(1)

        if data.size() <= 1:
            return data

        pivot = data.get_item(data.size() // 2)
        pivot_value = self._value_getter(pivot)

        left = Vector[dict]([])
        middle = Vector[dict]([])
        right = Vector[dict]([])

        metrics_manager.increment_operations(6)

        for i in range(data.size()):
            metrics_manager.increment_iterations()
            x = data.get_item(i)
            x_value = self._value_getter(x)
            metrics_manager.increment_operations(4)

            if x_value < pivot_value:
                left.append(x)
                metrics_manager.increment_operations(1)
            elif x_value == pivot_value:
                middle.append(x)
                metrics_manager.increment_operations(1)
            else:
                right.append(x)
                metrics_manager.increment_operations(1)

        left_sorted = self._recursive_quick_sort(left, metrics_manager)
        right_sorted = self._recursive_quick_sort(right, metrics_manager)

        result = Vector[dict]([])
        result.extend(left_sorted)
        result.extend(middle)
        result.extend(right_sorted)
        metrics_manager.increment_operations(
            1 + left_sorted.size() + middle.size() + right_sorted.size())

        return result
