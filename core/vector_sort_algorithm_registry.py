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
                    space_complexity=INFO['VECTOR']['sort_algorithms']['BUBBLE_SORT']['space_complexity'],
                    best_time_complexity=INFO['VECTOR']['sort_algorithms']['BUBBLE_SORT']['best_time_complexity'],
                    worst_time_complexity=INFO['VECTOR'][
                        'sort_algorithms']['BUBBLE_SORT']['worst_time_complexity'],
                    average_time_complexity=INFO['VECTOR'][
                        'sort_algorithms']['BUBBLE_SORT']['average_time_complexity'],
                ),
                AlgorithmOption(
                    key=INFO['VECTOR']['sort_algorithms']['SELECTION_SORT']['key'],
                    name=INFO['VECTOR']['sort_algorithms']['SELECTION_SORT']['name'],
                    description=INFO['VECTOR']['sort_algorithms']['SELECTION_SORT']['description'],
                    space_complexity=INFO['VECTOR']['sort_algorithms']['SELECTION_SORT']['space_complexity'],
                    best_time_complexity=INFO['VECTOR'][
                        'sort_algorithms']['SELECTION_SORT']['best_time_complexity'],
                    worst_time_complexity=INFO['VECTOR'][
                        'sort_algorithms']['SELECTION_SORT']['worst_time_complexity'],
                    average_time_complexity=INFO['VECTOR'][
                        'sort_algorithms']['SELECTION_SORT']['average_time_complexity'],
                ),
                AlgorithmOption(
                    key=INFO['VECTOR']['sort_algorithms']['INSERTION_SORT']['key'],
                    name=INFO['VECTOR']['sort_algorithms']['INSERTION_SORT']['name'],
                    description=INFO['VECTOR']['sort_algorithms']['INSERTION_SORT']['description'],
                    space_complexity=INFO['VECTOR']['sort_algorithms']['INSERTION_SORT']['space_complexity'],
                    best_time_complexity=INFO['VECTOR'][
                        'sort_algorithms']['INSERTION_SORT']['best_time_complexity'],
                    worst_time_complexity=INFO['VECTOR'][
                        'sort_algorithms']['INSERTION_SORT']['worst_time_complexity'],
                    average_time_complexity=INFO['VECTOR'][
                        'sort_algorithms']['INSERTION_SORT']['average_time_complexity'],
                ),
                AlgorithmOption(
                    key=INFO['VECTOR']['sort_algorithms']['MERGE_SORT']['key'],
                    name=INFO['VECTOR']['sort_algorithms']['MERGE_SORT']['name'],
                    description=INFO['VECTOR']['sort_algorithms']['MERGE_SORT']['description'],
                    space_complexity=INFO['VECTOR']['sort_algorithms']['MERGE_SORT']['space_complexity'],
                    best_time_complexity=INFO['VECTOR']['sort_algorithms']['MERGE_SORT']['best_time_complexity'],
                    worst_time_complexity=INFO['VECTOR'][
                        'sort_algorithms']['MERGE_SORT']['worst_time_complexity'],
                    average_time_complexity=INFO['VECTOR'][
                        'sort_algorithms']['MERGE_SORT']['average_time_complexity'],
                ),
                AlgorithmOption(
                    key=INFO['VECTOR']['sort_algorithms']['QUICK_SORT']['key'],
                    name=INFO['VECTOR']['sort_algorithms']['QUICK_SORT']['name'],
                    description=INFO['VECTOR']['sort_algorithms']['QUICK_SORT']['description'],
                    space_complexity=INFO['VECTOR']['sort_algorithms']['QUICK_SORT']['space_complexity'],
                    best_time_complexity=INFO['VECTOR']['sort_algorithms']['QUICK_SORT']['best_time_complexity'],
                    worst_time_complexity=INFO['VECTOR'][
                        'sort_algorithms']['QUICK_SORT']['worst_time_complexity'],
                    average_time_complexity=INFO['VECTOR'][
                        'sort_algorithms']['QUICK_SORT']['average_time_complexity'],
                ),
            ]
        )

    def bubble_sort(self):
        metrics_manager = AlgorithmMetricsManager()
        metrics_manager.start()

        sorted_data = self._data.copy()
        n = sorted_data.size()

        for i in range(n):
            is_sorted = True

            for j in range(n - i - 1):
                a = sorted_data.get_item(j)
                b = sorted_data.get_item(j + 1)
                a_value = self._value_getter(a)
                b_value = self._value_getter(b)

                metrics_manager.increment_comparisons()

                if a_value > b_value:
                    sorted_data.set_item(j, b)
                    sorted_data.set_item(j + 1, a)
                    is_sorted = False

            if is_sorted:
                break

        metrics_manager.end()

        return SortResult(
            data_structure=INFO['VECTOR']['name'],
            algorithm=INFO['VECTOR']['sort_algorithms']['BUBBLE_SORT']['name'],
            item_count=self._data.size(),
            sorted_data=sorted_data.to_list(),
            metrics=metrics_manager.get_metrics()
        )

    def selection_sort(self):
        metrics_manager = AlgorithmMetricsManager()
        metrics_manager.start()

        sorted_data = self._data.copy()
        n = sorted_data.size()

        for i in range(n):
            min_index = i
            min_value = self._value_getter(sorted_data.get_item(i))

            for j in range(i + 1, n):
                value = self._value_getter(sorted_data.get_item(j))

                if value < min_value:
                    min_index = j
                    min_value = value

                metrics_manager.increment_comparisons()

            temp = sorted_data.get_item(i)
            sorted_data.set_item(i, sorted_data.get_item(min_index))
            sorted_data.set_item(min_index, temp)

        metrics_manager.end()

        return SortResult(
            data_structure=INFO['VECTOR']['name'],
            algorithm=INFO['VECTOR']['sort_algorithms']['SELECTION_SORT']['name'],
            item_count=self._data.size(),
            sorted_data=sorted_data.to_list(),
            metrics=metrics_manager.get_metrics()
        )

    def insertion_sort(self):
        metrics_manager = AlgorithmMetricsManager()
        metrics_manager.start()

        sorted_data = self._data.copy()
        n = sorted_data.size()

        for i in range(1, n):
            item = sorted_data.get_item(i)
            item_value = self._value_getter(item)

            j = i - 1
            previous_item = sorted_data.get_item(j)
            previous_item_value = self._value_getter(previous_item)

            while j >= 0 and previous_item_value > item_value:
                metrics_manager.increment_comparisons()
                sorted_data.set_item(j + 1, previous_item)

                j -= 1
                previous_item = sorted_data.get_item(j)
                previous_item_value = self._value_getter(previous_item)

            metrics_manager.increment_comparisons()
            sorted_data.set_item(j + 1, item)

        metrics_manager.end()

        return SortResult(
            data_structure=INFO['VECTOR']['name'],
            algorithm=INFO['VECTOR']['sort_algorithms']['INSERTION_SORT']['name'],
            item_count=self._data.size(),
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
            data_structure=INFO['VECTOR']['name'],
            algorithm=INFO['VECTOR']['sort_algorithms']['MERGE_SORT']['name'],
            item_count=self._data.size(),
            sorted_data=sorted_data.to_list(),
            metrics=metrics_manager.get_metrics()
        )

    def _recursive_merge_sort(self, data: Vector[dict], metrics_manager: AlgorithmMetricsManager) -> Vector[dict]:
        n = data.size()

        if n <= 1:
            return data

        mid = n // 2
        left = data.get_slice(0, mid)
        right = data.get_slice(mid, n)

        left_sorted = self._recursive_merge_sort(left, metrics_manager)
        right_sorted = self._recursive_merge_sort(right, metrics_manager)

        return self._merge(left_sorted, right_sorted, metrics_manager)

    def _merge(self, left: Vector[dict], right: Vector[dict], metrics_manager: AlgorithmMetricsManager) -> Vector[dict]:
        i = j = 0
        merged_data = Vector[dict]([])

        while i < left.size() and j < right.size():
            a = left.get_item(i)
            b = right.get_item(j)
            a_value = self._value_getter(a)
            b_value = self._value_getter(b)

            metrics_manager.increment_comparisons()

            if a_value <= b_value:
                merged_data.append(a)
                i += 1
            else:
                merged_data.append(b)
                j += 1

        if i < left.size():
            merged_data.extend(left.get_slice(i, left.size()))

        if j < right.size():
            merged_data.extend(right.get_slice(j, right.size()))

        return merged_data

    def quick_sort(self):
        metrics_manager = AlgorithmMetricsManager()
        metrics_manager.start()

        sorted_data = self._recursive_quick_sort(
            self._data.copy(), metrics_manager)

        metrics_manager.end()

        return SortResult(
            data_structure=INFO['VECTOR']['name'],
            algorithm=INFO['VECTOR']['sort_algorithms']['QUICK_SORT']['name'],
            item_count=self._data.size(),
            sorted_data=sorted_data.to_list(),
            metrics=metrics_manager.get_metrics()
        )

    def _recursive_quick_sort(self, data: Vector[dict], metrics_manager: AlgorithmMetricsManager) -> Vector[dict]:
        if data.size() <= 1:
            return data

        pivot = data.get_item(data.size() // 2)
        pivot_value = self._value_getter(pivot)

        left = Vector[dict]([])
        middle = Vector[dict]([])
        right = Vector[dict]([])

        for i in range(data.size()):
            x = data.get_item(i)
            x_value = self._value_getter(x)
            metrics_manager.increment_comparisons()

            if x_value < pivot_value:
                left.append(x)
            elif x_value == pivot_value:
                middle.append(x)
            else:
                right.append(x)

        left_sorted = self._recursive_quick_sort(left, metrics_manager)
        right_sorted = self._recursive_quick_sort(right, metrics_manager)

        result = Vector[dict]([])
        result.extend(left_sorted)
        result.extend(middle)
        result.extend(right_sorted)

        return result
