from typing import Callable
from core.results import SearchResult
from core.algorithm_metrics import AlgorithmMetricsManager
from core.data_structure_algorithm_registry import AlgorithmOption, DataStructureOption,  DataStructureAlgorithmRegistry


class OneDimensionalArraySearchAlgorithm(DataStructureAlgorithmRegistry):
    def __init__(self, data: list[dict] = [], value_getter: Callable[[dict], int] = lambda: 0):
        self.data = data
        self.value_getter = value_getter

    def register(self) -> DataStructureOption:
        return DataStructureOption(
            key="one_dimensional_array",
            name="Arreglo Unidimensional",
            description="Un arreglo unidimensional es una estructura de datos que almacena elementos secuencialmente en una sola dimensión.",
            algorithms=[
                AlgorithmOption(
                    complexity="O(n)",
                    key="linear_search",
                    name="Búsqueda Lineal",
                    description="Busca un valor en el arreglo de forma lineal"
                ),
            ]
        )

    def linear_search(self, value: int) -> SearchResult:
        metrics_manager = AlgorithmMetricsManager()
        metrics_manager.start()

        for item in self.data:
            if self.value_getter(item) == value:
                metrics_manager.increment_comparisons()
                metrics_manager.end()
                return SearchResult(
                    data_structure="Arreglo Unidimensional",
                    algorithm="Búsqueda Lineal",
                    item_count=len(self.data),
                    item_found=item,
                    metrics=metrics_manager.get_metrics()
                )
            else:
                metrics_manager.increment_comparisons()

        metrics_manager.end()
        return SearchResult(
            data_structure="Arreglo Unidimensional",
            algorithm="Búsqueda Lineal",
            item_count=len(self.data),
            item_found=None,
            metrics=metrics_manager.get_metrics()
        )
