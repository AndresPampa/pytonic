from abc import ABC, abstractmethod
from dataclasses import dataclass, field


@dataclass
class PizzaProducto(ABC):
    _name: str
    _dough: str
    _sauce: str
    _ingredients: list[str] = field(default_factory=list)

    @property
    def name(self) -> str:
        return self._name

    def prepare(self) -> None:
        print(
            f"Preparando {self._name}: masa={self._dough}, "
            f"sauce={self.sauce}, ingredientes={self._ingredients}"
        )

    @abstractmethod
    def cook(self) -> None:
        pass

    @abstractmethod
    def cut(self) -> None:
        pass

    def pack(self) -> None:
        print(f"Empacando {self._name}")