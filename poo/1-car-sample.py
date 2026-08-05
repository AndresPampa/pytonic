# class Car:
#     #Constructor: metodo que se ejecuta cuando se crea una instancia de la clase
#     #Es un metodo de inicializacion
#     #self es una referencia a la instancia de la clase
#     #manufacturer, model, cylinder son los parametros del constructor y por lo tanto son atributos de la clase
#     def __init__(self, manufacturer=None, model=None, color='', cylinder=0.00) -> None:
#         #cuando comienza con un guion bajo es protegido y con doble guion bajo es privado
#         self.__manufacturer = manufacturer #Atributo privado va con doble guion bajo
#         self.__model = model
#         self.__color = color
#         self.__cylinder = cylinder
#         self._other = 'motor' #Atributo protegido va con un guion bajo
    
#     #Metodos getters y setters
#     # def get_model(self) -> str:
#     #     return self.__model

#     # def set_model(self, model: str) -> None:
#     #     self.__model = model

#     def get_color(self) -> str:
#         return self.__color

#     def set_color(self, color: str) -> None:
#         self.__color = color

#     # def get_cylinder(self) -> float:
#     #     return self.__cylinder

#     # def set_cylinder(self, cylinder: float) -> None:
#     #     self.__cylinder = cylinder

#     #Propiedad cylinder y setter --> otro metodo para acceder a los atributos privados
#     @property
#     def cylinder(self) -> float:
#         return self.__cylinder
    
#     @cylinder.setter
#     def cylinder(self, cylinder: float) -> None:
#         self.__cylinder = cylinder

#     @property
#     def model(self) -> str:
#         return self.__model
    
#     @model.setter
#     def model(self, model: str) -> None:
#         self.__model = model

#     def details(self) -> str:
#         return f"manufacturer: {self.__manufacturer}, model: {self.__model}, color: {self.__color}, cylinder: {self.__cylinder} other: {self._other}"

#     #metodo str --> se ejecuta cuando se imprime el objeto
#     def __str__(self) -> str:
#         return f"manufacturer: {self.__manufacturer}, model: {self.__model}, color: {self.__color}, cylinder: {self.__cylinder} other: {self._other}"

#     #metodo repr --> se ejecuta cuando se imprime el objeto en consola y sirve para debugging
#     def __repr__(self) -> str:
#         return f"manufacturer: {self.__manufacturer}, model: {self.__model}, color: {self.__color}, cylinder: {self.__cylinder} other: {self._other}"
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


