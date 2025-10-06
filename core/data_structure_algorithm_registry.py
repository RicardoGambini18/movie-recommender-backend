from typing import Callable
from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class AlgorithmOption():
    key: str
    name: str
    description: str
    space_complexity: str
    best_time_complexity: str
    worst_time_complexity: str
    average_time_complexity: str


@dataclass
class SearchAlgorithmOption(AlgorithmOption):
    needs_sort: bool


@dataclass
class DataStructureOption():
    key: str
    name: str
    description: str
    algorithms: list[AlgorithmOption]


class DataStructureAlgorithmRegistry(ABC):
    @abstractmethod
    def __init__(self, data: list[dict] = [], value_getter: Callable[[dict], int] = lambda: 0):
        pass

    @abstractmethod
    def register(self) -> DataStructureOption:
        pass


class DataStructureAlgorithmRegistryManager:
    def __init__(self, registries: list[DataStructureAlgorithmRegistry]):
        self.registries = registries
        self.validate()

    def validate(self):
        for registry in self.registries:
            if not issubclass(registry, DataStructureAlgorithmRegistry):
                raise ValueError(
                    f"{registry.__name__} no es una subclase de DataStructureAlgorithmRegistry")

            registry_instance = registry()
            option = registry_instance.register()

            for algorithm in option.algorithms:
                if not hasattr(registry_instance, algorithm.key):
                    raise ValueError(
                        f"El algoritmo '{algorithm.key}' en {registry.__name__} no tiene un método definido")

                method = getattr(registry_instance, algorithm.key)
                if not callable(method):
                    raise ValueError(
                        f"El algoritmo '{algorithm.key}' en {registry.__name__} no tiene un método válido")

    def get_options(self):
        options = []

        for registry in self.registries:
            registry_instance = registry()
            options.append(registry_instance.register())

        return options

    def get_algorithm_method(self, data_structure_key: str, algorithm_key: str, data: list[dict] = [], value_getter: Callable[[dict], int] = lambda: 0):
        for registry in self.registries:
            registry_instance = registry(data=data, value_getter=value_getter)
            option = registry_instance.register()

            if option.key != data_structure_key:
                continue

            for algorithm in option.algorithms:
                if algorithm.key != algorithm_key:
                    continue

                return getattr(registry_instance, algorithm.key)

        return None
