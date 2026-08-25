from typing import Final, Optional, List
from color import Color
from car_type import CarType
from engine import Engine
from fuel_tank import FuelTank
from person import Person
from wheel import Wheel

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
        engine:Optional[Engine] | None = None,
        fuel_tank:Optional[FuelTank] | None = None,
        driver: Optional[Person] | None = None,
        wheels: List[Wheel] = []
    ) -> None:
        #cuando comienza con un guion bajo es protegido y con doble guion bajo es privado
        self.__id = Car.last_id + 1
        Car.last_id = self.__id
        self.__manufacturer = manufacturer #Atributo privado va con doble guion bajo
        self.__model = model
        self.__color = color
        # self.__cylinder = cylinder
        self.__engine = engine
        self._other = 'motor' #Atributo protegido va con un guion bajo
        # self.__tank_capacity = 40
        self.__fuel_tank = fuel_tank
        self.__car_type: Optional[CarType] | None = None
        self.__driver = driver
        self.__wheels = wheels

    #en python no existe la sobrecarga de constructores, por lo que no se puede tener diferentes constructores para diferentes tipos de datos
    #para eso se puede usar el patron de diseño factory
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
    def only_engine(cls, manufacturer:str, engine:Optional[Engine] | None = None) -> str:
        return cls(manufacturer=manufacturer, model=None, color=None, engine=engine)
    
    @classmethod
    def only_fuel_tank(cls, manufacturer:str, fuel_tank:Optional[FuelTank] | None = None) -> str:
        return cls(manufacturer=manufacturer, model=None, color=None, engine=None, fuel_tank=fuel_tank)
    
    @classmethod
    def full_spec(cls, manufacturer:str, model:str, color:str, engine:Optional[Engine] | None = None, fuel_tank:Optional[FuelTank] | None = None) -> str:
        return cls(manufacturer=manufacturer, model=model, color=color, engine=engine, fuel_tank=fuel_tank)
    
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
                and self.__engine == other.__engine \
                and self.__fuel_tank == other.__fuel_tank \
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
    def engine(self) -> float:
        return self.__engine
    
    @engine.setter
    def engine(self, engine: Engine) -> None:
        self.__engine = engine

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

    @property
    def fuel_tank(self) -> FuelTank:
        return self.__fuel_tank
    
    @fuel_tank.setter
    def fuel_tank(self, fuel_tank: FuelTank) -> None:
        self.__fuel_tank = fuel_tank

    @property
    def driver(self) -> Person:
        return self.__driver
    
    @driver.setter
    def driver(self, driver: Person) -> None:
        self.__driver = driver

    @property
    def wheels(self) -> List[Wheel]:
        return self.__wheels
    
    @wheels.setter
    def wheels(self, wheels: List[Wheel]) -> None:
        self.__wheels = wheels

    def add_wheel(self, wheel: Wheel) -> 'Car': #se usa el tipo 'Car' para indicar que el metodo retorna una instancia de la clase Car
        self.__wheels.append(wheel)
        return self #Esto se llama chaining y es una tecnica de programacion que permite encadenar metodos de una clase
        #esto es util para encadenar metodos de una clase y para hacer mas legible el codigo
        #por ejemplo: car.add_wheel(Wheel(manufacturer="Michelin", rim_size=16, width=20)).add_wheel(Wheel(manufacturer="Michelin", rim_size=16, width=20)).add_wheel(Wheel(manufacturer="Michelin", rim_size=16, width=20))
        #esto es util para encadenar metodos de una clase y para hacer mas legible el codigo

    def details(self) -> str:
        return f"manufacturer: {self.__manufacturer}, model: {self.__model}, color: {self.__color}, engine: {self.__engine} fuel_tank: {self.__fuel_tank} other: {self._other} license_plate_color: {Car.license_plate_color} id: {self.__id} driver: {self.__driver} wheels: {self.__wheels}"

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
        return km/(fuel_percentage * self.__fuel_tank.capacity)


    #metodo str --> se ejecuta cuando se imprime el objeto
    def __str__(self) -> str:
        return f"manufacturer: {self.__manufacturer}, model: {self.__model}, color: {self.__color}, engine: {self.__engine} other: {self._other} fuel_tank: {self.__fuel_tank} license_plate_color: {Car.license_plate_color} id: {self.__id} car_type: {self.__car_type} driver: {self.__driver} wheels: {self.__wheels}"

    #metodo repr --> se ejecuta cuando se imprime el objeto en consola y sirve para debugging
    def __repr__(self) -> str:
        return f"manufacturer: {self.__manufacturer}, model: {self.__model}, color: {self.__color}, engine: {self.__engine} other: {self._other} fuel_tank: {self.__fuel_tank} license_plate_color: {Car.license_plate_color} id: {self.__id} car_type: {self.__car_type} driver: {self.__driver} wheels: {self.__wheels}"
    
    def __lt__(self, other) -> bool:
        return self.__manufacturer  < other.__manufacturer #se compara el atributo manufacturer de la clase Car