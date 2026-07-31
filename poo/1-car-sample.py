class Car:
    #Constructor: metodo que se ejecuta cuando se crea una instancia de la clase
    #Es un metodo de inicializacion
    #self es una referencia a la instancia de la clase
    #manufacturer, model, cylinder son los parametros del constructor y por lo tanto son atributos de la clase
    def __init__(self, manufacturer=None, model=None, color='', cylinder=0.00) -> None:
        self.manufacturer = manufacturer
        self.model = model
        self.color = color
        self.cylinder = cylinder

    def details(self) -> str:
        return f"manufacturer: {self.manufacturer}, model: {self.model}, color: {self.color}, cylinder: {self.cylinder}"


# no se usa el operador new en python
car = Car(manufacturer="Toyota", model="Corolla", cylinder=1.6)
print("car.manufacturer: ", car.manufacturer)
print("car.model: ", car.model)
print("car.cylinder: ", car.cylinder)

car.manufacturer = "Ford"
car.model = "Mustang"
car.cylinder = 4.0
print("car.manufacturer: ", car.manufacturer)
print("car.model: ", car.model)
print("car.cylinder: ", car.cylinder)
print("detalles", car.details())

#creando una instancia distinta de la calse
mazda = Car()
mazda.manufacturer = "Mazda"
mazda.model = "CX-5"
mazda.cylinder = 2.0
print("mazda.manufacturer: ", mazda.manufacturer)
print("mazda.model: ", mazda.model)
print("mazda.cylinder: ", mazda.cylinder)

print("detalles", mazda.details())