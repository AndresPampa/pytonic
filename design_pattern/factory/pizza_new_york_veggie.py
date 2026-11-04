from .pizza_producto import PizzaProducto
from dataclasses import dataclass

@dataclass
class PizzaNewYorkVeggie(PizzaProducto):
    def __init__(self) -> None:
        super().__init__(
            _name="Pizza Veggetariana New York",
            _dough="Masa Integral Vegana",
            _sauce="salsa de tomate",
            _ingredients=[
                "queso vegano",
                "tomate",
                "aceitunas",
                "espinaca",
                "berenjenas",
            ],
        )

    def cook(self) -> None:
        print("Cocinando a 150 grados por 25 min")

    def cut(self) -> None:
        print("Cortando la pizza en rebanadas cuadradas")