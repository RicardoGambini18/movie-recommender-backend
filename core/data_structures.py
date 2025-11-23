from typing import TypeVar, Generic
from abc import ABC, abstractmethod

T = TypeVar('T')


class DataStructure(ABC, Generic[T]):
    def __init__(self, data: list[T] = []):
        self._build_from_list(data)

    @abstractmethod
    def _build_from_list(self, data: list[T]) -> None:
        pass

    @abstractmethod
    def to_list(self) -> list[T]:
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def size(self) -> int:
        pass

    @abstractmethod
    def copy(self) -> 'DataStructure[T]':
        pass


class Stack(DataStructure[T]):
    def _build_from_list(self, data: list[T]) -> None:
        self._items: list[T] = []
        for item in data:
            self.push(item)

    def to_list(self) -> list[T]:
        result = []
        pila_auxiliar: list[T] = []

        while not self.is_empty():
            item = self.pop()
            result.append(item)
            pila_auxiliar.append(item)

        pila_auxiliar.reverse()
        for item in pila_auxiliar:
            self.push(item)

        result.reverse()
        return result

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T | None:
        if self.is_empty():
            return None
        return self._items.pop()

    def peek(self) -> T | None:
        if self.is_empty():
            return None
        return self._items[-1]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)

    def copy(self) -> 'Stack[T]':
        stack_copy = Stack[T]([])
        stack_copy._items = self._items.copy()
        return stack_copy


class Queue(DataStructure[T]):
    def _build_from_list(self, data: list[T]) -> None:
        self._items: list[T] = []
        for item in data:
            self.enqueue(item)

    def to_list(self) -> list[T]:
        result = []
        cola_auxiliar: list[T] = []

        queue_size = self.size()
        for _ in range(queue_size):
            item = self.dequeue()
            result.append(item)
            cola_auxiliar.append(item)

        for item in cola_auxiliar:
            self.enqueue(item)

        return result

    def enqueue(self, item: T) -> None:
        self._items.append(item)

    def dequeue(self) -> T | None:
        if self.is_empty():
            return None
        return self._items.pop(0)

    def peek(self) -> T | None:
        if self.is_empty():
            return None
        return self._items[0]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)

    def copy(self) -> 'Queue[T]':
        queue_copy = Queue[T]([])
        queue_copy._items = self._items.copy()
        return queue_copy
