from car import Car
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


print(car1.car_type)
print(car1.car_type.name)
print(car1.car_type.description)
print(car1.car_type.doors_count)

car_type = car1.car_type

match car_type:
    case CarType.SEDAN:
        print("El auto es un sedan")
    case CarType.SUV:
        print("El auto es un SUV")
    case CarType.PICKUP:
        print("El auto es un pickup")
    case CarType.COUPE:
        print("El auto es un coupe")
    case CarType.CONVERTIBLE:
        print("El auto es un convertible")
    case CarType.HATCHBACK:
        print("El auto es un hatchback")

for ct in CarType:
    print(f'{ct} => {ct.name} - {ct.description} - {ct.doors_count}')
    