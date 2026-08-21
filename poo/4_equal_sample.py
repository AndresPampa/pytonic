from car import Car
from datetime import datetime, timezone


car1 = Car.full_spec(manufacturer='mazda',model='3', color=Car.COLOR_RED, cylinder=None, tank_capacity=34.00)
Car.license_plate_color = 'Red' #se puede cambiar el atributo estatico de la clase desde la instancia, solo desde la clase
print(car1)

car2 = Car.full_spec(manufacturer='mazda',model='3', color=Car.COLOR_PURPLE, cylinder=None, tank_capacity=34.00)
print(car2)

car3 = car1
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
print(car4)

speed_highway = Car.MAX_SPEED_HIGHWAY
print("speed_highway:",speed_highway)

Car.MAX_SPEED_HIGHWAY = 240
print("speed_highway:", Car.MAX_SPEED_HIGHWAY)
