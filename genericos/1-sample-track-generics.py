from genericos.truck import Truck
from genericos.animal import Animal, AnimalType
from genericos.machinery import Machinery
from genericos.car import Car

horses_transport: Truck[Animal] = Truck(capacity=5)

horses_transport.add(
    Animal(name="Peregrino", type=AnimalType.CABALLO.value),
).add(
    Animal(name="Grillo", type=AnimalType.BOVINO.value),
).add(
    Animal(name="Topocalma", type=AnimalType.CABALLO.value),
)


for animal in horses_transport:
    print(f"Animal: {animal.name}, Type: {animal.type}")

print("".center(50, "="))

machines_transport: Truck[Machinery] = Truck(capacity=3)

machines_transport.add(
    Machinery(type="Bulldozer"),
).add(
    Machinery(type="Grua Hidraulica"),
).add(
    Machinery(type="Perforadora"),
)


for machine in machines_transport:
    print(f"Machine: {machine.type}")


print("".center(50, "="))

cars_transport:Truck[Car]  = Truck(capacity=3)

cars_transport.add(
    Car(brand="Toyota"),
).add(
    Car(brand="Honda"),
).add(
    Car(brand="Ford"),  
)


for car in cars_transport:
    print(f"Car: {car.brand}")