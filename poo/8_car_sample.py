from car import Car
from engine import Engine
from fuel_tank import FuelTank
from person import Person
from wheel import Wheel

if __name__ == "__main__":

    # no se usa el operador new en python
    car = Car(
        manufacturer="Toyota", 
        model="Corolla", 
        engine=Engine(cylinder=1.6), 
        fuel_tank=FuelTank(capacity=40), 
        driver=Person(first_name="Juan", last_name="Perez"), 
        wheels=[Wheel(manufacturer="Michelin", rim_size=16, width=20), Wheel(manufacturer="Michelin", rim_size=16, width=20)]
    )

    # print("detalles", car.details())
    # print("str", car)
    # print("repr", repr(car))

    #creando una instancia distinta de la calse
    mazda = Car(
        manufacturer="Mazda", 
        model="CX-5", 
        engine=Engine(cylinder=2.0), 
        fuel_tank=FuelTank(capacity=40), 
        driver=Person(first_name="Cacho", last_name="Castaña"), 
        wheels=[Wheel(manufacturer="Michelin", rim_size=16, width=20)]*4
    )

    mazda.add_wheel(Wheel(manufacturer="Michelin", rim_size=16, width=20))
    # for _ in range(5):
    #     mazda.add_wheel(Wheel(manufacturer="Michelin", rim_size=16, width=20))

    # print("detalles", mazda.details())
    # print("car.color: ", mazda.get_color())

    mazda.engine = Engine(cylinder=4.0)
    mazda.model = "CX-9"
    # print("mazda.engine: ", mazda.engine)
    # print("mazda.model: ", mazda.model)

    susuki = Car(manufacturer="Suzuki", 
        model="Vitara", 
        engine=Engine(cylinder=1.6), 
        fuel_tank=FuelTank(capacity=40), 
        driver=Person(first_name="John", last_name="Salchichon"), 
        wheels=[Wheel(manufacturer="Michelin", rim_size=16, width=20)]*4
    )
    # print("detalles", susuki.details())

    audi = Car(
        manufacturer="Audi", 
        model="A4", 
        engine=Engine(cylinder=2.0), 
        fuel_tank=FuelTank(capacity=40), 
        driver=Person(first_name="Jane", last_name="Doe"), 
        wheels=[Wheel(manufacturer="Michelin", rim_size=16, width=20)]*4
    )
    # print("detalles", audi.details())

    cars = [car, mazda, susuki, audi]
    sorted_cars = sorted(cars)
    
    for car in sorted_cars:
        print(car)