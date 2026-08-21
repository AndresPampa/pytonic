from car import Car
from datetime import datetime, timezone
from constants import Constants
from color import Color
from car_type import CarType

Car.set_license_plate_color(Constants.COLOR_RED)
print(Car.get_license_plate_color())

Car.set_license_plate_color(Color.RED.value)
print(Car.get_license_plate_color())

car1 = Car.full_spec(manufacturer='mazda',model='3', color=Color.YELLOW.value, cylinder=None, tank_capacity=34.00)
car1.car_type = CarType.SEDAN
Car.license_plate_color = 'Red' #se puede cambiar el atributo estatico de la clase desde la instancia, solo desde la clase
print(car1)

car2 = Car.full_spec(manufacturer='mazda',model='3', color=Car.COLOR_PURPLE, cylinder=None, tank_capacity=34.00)
print(car2)

car3 = car1
car3.car_type = CarType.SUV
date_now = datetime.now(tz=timezone.utc)
print(date_now)

print(car1 == car2) #== compara si son iguales, es decir, si tienen los mismos valores
print(car1 is car2) #is compara si son el mismo objeto, es decir, si son la misma instancia
print(car1 is car3) #TRUE
print(car1 == date_now) #False

#los atributos estaticos no le pertenecen a la instancia, sino a la clase, por lo que no se pueden comparar con el metodo __eq__

car1.set_license_plate_color('Blue')
print(car1.get_license_plate_color())

car4 = Car.full_spec(manufacturer='mazda',model='4', color=Car.COLOR_WHITE, cylinder=None, tank_capacity=65.00)
car4.car_type = CarType.PICKUP
print(car4)

speed_highway = Constants.MAX_SPEED_HIGHWAY
print("speed_highway:",speed_highway)

Constants.MAX_SPEED_HIGHWAY = 240 #ESTO NO SE DEBE HACER, YA QUE ES UNA CONSTANTE
print("speed_highway:", Constants.MAX_SPEED_HIGHWAY)

#Los enums son iterables
# for color in Color:
#     print(color)
#     print(color.value)

print(car1.car_type)
print(car1.car_type.name)
print(car1.car_type.description)
print(car1.car_type.doors_count)