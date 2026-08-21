from typing import Final
from color import Color
from car_type import CarType

class Car:
    #Constructor: metodo que se ejecuta cuando se crea una instancia de la clase
    #Es un metodo de inicializacion
    #self es una referencia a la instancia de la clase
    #manufacturer, model, cylinder son los parametros del constructor y por lo tanto son atributos de la clase
    
    license_plate_color = 'Orange' #se define como atributo estatico fuera del constructor y por lo tanto es un atributo de la clase y no de la instancia, con doble guion bajo es privado
    #por lo tanto se puede acceder a el desde la clase y desde la instancia
    #se puede acceder a el desde la clase con Car.license_plate_color
    #se puede acceder a el desde la instancia con self.license_plate_color
    #__license_plate_color = 'Orange' # --> con doble guion bajo es privado con un guion bajo es protegido
    last_id = 0 #atributo estatico que se incrementa cada vez que se crea una instancia de la clase

    #static Final =Atributos constantes que no se pueden modificar
    MAX_SPEED_HIGHWAY: Final[int] = 120
    COLOR_RED:Final[str] = 'Red'
    COLOR_WHITE: Final[str] = 'Blanco'
    COLOR_GREY: Final[str] = 'Gris'
    COLOR_BLUE: Final[str] = 'Azul'
    COLOR_PURPLE: Final[str] = 'Purpura'

    def __init__(
        self, 
        manufacturer:str | None = None, 
        model:str | None=None, 
        color:str | Color | None='', 
        cylinder:float | None=0.00,
        tank_capacity:float | None=40.00
    ) -> None:
        #cuando comienza con un guion bajo es protegido y con doble guion bajo es privado
        self.__id = Car.last_id + 1
        Car.last_id = self.__id
        self.__manufacturer = manufacturer #Atributo privado va con doble guion bajo
        self.__model = model
        self.__color = color
        self.__cylinder = cylinder
        self._other = 'motor' #Atributo protegido va con un guion bajo
        self.__tank_capacity = 40
        self.__car_type: CarType | None = None

    #en python no existe la sobrecarga de constructores, por lo que no se puede tener diferentes constructores para diferentes tipos de datos
    #para eso se puede usar el patron de diseño factory
    #factory es un patron de diseño que se encarga de crear objetos de una clase
    #factory es un patron de diseño que se encarga de crear objetos de una clase
    @classmethod
    def empty(cls) -> str:
        return cls() #invocamos el constructor de la clase vacio

    @classmethod
    def basic(cls, manufacturer:str, model:str) -> str:
        return cls(manufacturer=manufacturer, model=model) #invocamos el constructor de la clase con solo dos parametros

    @classmethod
    def with_color(cls, manufacturer:str, model:str, color:str) -> str:
        return cls(manufacturer=manufacturer, model=model, color=color) #invocamos el constructor de la clase con solo tres parametros
    
    @classmethod
    def only_color(cls, manufacturer:str, color:str) -> str:
        return cls(manufacturer=manufacturer, model=None, color=color)
    
    @classmethod
    def only_cylinder(cls, manufacturer:str, cylinder:float) -> str:
        return cls(manufacturer=manufacturer, model=None, color=None, cylinder=cylinder)
    
    @classmethod
    def only_tank_capacity(cls, manufacturer:str, tank_capacity:float) -> str:
        return cls(manufacturer=manufacturer, model=None, color=None, cylinder=None, tank_capacity=tank_capacity)
    
    @classmethod
    def full_spec(cls, manufacturer:str, model:str, color:str, cylinder:float, tank_capacity:float) -> str:
        return cls(manufacturer=manufacturer, model=model, color=color, cylinder=cylinder, tank_capacity=tank_capacity)
    
    @classmethod
    def set_license_plate_color(cls, color:str) -> None:
        cls.license_plate_color = color
    
    @classmethod
    def get_license_plate_color(cls) -> str:
        return cls.license_plate_color



    def __eq__(self, other) -> bool:
        #recibe la misma instancia y la compara con otra
        if self is other:
            return True

        if not isinstance(other, Car):
            return False
        return self.__model == other.__model \
                and self.__manufacturer == other.__manufacturer \
                and self.__color == other.__color \
                and self.__cylinder == other.__cylinder \
                and self.__tank_capacity == other.__tank_capacity \
                and self._other == other._other
    

    
    #----------------------------------------------#
    #Metodos getters y setters
    # def get_model(self) -> str:
    #     return self.__model

    # def set_model(self, model: str) -> None:
    #     self.__model = model
    #----------------------------------------------#

    def get_color(self) -> str:
        return self.__color

    def set_color(self, color: str) -> None:
        self.__color = color

    # def get_cylinder(self) -> float:
    #     return self.__cylinder

    # def set_cylinder(self, cylinder: float) -> None:
    #     self.__cylinder = cylinder

    #Propiedad cylinder y setter --> otro metodo para acceder a los atributos privados
    @property
    def cylinder(self) -> float:
        return self.__cylinder
    
    @cylinder.setter
    def cylinder(self, cylinder: float) -> None:
        self.__cylinder = cylinder

    @property
    def model(self) -> str:
        return self.__model
    
    @model.setter
    def model(self, model: str) -> None:
        self.__model = model

    @property
    def car_type(self) -> CarType:
        return self.__car_type
    
    @car_type.setter
    def car_type(self, car_type: CarType) -> None:
        self.__car_type = car_type

    def details(self) -> str:
        return f"manufacturer: {self.__manufacturer}, model: {self.__model}, color: {self.__color}, cylinder: {self.__cylinder} other: {self._other} license_plate_color: {Car.license_plate_color} id: {self.__id}"

    #metodo para acelerar el auto
    def accelerate(self, rpm:int, speed:int) -> str:
        return f'El auto {self.__manufacturer} acelera a {rpm} y a {speed} km/h'

    def brake(self) -> str:
        return f'El auto {self.__manufacturer} {self.__model} frenando!!'
    
    def accelerate_n_brake(self, rpm:int, speed:int) -> str:
        accelerating = self.accelerate(rpm, speed)
        braking = self.brake()
        return f'{accelerating} and {braking}'
    
    def calculate_consumption(self, km:int, fuel_percentage:float) -> float:
        if isinstance(fuel_percentage, int):
            fuel_percentage = fuel_percentage/100.00
        return km/(fuel_percentage * self.__tank_capacity)


    #metodo str --> se ejecuta cuando se imprime el objeto
    def __str__(self) -> str:
        return f"manufacturer: {self.__manufacturer}, model: {self.__model}, color: {self.__color}, cylinder: {self.__cylinder} other: {self._other} tank_capacity: {self.__tank_capacity} license_plate_color: {Car.license_plate_color} id: {self.__id} car_type: {self.__car_type}"

    #metodo repr --> se ejecuta cuando se imprime el objeto en consola y sirve para debugging
    def __repr__(self) -> str:
        return f"manufacturer: {self.__manufacturer}, model: {self.__model}, color: {self.__color}, cylinder: {self.__cylinder} other: {self._other} tank_capacity: {self.__tank_capacity} license_plate_color: {Car.license_plate_color} id: {self.__id} car_type: {self.__car_type}"
    
