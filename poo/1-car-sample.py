from car import Car

if __name__ == "__main__":

    # no se usa el operador new en python
    car = Car(manufacturer="Toyota", model="Corolla", cylinder=1.6)
    # print("car.manufacturer: ", car.manufacturer)
    # print("car.model: ", car.model)
    # print("car.cylinder: ", car.cylinder)

    #Una vez que se crea el objeto, no se puede modificar el valor de los atributos privados
    # car.manufacturer = "Ford"
    # car.model = "Mustang"
    # car.cylinder = 4.0
    # print("car.manufacturer: ", car.manufacturer)
    # print("car.model: ", car.model)
    # print("car.cylinder: ", car.cylinder)
    print("detalles", car.details())
    print("str", car)
    print("repr", repr(car))

    #creando una instancia distinta de la calse
    mazda = Car(manufacturer="Mazda", model="CX-5", cylinder=2.0)
    # mazda.manufacturer = "Mazda"
    # mazda.model = "CX-5"
    # mazda.cylinder = 2.0
    # print("mazda.manufacturer: ", mazda.manufacturer)
    # print("mazda.model: ", mazda.model)
    # print("mazda.cylinder: ", mazda.cylinder)

    print("detalles", mazda.details())
    # print("car.manufacturer: ", mazda.get_model())
    # print("car.manufacturer: ", mazda.get_cylinder())
    print("car.manufacturer: ", mazda.get_color())

    mazda.cylinder = 4.0
    mazda.model = "CX-9"
    print("mazda.cylinder: ", mazda.cylinder)
    print("mazda.model: ", mazda.model)

    mazda._other = 'otro'
    print("mazda._other: ", mazda._other) #si se imprime un atributo protegido, se puede acceder a el pero no se debe hacer
    print("str", mazda)
    print("repr", repr(mazda))


    #metodos de instancia
    # mazda.accelerate(rpm=3000, speed=100)
    # mazda.brake()
    print("mazda.accelerate: ", mazda.accelerate(rpm=3000, speed=100))
    print("mazda.brake: ", mazda.brake())
    print("mazda.accelerate_n_brake: ", mazda.accelerate_n_brake(rpm=5000, speed=150))

    #esto seria polimorfismo ya que se puede usar el mismo metodo para diferentes tipos de datos como int y float
    #un mismo metodo puede tener diferentes implementaciones para diferentes tipos de datos
    print("mazda.calculate_consumption: ", mazda.calculate_consumption(km=300, fuel_percentage=0.6))
    print("mazda.calculate_consumption: ", mazda.calculate_consumption(km=300, fuel_percentage=60))


