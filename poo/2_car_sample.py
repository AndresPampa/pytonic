from car import Car
from vehicle import Vehicle

car = Car()
print(car)

car1 = Car.with_color(manufacturer='mazda',model='3', color='gris')
print(car1)
car2 = Car(manufacturer='Citroen',model='C3', color='rojo', cylinder=1.6)
print(car2)
car3 = Car(manufacturer='Subaru',model='Legacy', color='azul', cylinder=3.0, tank_capacity=50.00)
print(car3)
car4 = Car.only_tank_capacity(manufacturer='mazda', tank_capacity=34.00)
print(car4)
car5 = Car(manufacturer='mazda',model='3', color=None, cylinder=None, tank_capacity=34.00)
print(car5)
car6 = Car.empty()
print(car6)
