from collections.abc import Iterable, Iterator
from dataclasses import dataclass#, field
from typing import Generic, List, TypeVar

from genericos.animal import Animal
from genericos.car import Car
from genericos.machinery import Machinery


T = TypeVar('T', bound=[Animal, Car, Machinery])  # Generic type variable for items in the Truck
@dataclass
# class Truck(Iterable):
class Truck(Generic[T], Iterable[T]):

    capacity: int
    # __items: list[T] = field(default_factory=list, init=False, repr=False)

    def __post_init__(self):
        self.__items: List[T] = []

    def add(self, item: T) -> 'Truck':
        if len(self.__items) >= self.capacity:
            raise ValueError("Truck is full")
        else:
            self.__items.append(item)

        return self

    def __iter__(self) -> Iterator[T]:
        return iter(self.__items)

    
    def __len__(self) -> int:
        return len(self.__items)

    