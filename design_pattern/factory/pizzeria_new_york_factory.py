from .pizza_new_york_italian import PizzaNewYorkItalian
from .pizza_new_york_pepperoni import PizzaNewYorkPepperoni
from .pizza_new_york_veggie import PizzaNewYorkVeggie
from .pizza_producto import PizzaProducto
from .pizzeria_zone_abstract_factory import PizzeriaZoneAbstractFactory


class PizzeriaNewYorkFactory(PizzeriaZoneAbstractFactory):
    def create_pizza(self, tipo: str) -> PizzaProducto | None:
        match tipo:
            case "vegetariano":
                return PizzaNewYorkVeggie()
            case "pepperoni":
                return PizzaNewYorkPepperoni()
            case "italian":
                return PizzaNewYorkItalian()
            case "cheese":
                return PizzaNewYorkItalian()
            case _:
                return None