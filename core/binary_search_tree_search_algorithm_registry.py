from typing import Callable
from core.constants import INFO
from core.results import SearchResult
from core.algorithm_metrics import AlgorithmMetricsManager
from core.data_structures import BinarySearchTree, TreeNode, Queue
from core.data_structure_algorithm_registry import DataStructureOption, DataStructureAlgorithmRegistry, SearchAlgorithmOption


class BinarySearchTreeSearchAlgorithmRegistry(DataStructureAlgorithmRegistry):
    def __init__(self, data: list[dict] = [], value_getter: Callable[[dict], int] = lambda: 0):
        self._value_getter = value_getter
        self._data: BinarySearchTree[dict] = BinarySearchTree(
            data, value_getter=value_getter)

    def register(self):
        return DataStructureOption(
            key=INFO['BINARY_SEARCH_TREE']['key'],
            name=INFO['BINARY_SEARCH_TREE']['name'],
            description=INFO['BINARY_SEARCH_TREE']['description'],
            algorithms=[
                SearchAlgorithmOption(
                    key=INFO['BINARY_SEARCH_TREE']['search_algorithms']['DFS']['key'],
                    name=INFO['BINARY_SEARCH_TREE']['search_algorithms']['DFS']['name'],
                    needs_sort=INFO['BINARY_SEARCH_TREE']['search_algorithms']['DFS']['needs_sort'],
                    description=INFO['BINARY_SEARCH_TREE']['search_algorithms']['DFS']['description'],
                    time_complexity=INFO['BINARY_SEARCH_TREE']['search_algorithms']['DFS']['time_complexity'],
                    space_complexity=INFO['BINARY_SEARCH_TREE']['search_algorithms']['DFS']['space_complexity'],
                    time_complexity_level=INFO['BINARY_SEARCH_TREE']['search_algorithms']['DFS']['time_complexity_level'],
                    space_complexity_level=INFO['BINARY_SEARCH_TREE']['search_algorithms']['DFS']['space_complexity_level'],
                ),
                SearchAlgorithmOption(
                    key=INFO['BINARY_SEARCH_TREE']['search_algorithms']['BFS']['key'],
                    name=INFO['BINARY_SEARCH_TREE']['search_algorithms']['BFS']['name'],
                    needs_sort=INFO['BINARY_SEARCH_TREE']['search_algorithms']['BFS']['needs_sort'],
                    description=INFO['BINARY_SEARCH_TREE']['search_algorithms']['BFS']['description'],
                    time_complexity=INFO['BINARY_SEARCH_TREE']['search_algorithms']['BFS']['time_complexity'],
                    space_complexity=INFO['BINARY_SEARCH_TREE']['search_algorithms']['BFS']['space_complexity'],
                    time_complexity_level=INFO['BINARY_SEARCH_TREE']['search_algorithms']['BFS']['time_complexity_level'],
                    space_complexity_level=INFO['BINARY_SEARCH_TREE']['search_algorithms']['BFS']['space_complexity_level'],
                ),
            ]
        )

    def dfs(self, value: int):
        metrics_manager = AlgorithmMetricsManager()
        metrics_manager.start()

        metrics_manager.increment_operations(1)
        result = self._recursive_dfs(
            self._data.get_root(), value, metrics_manager)

        metrics_manager.end()

        return SearchResult(
            data_structure=INFO['BINARY_SEARCH_TREE']['name'],
            algorithm=INFO['BINARY_SEARCH_TREE']['search_algorithms']['DFS']['name'],
            needs_sort=INFO['BINARY_SEARCH_TREE']['search_algorithms']['DFS']['needs_sort'],
            time_complexity=INFO['BINARY_SEARCH_TREE']['search_algorithms']['DFS']['time_complexity'],
            time_complexity_level=INFO['BINARY_SEARCH_TREE']['search_algorithms']['DFS']['time_complexity_level'],
            space_complexity=INFO['BINARY_SEARCH_TREE']['search_algorithms']['DFS']['space_complexity'],
            space_complexity_level=INFO['BINARY_SEARCH_TREE']['search_algorithms']['DFS']['space_complexity_level'],
            item_count=self._data.size(),
            item_found=result,
            metrics=metrics_manager.get_metrics()
        )

    def _recursive_dfs(self, node: TreeNode[dict] | None, value: int, metrics_manager: AlgorithmMetricsManager) -> dict | None:
        metrics_manager.increment_iterations()
        metrics_manager.increment_operations(1)

        if node is None:
            return None

        node_data = node.get_data()
        node_value = self._value_getter(node_data)

        metrics_manager.increment_operations(3)

        if node_value == value:
            return node_data

        metrics_manager.increment_operations(1)

        if value < node_value:
            return self._recursive_dfs(node.get_left(), value, metrics_manager)
        else:
            return self._recursive_dfs(node.get_right(), value, metrics_manager)

    def bfs(self, value: int):
        metrics_manager = AlgorithmMetricsManager()
        metrics_manager.start()

        item_found = None
        root = self._data.get_root()

        metrics_manager.increment_operations(3)

        if root is not None:
            queue = Queue[TreeNode[dict]]()
            queue.enqueue(root)
            metrics_manager.increment_operations(2)

            while not queue.is_empty():
                metrics_manager.increment_iterations()

                current_node = queue.dequeue()
                metrics_manager.increment_operations(3)

                if current_node is None:
                    continue

                current_data = current_node.get_data()
                current_value = self._value_getter(current_data)
                metrics_manager.increment_operations(3)

                if current_value == value:
                    item_found = current_data
                    metrics_manager.increment_operations(1)
                    break

                left = current_node.get_left()
                metrics_manager.increment_operations(2)

                if left:
                    queue.enqueue(left)
                    metrics_manager.increment_operations(1)

                right = current_node.get_right()
                metrics_manager.increment_operations(2)

                if right:
                    queue.enqueue(right)
                    metrics_manager.increment_operations(1)

            metrics_manager.increment_operations(1)

        metrics_manager.end()

        return SearchResult(
            data_structure=INFO['BINARY_SEARCH_TREE']['name'],
            algorithm=INFO['BINARY_SEARCH_TREE']['search_algorithms']['BFS']['name'],
            needs_sort=INFO['BINARY_SEARCH_TREE']['search_algorithms']['BFS']['needs_sort'],
            time_complexity=INFO['BINARY_SEARCH_TREE']['search_algorithms']['BFS']['time_complexity'],
            time_complexity_level=INFO['BINARY_SEARCH_TREE']['search_algorithms']['BFS']['time_complexity_level'],
            space_complexity=INFO['BINARY_SEARCH_TREE']['search_algorithms']['BFS']['space_complexity'],
            space_complexity_level=INFO['BINARY_SEARCH_TREE']['search_algorithms']['BFS']['space_complexity_level'],
            item_count=self._data.size(),
            item_found=item_found,
            metrics=metrics_manager.get_metrics()
        )
