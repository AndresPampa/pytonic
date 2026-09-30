from dataclasses import dataclass, field

@dataclass
class Truck:
    capacity: int
    # __items: list = field(default_factory=list, init=False, repr=False)

    def __post_init__(self):
        self.__items = []

    def add(self, item) -> None:
        if len(self.__items) >= self.capacity:
            raise ValueError("Truck is full")
        else:
            self.__items.append(item)

        return self