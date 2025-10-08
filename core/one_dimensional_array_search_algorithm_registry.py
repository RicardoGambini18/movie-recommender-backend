import math
from typing import Callable
from core.constants import INFO
from core.results import SearchResult
from core.algorithm_metrics import AlgorithmMetricsManager
from core.data_structure_algorithm_registry import DataStructureOption,  DataStructureAlgorithmRegistry, SearchAlgorithmOption


class OneDimensionalArraySearchAlgorithmRegistry(DataStructureAlgorithmRegistry):
    def __init__(self, data: list[dict] = [], value_getter: Callable[[dict], int] = lambda: 0):
        self.data = data
        self.value_getter = value_getter

    def register(self):
        return DataStructureOption(
            key=INFO['ONE_DIMENSIONAL_ARRAY']['key'],
            name=INFO['ONE_DIMENSIONAL_ARRAY']['name'],
            description=INFO['ONE_DIMENSIONAL_ARRAY']['description'],
            algorithms=[
                SearchAlgorithmOption(
                    key=INFO['ONE_DIMENSIONAL_ARRAY']['search_algorithms']['LINEAR_SEARCH']['key'],
                    name=INFO['ONE_DIMENSIONAL_ARRAY']['search_algorithms']['LINEAR_SEARCH']['name'],
                    needs_sort=INFO['ONE_DIMENSIONAL_ARRAY']['search_algorithms']['LINEAR_SEARCH']['needs_sort'],
                    description=INFO['ONE_DIMENSIONAL_ARRAY']['search_algorithms']['LINEAR_SEARCH']['description'],
                    space_complexity=INFO['ONE_DIMENSIONAL_ARRAY']['search_algorithms']['LINEAR_SEARCH']['space_complexity'],
                    best_time_complexity=INFO['ONE_DIMENSIONAL_ARRAY'][
                        'search_algorithms']['LINEAR_SEARCH']['best_time_complexity'],
                    worst_time_complexity=INFO['ONE_DIMENSIONAL_ARRAY'][
                        'search_algorithms']['LINEAR_SEARCH']['worst_time_complexity'],
                    average_time_complexity=INFO['ONE_DIMENSIONAL_ARRAY'][
                        'search_algorithms']['LINEAR_SEARCH']['average_time_complexity'],
                ),
                SearchAlgorithmOption(
                    key=INFO['ONE_DIMENSIONAL_ARRAY']['search_algorithms']['BINARY_SEARCH']['key'],
                    name=INFO['ONE_DIMENSIONAL_ARRAY']['search_algorithms']['BINARY_SEARCH']['name'],
                    needs_sort=INFO['ONE_DIMENSIONAL_ARRAY']['search_algorithms']['BINARY_SEARCH']['needs_sort'],
                    description=INFO['ONE_DIMENSIONAL_ARRAY']['search_algorithms']['BINARY_SEARCH']['description'],
                    space_complexity=INFO['ONE_DIMENSIONAL_ARRAY']['search_algorithms']['BINARY_SEARCH']['space_complexity'],
                    best_time_complexity=INFO['ONE_DIMENSIONAL_ARRAY'][
                        'search_algorithms']['BINARY_SEARCH']['best_time_complexity'],
                    worst_time_complexity=INFO['ONE_DIMENSIONAL_ARRAY'][
                        'search_algorithms']['BINARY_SEARCH']['worst_time_complexity'],
                    average_time_complexity=INFO['ONE_DIMENSIONAL_ARRAY'][
                        'search_algorithms']['BINARY_SEARCH']['average_time_complexity'],
                ),
                SearchAlgorithmOption(
                    key=INFO['ONE_DIMENSIONAL_ARRAY']['search_algorithms']['JUMP_SEARCH']['key'],
                    name=INFO['ONE_DIMENSIONAL_ARRAY']['search_algorithms']['JUMP_SEARCH']['name'],
                    needs_sort=INFO['ONE_DIMENSIONAL_ARRAY']['search_algorithms']['JUMP_SEARCH']['needs_sort'],
                    description=INFO['ONE_DIMENSIONAL_ARRAY']['search_algorithms']['JUMP_SEARCH']['description'],
                    space_complexity=INFO['ONE_DIMENSIONAL_ARRAY']['search_algorithms']['JUMP_SEARCH']['space_complexity'],
                    best_time_complexity=INFO['ONE_DIMENSIONAL_ARRAY'][
                        'search_algorithms']['JUMP_SEARCH']['best_time_complexity'],
                    worst_time_complexity=INFO['ONE_DIMENSIONAL_ARRAY'][
                        'search_algorithms']['JUMP_SEARCH']['worst_time_complexity'],
                    average_time_complexity=INFO['ONE_DIMENSIONAL_ARRAY'][
                        'search_algorithms']['JUMP_SEARCH']['average_time_complexity'],
                ),
                SearchAlgorithmOption(
                    key=INFO['ONE_DIMENSIONAL_ARRAY']['search_algorithms']['EXPONENTIAL_SEARCH']['key'],
                    name=INFO['ONE_DIMENSIONAL_ARRAY']['search_algorithms']['EXPONENTIAL_SEARCH']['name'],
                    needs_sort=INFO['ONE_DIMENSIONAL_ARRAY']['search_algorithms']['EXPONENTIAL_SEARCH']['needs_sort'],
                    description=INFO['ONE_DIMENSIONAL_ARRAY']['search_algorithms']['EXPONENTIAL_SEARCH']['description'],
                    space_complexity=INFO['ONE_DIMENSIONAL_ARRAY']['search_algorithms']['EXPONENTIAL_SEARCH']['space_complexity'],
                    best_time_complexity=INFO['ONE_DIMENSIONAL_ARRAY'][
                        'search_algorithms']['EXPONENTIAL_SEARCH']['best_time_complexity'],
                    worst_time_complexity=INFO['ONE_DIMENSIONAL_ARRAY'][
                        'search_algorithms']['EXPONENTIAL_SEARCH']['worst_time_complexity'],
                    average_time_complexity=INFO['ONE_DIMENSIONAL_ARRAY'][
                        'search_algorithms']['EXPONENTIAL_SEARCH']['average_time_complexity'],
                ),
                SearchAlgorithmOption(
                    key=INFO['ONE_DIMENSIONAL_ARRAY']['search_algorithms']['INTERPOLATION_SEARCH']['key'],
                    name=INFO['ONE_DIMENSIONAL_ARRAY']['search_algorithms']['INTERPOLATION_SEARCH']['name'],
                    needs_sort=INFO['ONE_DIMENSIONAL_ARRAY']['search_algorithms']['INTERPOLATION_SEARCH']['needs_sort'],
                    description=INFO['ONE_DIMENSIONAL_ARRAY']['search_algorithms']['INTERPOLATION_SEARCH']['description'],
                    space_complexity=INFO['ONE_DIMENSIONAL_ARRAY']['search_algorithms']['INTERPOLATION_SEARCH']['space_complexity'],
                    best_time_complexity=INFO['ONE_DIMENSIONAL_ARRAY'][
                        'search_algorithms']['INTERPOLATION_SEARCH']['best_time_complexity'],
                    worst_time_complexity=INFO['ONE_DIMENSIONAL_ARRAY'][
                        'search_algorithms']['INTERPOLATION_SEARCH']['worst_time_complexity'],
                    average_time_complexity=INFO['ONE_DIMENSIONAL_ARRAY'][
                        'search_algorithms']['INTERPOLATION_SEARCH']['average_time_complexity'],
                ),
            ]
        )

    def linear_search(self, value: int):
        metrics_manager = AlgorithmMetricsManager()
        metrics_manager.start()

        for index, item in enumerate(self.data):
            metrics_manager.increment_comparisons()

            if self.value_getter(item) == value:
                metrics_manager.end()

                return SearchResult(
                    data_structure=INFO['ONE_DIMENSIONAL_ARRAY']['name'],
                    algorithm=INFO['ONE_DIMENSIONAL_ARRAY']['search_algorithms']['LINEAR_SEARCH']['name'],
                    needs_sort=INFO['ONE_DIMENSIONAL_ARRAY']['search_algorithms']['LINEAR_SEARCH']['needs_sort'],
                    item_count=len(self.data),
                    item_found=item,
                    item_found_index=index,
                    metrics=metrics_manager.get_metrics()
                )

        metrics_manager.end()

        return SearchResult(
            data_structure=INFO['ONE_DIMENSIONAL_ARRAY']['name'],
            algorithm=INFO['ONE_DIMENSIONAL_ARRAY']['search_algorithms']['LINEAR_SEARCH']['name'],
            needs_sort=INFO['ONE_DIMENSIONAL_ARRAY']['search_algorithms']['LINEAR_SEARCH']['needs_sort'],
            item_count=len(self.data),
            item_found=None,
            item_found_index=None,
            metrics=metrics_manager.get_metrics()
        )

    def binary_search(self, value: int):
        metrics_manager = AlgorithmMetricsManager()
        metrics_manager.start()

        low = 0
        high = len(self.data) - 1

        while low <= high:
            mid = (low + high) // 2
            item = self.data[mid]
            item_value = self.value_getter(item)
            metrics_manager.increment_comparisons()

            if item_value == value:
                metrics_manager.end()

                return SearchResult(
                    data_structure=INFO['ONE_DIMENSIONAL_ARRAY']['name'],
                    algorithm=INFO['ONE_DIMENSIONAL_ARRAY']['search_algorithms']['BINARY_SEARCH']['name'],
                    needs_sort=INFO['ONE_DIMENSIONAL_ARRAY']['search_algorithms']['BINARY_SEARCH']['needs_sort'],
                    item_count=len(self.data),
                    item_found=item,
                    item_found_index=mid,
                    metrics=metrics_manager.get_metrics()
                )
            elif item_value < value:
                low = mid + 1
            else:
                high = mid - 1

        metrics_manager.end()

        return SearchResult(
            data_structure=INFO['ONE_DIMENSIONAL_ARRAY']['name'],
            algorithm=INFO['ONE_DIMENSIONAL_ARRAY']['search_algorithms']['BINARY_SEARCH']['name'],
            needs_sort=INFO['ONE_DIMENSIONAL_ARRAY']['search_algorithms']['BINARY_SEARCH']['needs_sort'],
            item_count=len(self.data),
            item_found=None,
            item_found_index=None,
            metrics=metrics_manager.get_metrics()
        )

    def jump_search(self, value: int):
        metrics_manager = AlgorithmMetricsManager()
        metrics_manager.start()

        n = len(self.data)

        if n == 0:
            metrics_manager.end()

            return SearchResult(
                data_structure=INFO['ONE_DIMENSIONAL_ARRAY']['name'],
                algorithm=INFO['ONE_DIMENSIONAL_ARRAY']['search_algorithms']['JUMP_SEARCH']['name'],
                needs_sort=INFO['ONE_DIMENSIONAL_ARRAY']['search_algorithms']['JUMP_SEARCH']['needs_sort'],
                item_count=len(self.data),
                item_found=None,
                item_found_index=None,
                metrics=metrics_manager.get_metrics()
            )

        step_size = math.floor(math.sqrt(n))
        steps = n // step_size

        if (steps * step_size) < n:
            steps += 1

        target_start = -1
        target_end = -1

        for step in range(steps):
            current_start = step_size * step
            current_end = min(current_start + step_size, n)
            current_item = self.data[current_end - 1]
            current_value = self.value_getter(current_item)
            metrics_manager.increment_comparisons()

            if value <= current_value:
                target_start = current_start
                target_end = current_end
                break

        if target_start == -1 or target_end == -1:
            metrics_manager.end()

            return SearchResult(
                data_structure=INFO['ONE_DIMENSIONAL_ARRAY']['name'],
                algorithm=INFO['ONE_DIMENSIONAL_ARRAY']['search_algorithms']['JUMP_SEARCH']['name'],
                needs_sort=INFO['ONE_DIMENSIONAL_ARRAY']['search_algorithms']['JUMP_SEARCH']['needs_sort'],
                item_count=len(self.data),
                item_found=None,
                item_found_index=None,
                metrics=metrics_manager.get_metrics()
            )

        for i in range(target_start, target_end):
            item = self.data[i]
            item_value = self.value_getter(item)
            metrics_manager.increment_comparisons()

            if item_value == value:
                metrics_manager.end()

                return SearchResult(
                    data_structure=INFO['ONE_DIMENSIONAL_ARRAY']['name'],
                    algorithm=INFO['ONE_DIMENSIONAL_ARRAY']['search_algorithms']['JUMP_SEARCH']['name'],
                    needs_sort=INFO['ONE_DIMENSIONAL_ARRAY']['search_algorithms']['JUMP_SEARCH']['needs_sort'],
                    item_count=len(self.data),
                    item_found=item,
                    item_found_index=i,
                    metrics=metrics_manager.get_metrics()
                )

        metrics_manager.end()

        return SearchResult(
            data_structure=INFO['ONE_DIMENSIONAL_ARRAY']['name'],
            algorithm=INFO['ONE_DIMENSIONAL_ARRAY']['search_algorithms']['JUMP_SEARCH']['name'],
            needs_sort=INFO['ONE_DIMENSIONAL_ARRAY']['search_algorithms']['JUMP_SEARCH']['needs_sort'],
            item_count=len(self.data),
            item_found=None,
            item_found_index=None,
            metrics=metrics_manager.get_metrics()
        )

    def exponential_search(self, value: int):
        metrics_manager = AlgorithmMetricsManager()
        metrics_manager.start()

        n = len(self.data)

        if n == 0:
            metrics_manager.end()

            return SearchResult(
                data_structure=INFO['ONE_DIMENSIONAL_ARRAY']['name'],
                algorithm=INFO['ONE_DIMENSIONAL_ARRAY']['search_algorithms']['EXPONENTIAL_SEARCH']['name'],
                needs_sort=INFO['ONE_DIMENSIONAL_ARRAY']['search_algorithms']['EXPONENTIAL_SEARCH']['needs_sort'],
                item_count=0,
                item_found=None,
                item_found_index=None,
                metrics=metrics_manager.get_metrics()
            )

        first_item = self.data[0]
        first_value = self.value_getter(first_item)
        metrics_manager.increment_comparisons()

        if first_value == value:
            metrics_manager.end()

            return SearchResult(
                data_structure=INFO['ONE_DIMENSIONAL_ARRAY']['name'],
                algorithm=INFO['ONE_DIMENSIONAL_ARRAY']['search_algorithms']['EXPONENTIAL_SEARCH']['name'],
                needs_sort=INFO['ONE_DIMENSIONAL_ARRAY']['search_algorithms']['EXPONENTIAL_SEARCH']['needs_sort'],
                item_count=len(self.data),
                item_found=first_item,
                item_found_index=0,
                metrics=metrics_manager.get_metrics()
            )

        i = 1

        while i < n:
            current_item = self.data[i]
            current_value = self.value_getter(current_item)
            metrics_manager.increment_comparisons()

            if current_value > value:
                break

            i = i * 2

        left = i // 2
        right = min(i, n - 1)

        found_result = self.recursive_binary_search(
            self.data, left, right, value, metrics_manager)

        metrics_manager.end()

        return SearchResult(
            data_structure=INFO['ONE_DIMENSIONAL_ARRAY']['name'],
            algorithm=INFO['ONE_DIMENSIONAL_ARRAY']['search_algorithms']['EXPONENTIAL_SEARCH']['name'],
            needs_sort=INFO['ONE_DIMENSIONAL_ARRAY']['search_algorithms']['EXPONENTIAL_SEARCH']['needs_sort'],
            item_count=len(self.data),
            item_found=found_result['item'] if found_result else None,
            item_found_index=found_result['index'] if found_result else None,
            metrics=metrics_manager.get_metrics()
        )

    def recursive_binary_search(self, data, left, right, value, metrics_manager):
        if right >= left:
            mid = left + (right - left) // 2
            mid_item = data[mid]
            mid_value = self.value_getter(mid_item)

            metrics_manager.increment_comparisons()

            if mid_value == value:
                return {'item': mid_item, 'index': mid}

            if mid_value > value:
                return self.recursive_binary_search(data, left, mid - 1, value, metrics_manager)

            return self.recursive_binary_search(data, mid + 1, right, value, metrics_manager)

        return None

    def interpolation_search(self, value: int):
        metrics_manager = AlgorithmMetricsManager()
        metrics_manager.start()

        n = len(self.data)

        if n == 0:
            metrics_manager.end()

            return SearchResult(
                data_structure=INFO['ONE_DIMENSIONAL_ARRAY']['name'],
                algorithm=INFO['ONE_DIMENSIONAL_ARRAY']['search_algorithms']['INTERPOLATION_SEARCH']['name'],
                needs_sort=INFO['ONE_DIMENSIONAL_ARRAY']['search_algorithms']['INTERPOLATION_SEARCH']['needs_sort'],
                item_count=0,
                item_found=None,
                item_found_index=None,
                metrics=metrics_manager.get_metrics()
            )

        found_result = self.recursive_interpolation_search(
            self.data, 0, n - 1, value, metrics_manager)

        metrics_manager.end()

        return SearchResult(
            data_structure=INFO['ONE_DIMENSIONAL_ARRAY']['name'],
            algorithm=INFO['ONE_DIMENSIONAL_ARRAY']['search_algorithms']['INTERPOLATION_SEARCH']['name'],
            needs_sort=INFO['ONE_DIMENSIONAL_ARRAY']['search_algorithms']['INTERPOLATION_SEARCH']['needs_sort'],
            item_count=len(self.data),
            item_found=found_result['item'] if found_result else None,
            item_found_index=found_result['index'] if found_result else None,
            metrics=metrics_manager.get_metrics()
        )

    def recursive_interpolation_search(self, data, left, right, value, metrics_manager):
        if left <= right:
            left_item = data[left]
            right_item = data[right]
            left_value = self.value_getter(left_item)
            right_value = self.value_getter(right_item)

            metrics_manager.increment_comparisons()

            if value < left_value or value > right_value:
                return None

            if left_value == right_value:
                for i in range(left, right + 1):
                    item = data[i]
                    item_value = self.value_getter(item)

                    metrics_manager.increment_comparisons()

                    if item_value == value:
                        return {'item': item, 'index': i}

                return None

            pos = left + (((right - left) * (value - left_value)
                           ) // (right_value - left_value))

            pos = max(left, min(pos, right))

            pos_item = data[pos]
            pos_value = self.value_getter(pos_item)

            metrics_manager.increment_comparisons()

            if pos_value == value:
                return {'item': pos_item, 'index': pos}

            if pos_value < value:
                return self.recursive_interpolation_search(data, pos + 1, right, value, metrics_manager)

            return self.recursive_interpolation_search(data, left, pos - 1, value, metrics_manager)

        return None
