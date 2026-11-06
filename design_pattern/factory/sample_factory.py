from design_pattern.factory.pizzeria_new_york_factory import PizzeriaNewYorkFactory
from design_pattern.factory.pizzeria_california_factory import PizzeriaCaliforniaFactory
from design_pattern.factory.pizza_producto import PizzaProducto

ny = PizzeriaNewYorkFactory()
california = PizzeriaCaliforniaFactory()

pizza: PizzaProducto = california.order_pizza("cheese")
print(f'Buce ordena la {pizza.name}')


pizza: PizzaProducto = ny.order_pizza("pepperoni")
print(f'Buce ordena la {pizza.name}')