from .pizza_producto import PizzaProducto
from dataclasses import dataclass

@dataclass
class PizzaCaliforniaVeggie(PizzaProducto):
    def __init__(self) -> None:
        super().__init__(
            _name="pizza california veggie",
            _dough="masa delgada light",
            _sauce="bbq light",
            _ingredients=[
                "queso mozzarella",
                "aceitunas",
                "espinacas",
                "cebolla",
                "berenjenas",
                "choclo",
            ],
        )

    def cook(self) -> None:
        print("Cocinando por 25 min a 180 grados °C")

    def cut(self) -> None:
        print("Cortando la pizza en rebanadas rectangulares")