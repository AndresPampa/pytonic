from .pizza_california_cheese import PizzaCaliforniaCheese
from .pizza_california_veggie import PizzaCaliforniaVeggie
from .pizza_producto import PizzaProducto
from .pizzeria_zone_abstract_factory import PizzeriaZoneAbstractFactory


class PizzeriaCaliforniaFactory(PizzeriaZoneAbstractFactory):
    def create_pizza(self, tipo: str) -> PizzaProducto | None:
        match tipo.lower():
            case "vegetariano":
                return PizzaCaliforniaVeggie()
            case "cheese":
                return PizzaCaliforniaCheese()
            case _:
                return None
