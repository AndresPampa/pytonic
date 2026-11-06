from abc import ABC, abstractmethod
from .pizza_producto import PizzaProducto


class PizzeriaZoneAbstractFactory(ABC):

    def order_pizza(self, tipo: str) -> PizzaProducto | None:
        pizza = self.create_pizza(tipo)
        if pizza is None:
            return None 
        print(f"------------ | fabricando la pizza {pizza.name} | ------------")
        pizza.prepare()
        pizza.cook()
        pizza.cut()
        pizza.pack()
        return pizza

    @abstractmethod
    def create_pizza(self, tipo: str) -> PizzaProducto | None:
        pass