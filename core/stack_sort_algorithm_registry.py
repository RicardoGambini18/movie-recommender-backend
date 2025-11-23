from typing import Callable
from core.constants import INFO
from core.results import SortResult
from core.data_structures import Stack
from core.algorithm_metrics import AlgorithmMetricsManager
from core.data_structure_algorithm_registry import AlgorithmOption, DataStructureOption, DataStructureAlgorithmRegistry


class StackSortAlgorithmRegistry(DataStructureAlgorithmRegistry):
    def __init__(self, data: list[dict] = [], value_getter: Callable[[dict], int] = lambda: 0):
        self._value_getter = value_getter
        self._data: Stack[dict] = Stack(data)

    def register(self):
        return DataStructureOption(
            key=INFO['STACK']['key'],
            name=INFO['STACK']['name'],
            description=INFO['STACK']['description'],
            algorithms=[
                AlgorithmOption(
                    key=INFO['STACK']['sort_algorithms']['SORT_STACK']['key'],
                    name=INFO['STACK']['sort_algorithms']['SORT_STACK']['name'],
                    description=INFO['STACK']['sort_algorithms']['SORT_STACK']['description'],
                    space_complexity=INFO['STACK']['sort_algorithms']['SORT_STACK']['space_complexity'],
                    best_time_complexity=INFO['STACK']['sort_algorithms']['SORT_STACK']['best_time_complexity'],
                    worst_time_complexity=INFO['STACK']['sort_algorithms']['SORT_STACK']['worst_time_complexity'],
                    average_time_complexity=INFO['STACK']['sort_algorithms']['SORT_STACK']['average_time_complexity'],
                ),
            ]
        )

    def sort_stack(self):
        metrics_manager = AlgorithmMetricsManager()
        metrics_manager.start()

        sorted_data = Stack[dict]()
        aux_stack = self._data.copy()
        item_count = self._data.size()

        while not aux_stack.is_empty():
            item = aux_stack.pop()
            item_value = self._value_getter(item)

            while not sorted_data.is_empty():
                top = sorted_data.peek()
                top_value = self._value_getter(top)
                metrics_manager.increment_comparisons()

                if top_value > item_value:
                    aux_stack.push(sorted_data.pop())
                else:
                    break

            sorted_data.push(item)

        metrics_manager.end()

        return SortResult(
            data_structure=INFO['STACK']['name'],
            algorithm=INFO['STACK']['sort_algorithms']['SORT_STACK']['name'],
            item_count=item_count,
            sorted_data=sorted_data.to_list(),
            metrics=metrics_manager.get_metrics()
        )
