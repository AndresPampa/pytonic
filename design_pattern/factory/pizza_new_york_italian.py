from dataclasses import dataclass
from .pizza_producto import PizzaProducto


@dataclass
class PizzaNewYorkItalian(PizzaProducto):
    def __init__(self) -> None:
        super().__init__(
            _name="pizza italiana new york",
            _dough="gruesa",
            _sauce="salsa de tomate italiano con carne",
            _ingredients=[
                "queso mozzarella",
                "aceitunas",
                "jamon",
                "champignones",
            ],
        )

    def cook(self) -> None:
        print("Cocinando por 10 minutos a 200 grados")

    def cut(self) -> None:
        print("Cortando la pizza en pequeños triangulos")