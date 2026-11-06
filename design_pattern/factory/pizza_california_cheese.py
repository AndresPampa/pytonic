from dataclasses import dataclass
from .pizza_producto import PizzaProducto


@dataclass
class PizzaCaliforniaCheese(PizzaProducto):
    def __init__(self) -> None:
        super().__init__(
            _name="pizza california queso",
            _dough="a la piedra delgada",
            _sauce="Salsa de tomate con rucula",
            _ingredients=[
                "Extra queso Mozzarella",
                "Cebolla",
                "queso azul",
            ],
        )

    def cook(self) -> None:
        print("cocinando a 35 min a 100 grados")

    def cut(self) -> None:
        print("cortando la pizza en pequeños triangulos")