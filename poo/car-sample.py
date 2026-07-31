class Car:
    #Constructor: metodo que se ejecuta cuando se crea una instancia de la clase
    #Es un metodo de inicializacion
    #self es una referencia a la instancia de la clase
    #manufacturer, model, cylinder son los parametros del constructor y por lo tanto son atributos de la clase
    def __init__(self, manufacturer=None, model=None, cylinder=0.00) -> None:
        self.manufacturer = manufacturer
        self.model = model
        self.cylinder = cylinder



car = Car(manufacturer="Toyota", model="Corolla", cylinder=1.6)
print(car.manufacturer)
print(car.model)
print(car.cylinder)

car.manufacturer = "Ford"
car.model = "Mustang"
car.cylinder = 4.0
print(car.manufacturer)
print(car.model)
print(car.cylinder)