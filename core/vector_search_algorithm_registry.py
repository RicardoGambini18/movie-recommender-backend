import math
from typing import Callable
from core.constants import INFO
from core.results import SearchResult
from core.data_structures import Vector
from core.algorithm_metrics import AlgorithmMetricsManager
from core.data_structure_algorithm_registry import DataStructureOption,  DataStructureAlgorithmRegistry, SearchAlgorithmOption


class VectorSearchAlgorithmRegistry(DataStructureAlgorithmRegistry):
    def __init__(self, data: list[dict] = [], value_getter: Callable[[dict], int] = lambda: 0):
        self._value_getter = value_getter
        self._data: Vector[dict] = Vector(data)

    def register(self):
        return DataStructureOption(
            key=INFO['VECTOR']['key'],
            name=INFO['VECTOR']['name'],
            description=INFO['VECTOR']['description'],
            algorithms=[
                SearchAlgorithmOption(
                    key=INFO['VECTOR']['search_algorithms']['LINEAR_SEARCH']['key'],
                    name=INFO['VECTOR']['search_algorithms']['LINEAR_SEARCH']['name'],
                    needs_sort=INFO['VECTOR']['search_algorithms']['LINEAR_SEARCH']['needs_sort'],
                    description=INFO['VECTOR']['search_algorithms']['LINEAR_SEARCH']['description'],
                    space_complexity=INFO['VECTOR']['search_algorithms']['LINEAR_SEARCH']['space_complexity'],
                    best_time_complexity=INFO['VECTOR'][
                        'search_algorithms']['LINEAR_SEARCH']['best_time_complexity'],
                    worst_time_complexity=INFO['VECTOR'][
                        'search_algorithms']['LINEAR_SEARCH']['worst_time_complexity'],
                    average_time_complexity=INFO['VECTOR'][
                        'search_algorithms']['LINEAR_SEARCH']['average_time_complexity'],
                ),
                SearchAlgorithmOption(
                    key=INFO['VECTOR']['search_algorithms']['BINARY_SEARCH']['key'],
                    name=INFO['VECTOR']['search_algorithms']['BINARY_SEARCH']['name'],
                    needs_sort=INFO['VECTOR']['search_algorithms']['BINARY_SEARCH']['needs_sort'],
                    description=INFO['VECTOR']['search_algorithms']['BINARY_SEARCH']['description'],
                    space_complexity=INFO['VECTOR']['search_algorithms']['BINARY_SEARCH']['space_complexity'],
                    best_time_complexity=INFO['VECTOR'][
                        'search_algorithms']['BINARY_SEARCH']['best_time_complexity'],
                    worst_time_complexity=INFO['VECTOR'][
                        'search_algorithms']['BINARY_SEARCH']['worst_time_complexity'],
                    average_time_complexity=INFO['VECTOR'][
                        'search_algorithms']['BINARY_SEARCH']['average_time_complexity'],
                ),
                SearchAlgorithmOption(
                    key=INFO['VECTOR']['search_algorithms']['JUMP_SEARCH']['key'],
                    name=INFO['VECTOR']['search_algorithms']['JUMP_SEARCH']['name'],
                    needs_sort=INFO['VECTOR']['search_algorithms']['JUMP_SEARCH']['needs_sort'],
                    description=INFO['VECTOR']['search_algorithms']['JUMP_SEARCH']['description'],
                    space_complexity=INFO['VECTOR']['search_algorithms']['JUMP_SEARCH']['space_complexity'],
                    best_time_complexity=INFO['VECTOR'][
                        'search_algorithms']['JUMP_SEARCH']['best_time_complexity'],
                    worst_time_complexity=INFO['VECTOR'][
                        'search_algorithms']['JUMP_SEARCH']['worst_time_complexity'],
                    average_time_complexity=INFO['VECTOR'][
                        'search_algorithms']['JUMP_SEARCH']['average_time_complexity'],
                ),
                SearchAlgorithmOption(
                    key=INFO['VECTOR']['search_algorithms']['EXPONENTIAL_SEARCH']['key'],
                    name=INFO['VECTOR']['search_algorithms']['EXPONENTIAL_SEARCH']['name'],
                    needs_sort=INFO['VECTOR']['search_algorithms']['EXPONENTIAL_SEARCH']['needs_sort'],
                    description=INFO['VECTOR']['search_algorithms']['EXPONENTIAL_SEARCH']['description'],
                    space_complexity=INFO['VECTOR']['search_algorithms']['EXPONENTIAL_SEARCH']['space_complexity'],
                    best_time_complexity=INFO['VECTOR'][
                        'search_algorithms']['EXPONENTIAL_SEARCH']['best_time_complexity'],
                    worst_time_complexity=INFO['VECTOR'][
                        'search_algorithms']['EXPONENTIAL_SEARCH']['worst_time_complexity'],
                    average_time_complexity=INFO['VECTOR'][
                        'search_algorithms']['EXPONENTIAL_SEARCH']['average_time_complexity'],
                ),
                SearchAlgorithmOption(
                    key=INFO['VECTOR']['search_algorithms']['INTERPOLATION_SEARCH']['key'],
                    name=INFO['VECTOR']['search_algorithms']['INTERPOLATION_SEARCH']['name'],
                    needs_sort=INFO['VECTOR']['search_algorithms']['INTERPOLATION_SEARCH']['needs_sort'],
                    description=INFO['VECTOR']['search_algorithms']['INTERPOLATION_SEARCH']['description'],
                    space_complexity=INFO['VECTOR']['search_algorithms']['INTERPOLATION_SEARCH']['space_complexity'],
                    best_time_complexity=INFO['VECTOR'][
                        'search_algorithms']['INTERPOLATION_SEARCH']['best_time_complexity'],
                    worst_time_complexity=INFO['VECTOR'][
                        'search_algorithms']['INTERPOLATION_SEARCH']['worst_time_complexity'],
                    average_time_complexity=INFO['VECTOR'][
                        'search_algorithms']['INTERPOLATION_SEARCH']['average_time_complexity'],
                ),
            ]
        )

    def linear_search(self, value: int):
        metrics_manager = AlgorithmMetricsManager()
        metrics_manager.start()

        for index in range(self._data.size()):
            item = self._data.get_item(index)
            item_value = self._value_getter(item)
            metrics_manager.increment_operations(4)

            if item_value == value:
                metrics_manager.end()

                return SearchResult(
                    data_structure=INFO['VECTOR']['name'],
                    algorithm=INFO['VECTOR']['search_algorithms']['LINEAR_SEARCH']['name'],
                    needs_sort=INFO['VECTOR']['search_algorithms']['LINEAR_SEARCH']['needs_sort'],
                    item_count=self._data.size(),
                    item_found=item,
                    metrics=metrics_manager.get_metrics()
                )

        metrics_manager.end()

        return SearchResult(
            data_structure=INFO['VECTOR']['name'],
            algorithm=INFO['VECTOR']['search_algorithms']['LINEAR_SEARCH']['name'],
            needs_sort=INFO['VECTOR']['search_algorithms']['LINEAR_SEARCH']['needs_sort'],
            item_count=self._data.size(),
            item_found=None,
            metrics=metrics_manager.get_metrics()
        )

    def binary_search(self, value: int):
        metrics_manager = AlgorithmMetricsManager()
        metrics_manager.start()

        low = 0
        high = self._data.size() - 1
        metrics_manager.increment_operations(2)

        while low <= high:
            mid = (low + high) // 2
            item = self._data.get_item(mid)
            item_value = self._value_getter(item)
            metrics_manager.increment_operations(5)

            if item_value == value:
                metrics_manager.end()

                return SearchResult(
                    data_structure=INFO['VECTOR']['name'],
                    algorithm=INFO['VECTOR']['search_algorithms']['BINARY_SEARCH']['name'],
                    needs_sort=INFO['VECTOR']['search_algorithms']['BINARY_SEARCH']['needs_sort'],
                    item_count=self._data.size(),
                    item_found=item,
                    metrics=metrics_manager.get_metrics()
                )
            elif item_value < value:
                low = mid + 1
                metrics_manager.increment_operations(1)
            else:
                high = mid - 1
                metrics_manager.increment_operations(1)

        metrics_manager.increment_operations(1)

        metrics_manager.end()

        return SearchResult(
            data_structure=INFO['VECTOR']['name'],
            algorithm=INFO['VECTOR']['search_algorithms']['BINARY_SEARCH']['name'],
            needs_sort=INFO['VECTOR']['search_algorithms']['BINARY_SEARCH']['needs_sort'],
            item_count=self._data.size(),
            item_found=None,
            metrics=metrics_manager.get_metrics()
        )

    def jump_search(self, value: int):
        metrics_manager = AlgorithmMetricsManager()
        metrics_manager.start()

        n = self._data.size()
        metrics_manager.increment_operations(2)

        if n == 0:
            metrics_manager.end()

            return SearchResult(
                data_structure=INFO['VECTOR']['name'],
                algorithm=INFO['VECTOR']['search_algorithms']['JUMP_SEARCH']['name'],
                needs_sort=INFO['VECTOR']['search_algorithms']['JUMP_SEARCH']['needs_sort'],
                item_count=self._data.size(),
                item_found=None,
                metrics=metrics_manager.get_metrics()
            )

        step_size = math.floor(math.sqrt(n))
        steps = n // step_size
        metrics_manager.increment_operations(4)

        if (steps * step_size) < n:
            metrics_manager.increment_operations(1)
            steps += 1

        target_start = -1
        target_end = -1
        metrics_manager.increment_operations(2)

        for step in range(steps):
            current_start = step_size * step
            current_end = min(current_start + step_size, n)
            current_item = self._data.get_item(current_end - 1)
            current_value = self._value_getter(current_item)
            metrics_manager.increment_operations(6)

            if value <= current_value:
                target_start = current_start
                target_end = current_end
                metrics_manager.increment_operations(2)
                break

        metrics_manager.increment_operations(1)

        if target_start == -1 or target_end == -1:
            metrics_manager.end()

            return SearchResult(
                data_structure=INFO['VECTOR']['name'],
                algorithm=INFO['VECTOR']['search_algorithms']['JUMP_SEARCH']['name'],
                needs_sort=INFO['VECTOR']['search_algorithms']['JUMP_SEARCH']['needs_sort'],
                item_count=self._data.size(),
                item_found=None,
                metrics=metrics_manager.get_metrics()
            )

        for index in range(target_start, target_end):
            item = self._data.get_item(index)
            item_value = self._value_getter(item)
            metrics_manager.increment_operations(4)

            if item_value == value:
                metrics_manager.end()

                return SearchResult(
                    data_structure=INFO['VECTOR']['name'],
                    algorithm=INFO['VECTOR']['search_algorithms']['JUMP_SEARCH']['name'],
                    needs_sort=INFO['VECTOR']['search_algorithms']['JUMP_SEARCH']['needs_sort'],
                    item_count=self._data.size(),
                    item_found=item,
                    metrics=metrics_manager.get_metrics()
                )

        metrics_manager.end()

        return SearchResult(
            data_structure=INFO['VECTOR']['name'],
            algorithm=INFO['VECTOR']['search_algorithms']['JUMP_SEARCH']['name'],
            needs_sort=INFO['VECTOR']['search_algorithms']['JUMP_SEARCH']['needs_sort'],
            item_count=self._data.size(),
            item_found=None,
            metrics=metrics_manager.get_metrics()
        )

    def exponential_search(self, value: int):
        metrics_manager = AlgorithmMetricsManager()
        metrics_manager.start()

        n = self._data.size()
        metrics_manager.increment_operations(2)

        if n == 0:
            metrics_manager.end()

            return SearchResult(
                data_structure=INFO['VECTOR']['name'],
                algorithm=INFO['VECTOR']['search_algorithms']['EXPONENTIAL_SEARCH']['name'],
                needs_sort=INFO['VECTOR']['search_algorithms']['EXPONENTIAL_SEARCH']['needs_sort'],
                item_count=0,
                item_found=None,
                metrics=metrics_manager.get_metrics()
            )

        first_item = self._data.get_item(0)
        first_value = self._value_getter(first_item)
        metrics_manager.increment_operations(3)

        if first_value == value:
            metrics_manager.end()

            return SearchResult(
                data_structure=INFO['VECTOR']['name'],
                algorithm=INFO['VECTOR']['search_algorithms']['EXPONENTIAL_SEARCH']['name'],
                needs_sort=INFO['VECTOR']['search_algorithms']['EXPONENTIAL_SEARCH']['needs_sort'],
                item_count=self._data.size(),
                item_found=first_item,
                metrics=metrics_manager.get_metrics()
            )

        i = 1
        metrics_manager.increment_operations(1)

        while i < n:
            current_item = self._data.get_item(i)
            current_value = self._value_getter(current_item)
            metrics_manager.increment_operations(4)

            if current_value > value:
                break

            i = i * 2
            metrics_manager.increment_operations(1)

        left = i // 2
        right = min(i, n - 1)
        metrics_manager.increment_operations(3)

        found_result = self._recursive_binary_search(
            self._data, left, right, value, metrics_manager)

        metrics_manager.end()

        return SearchResult(
            data_structure=INFO['VECTOR']['name'],
            algorithm=INFO['VECTOR']['search_algorithms']['EXPONENTIAL_SEARCH']['name'],
            needs_sort=INFO['VECTOR']['search_algorithms']['EXPONENTIAL_SEARCH']['needs_sort'],
            item_count=self._data.size(),
            item_found=found_result['item'] if found_result else None,
            metrics=metrics_manager.get_metrics()
        )

    def _recursive_binary_search(self, data, left, right, value, metrics_manager):
        metrics_manager.increment_operations(1)

        if right >= left:
            mid = left + (right - left) // 2
            mid_item = data.get_item(mid)
            mid_value = self._value_getter(mid_item)

            metrics_manager.increment_operations(7)

            if mid_value == value:
                return {'item': mid_item, 'index': mid}

            if mid_value > value:
                return self._recursive_binary_search(data, left, mid - 1, value, metrics_manager)

            return self._recursive_binary_search(data, mid + 1, right, value, metrics_manager)

        return None

    def interpolation_search(self, value: int):
        metrics_manager = AlgorithmMetricsManager()
        metrics_manager.start()

        n = self._data.size()
        metrics_manager.increment_operations(2)

        if n == 0:
            metrics_manager.end()

            return SearchResult(
                data_structure=INFO['VECTOR']['name'],
                algorithm=INFO['VECTOR']['search_algorithms']['INTERPOLATION_SEARCH']['name'],
                needs_sort=INFO['VECTOR']['search_algorithms']['INTERPOLATION_SEARCH']['needs_sort'],
                item_count=0,
                item_found=None,
                metrics=metrics_manager.get_metrics()
            )

        found_result = self._recursive_interpolation_search(
            self._data, 0, n - 1, value, metrics_manager)

        metrics_manager.end()

        return SearchResult(
            data_structure=INFO['VECTOR']['name'],
            algorithm=INFO['VECTOR']['search_algorithms']['INTERPOLATION_SEARCH']['name'],
            needs_sort=INFO['VECTOR']['search_algorithms']['INTERPOLATION_SEARCH']['needs_sort'],
            item_count=self._data.size(),
            item_found=found_result['item'] if found_result else None,
            metrics=metrics_manager.get_metrics()
        )

    def _recursive_interpolation_search(self, data, left, right, value, metrics_manager):
        metrics_manager.increment_operations(1)

        if left <= right:
            left_item = data.get_item(left)
            right_item = data.get_item(right)
            left_value = self._value_getter(left_item)
            right_value = self._value_getter(right_item)

            metrics_manager.increment_operations(6)

            if value < left_value or value > right_value:
                return None

            metrics_manager.increment_operations(1)

            if left_value == right_value:
                for i in range(left, right + 1):
                    item = data.get_item(i)
                    item_value = self._value_getter(item)

                    metrics_manager.increment_operations(4)

                    if item_value == value:
                        return {'item': item, 'index': i}

                return None

            pos = left + (((right - left) * (value - left_value)
                           ) // (right_value - left_value))

            pos = max(left, min(pos, right))

            pos_item = data.get_item(pos)
            pos_value = self._value_getter(pos_item)

            metrics_manager.increment_operations(12)

            if pos_value == value:
                return {'item': pos_item, 'index': pos}

            if pos_value < value:
                return self._recursive_interpolation_search(data, pos + 1, right, value, metrics_manager)

            return self._recursive_interpolation_search(data, left, pos - 1, value, metrics_manager)

        return None
