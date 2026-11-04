from .pizza_producto import PizzaProducto
from dataclasses import dataclass

@dataclass
class PizzaNewYorkPepperoni(PizzaProducto):
    def __init__(self) -> None:
        super().__init__(
            _name="Pizza Pepperoni New York",
            _dough="Masa delgada a la piedra",
            _sauce="salsa de tomate",
            _ingredients=["queso mozzarella", "extra pepperoni", "aceitunas"],
        )

    def cook(self) -> None:
        print("Cocinando por 40 min a 90 grados °C")

    def cut(self) -> None:
        print("Cortando la pizza en triangulos")