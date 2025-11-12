from typing import Callable
from core.constants import INFO
from core.results import SortResult
from core.algorithm_metrics import AlgorithmMetricsManager
from core.data_structure_algorithm_registry import AlgorithmOption, DataStructureOption,  DataStructureAlgorithmRegistry


class VectorSortAlgorithmRegistry(DataStructureAlgorithmRegistry):
    def __init__(self, data: list[dict] = [], value_getter: Callable[[dict], int] = lambda: 0):
        self.data = data
        self.value_getter = value_getter

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

        sorted_data = self.data.copy()
        n = len(sorted_data)

        for i in range(n):
            is_sorted = True

            for j in range(n - i - 1):
                a = sorted_data[j]
                b = sorted_data[j + 1]
                a_value = self.value_getter(a)
                b_value = self.value_getter(b)

                metrics_manager.increment_comparisons()

                if a_value > b_value:
                    sorted_data[j], sorted_data[j + 1] = b, a
                    is_sorted = False

            if is_sorted:
                break

        metrics_manager.end()

        return SortResult(
            data_structure=INFO['VECTOR']['name'],
            algorithm=INFO['VECTOR']['sort_algorithms']['BUBBLE_SORT']['name'],
            item_count=len(self.data),
            sorted_data=sorted_data,
            metrics=metrics_manager.get_metrics()
        )

    def selection_sort(self):
        metrics_manager = AlgorithmMetricsManager()
        metrics_manager.start()

        sorted_data = self.data.copy()
        n = len(sorted_data)

        for i in range(n):
            min_index = i
            min_value = self.value_getter(sorted_data[i])

            for j in range(i + 1, n):
                value = self.value_getter(sorted_data[j])

                if value < min_value:
                    min_index = j
                    min_value = value

                metrics_manager.increment_comparisons()

            sorted_data[i], sorted_data[min_index] = sorted_data[min_index], sorted_data[i]

        metrics_manager.end()

        return SortResult(
            data_structure=INFO['VECTOR']['name'],
            algorithm=INFO['VECTOR']['sort_algorithms']['SELECTION_SORT']['name'],
            item_count=len(self.data),
            sorted_data=sorted_data,
            metrics=metrics_manager.get_metrics()
        )

    def insertion_sort(self):
        metrics_manager = AlgorithmMetricsManager()
        metrics_manager.start()

        sorted_data = self.data.copy()
        n = len(sorted_data)

        for i in range(1, n):
            item = sorted_data[i]
            item_value = self.value_getter(item)

            j = i - 1
            previous_item = sorted_data[j]
            previous_item_value = self.value_getter(previous_item)

            while j >= 0 and previous_item_value > item_value:
                metrics_manager.increment_comparisons()
                sorted_data[j + 1] = previous_item

                j -= 1
                previous_item = sorted_data[j]
                previous_item_value = self.value_getter(previous_item)

            metrics_manager.increment_comparisons()
            sorted_data[j + 1] = item

        metrics_manager.end()

        return SortResult(
            data_structure=INFO['VECTOR']['name'],
            algorithm=INFO['VECTOR']['sort_algorithms']['INSERTION_SORT']['name'],
            item_count=len(self.data),
            sorted_data=sorted_data,
            metrics=metrics_manager.get_metrics()
        )

    def merge_sort(self):
        metrics_manager = AlgorithmMetricsManager()
        metrics_manager.start()

        sorted_data = self.recursive_merge_sort(
            self.data.copy(), metrics_manager)

        metrics_manager.end()

        return SortResult(
            data_structure=INFO['VECTOR']['name'],
            algorithm=INFO['VECTOR']['sort_algorithms']['MERGE_SORT']['name'],
            item_count=len(self.data),
            sorted_data=sorted_data,
            metrics=metrics_manager.get_metrics()
        )

    def recursive_merge_sort(self, data, metrics_manager):
        n = len(data)

        if n <= 1:
            return data

        mid = n // 2
        left = data[:mid]
        right = data[mid:]

        left_sorted = self.recursive_merge_sort(left, metrics_manager)
        right_sorted = self.recursive_merge_sort(right, metrics_manager)

        return self.merge(left_sorted, right_sorted, metrics_manager)

    def merge(self, left, right, metrics_manager):
        i = j = 0
        merged_data = []

        while i < len(left) and j < len(right):
            a = left[i]
            b = right[j]
            a_value = self.value_getter(a)
            b_value = self.value_getter(b)

            metrics_manager.increment_comparisons()

            if a_value <= b_value:
                merged_data.append(a)
                i += 1
            else:
                merged_data.append(b)
                j += 1

        merged_data.extend(left[i:])
        merged_data.extend(right[j:])

        return merged_data

    def quick_sort(self):
        metrics_manager = AlgorithmMetricsManager()
        metrics_manager.start()

        sorted_data = self.recursive_quick_sort(
            self.data.copy(), metrics_manager)

        metrics_manager.end()

        return SortResult(
            data_structure=INFO['VECTOR']['name'],
            algorithm=INFO['VECTOR']['sort_algorithms']['QUICK_SORT']['name'],
            item_count=len(self.data),
            sorted_data=sorted_data,
            metrics=metrics_manager.get_metrics()
        )

    def recursive_quick_sort(self, data, metrics_manager):
        if len(data) <= 1:
            return data

        pivot = data[len(data) // 2]
        pivot_value = self.value_getter(pivot)

        left = []
        middle = []
        right = []

        for x in data:
            x_value = self.value_getter(x)
            metrics_manager.increment_comparisons()

            if x_value < pivot_value:
                left.append(x)
            elif x_value == pivot_value:
                middle.append(x)
            else:
                right.append(x)

        return (self.recursive_quick_sort(left, metrics_manager) +
                middle +
                self.recursive_quick_sort(right, metrics_manager))
