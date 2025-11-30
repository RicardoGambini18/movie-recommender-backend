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


class Vector(DataStructure[T]):
    def _build_from_list(self, data: list[T]) -> None:
        self._items: list[T] = data.copy()

    def to_list(self) -> list[T]:
        return self._items.copy()

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)

    def copy(self) -> 'Vector[T]':
        vector_copy = Vector[T]([])
        vector_copy._items = self._items.copy()
        return vector_copy

    def get_item(self, index: int) -> T:
        return self._items[index]

    def set_item(self, index: int, value: T) -> None:
        self._items[index] = value

    def get_slice(self, start: int, end: int) -> 'Vector[T]':
        vector_slice = Vector[T]([])
        vector_slice._items = self._items[start:end].copy()
        return vector_slice

    def append(self, item: T) -> None:
        self._items.append(item)

    def extend(self, other: 'Vector[T]') -> None:
        self._items.extend(other._items)


class Node(Generic[T]):
    def __init__(self, data: T):
        self.data = data
        self.prev: Node[T] | None = None
        self.next: Node[T] | None = None

    def get_data(self) -> T:
        return self.data

    def set_data(self, data: T) -> None:
        self.data = data

    def get_prev(self) -> 'Node[T] | None':
        return self.prev

    def set_prev(self, node: 'Node[T] | None') -> None:
        self.prev = node

    def get_next(self) -> 'Node[T] | None':
        return self.next

    def set_next(self, node: 'Node[T] | None') -> None:
        self.next = node


class DoublyLinkedList(DataStructure[T]):
    def _build_from_list(self, data: list[T]) -> None:
        self.head: Node[T] | None = None
        self.tail: Node[T] | None = None
        self._size = 0
        for item in data:
            self.append(item)

    def append(self, item: T) -> None:
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_prev(self.tail)
            self.tail.set_next(new_node)
            self.tail = new_node
        self._size += 1

    def to_list(self) -> list[T]:
        result = []
        current = self.head
        while current:
            result.append(current.get_data())
            current = current.get_next()
        return result

    def is_empty(self) -> bool:
        return self.head is None

    def size(self) -> int:
        return self._size

    def copy(self) -> 'DoublyLinkedList[T]':
        return DoublyLinkedList(self.to_list())

    def get_head(self) -> Node[T] | None:
        return self.head

    def set_head(self, node: Node[T] | None) -> None:
        self.head = node

    def get_tail(self) -> Node[T] | None:
        return self.tail

    def set_tail(self, node: Node[T] | None) -> None:
        self.tail = node
