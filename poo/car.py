class Car:
    #Constructor: metodo que se ejecuta cuando se crea una instancia de la clase
    #Es un metodo de inicializacion
    #self es una referencia a la instancia de la clase
    #manufacturer, model, cylinder son los parametros del constructor y por lo tanto son atributos de la clase
    def __init__(self, manufacturer=None, model=None, color='', cylinder=0.00) -> None:
        #cuando comienza con un guion bajo es protegido y con doble guion bajo es privado
        self.__manufacturer = manufacturer #Atributo privado va con doble guion bajo
        self.__model = model
        self.__color = color
        self.__cylinder = cylinder
        self._other = 'motor' #Atributo protegido va con un guion bajo
    
    #Metodos getters y setters
    # def get_model(self) -> str:
    #     return self.__model

    # def set_model(self, model: str) -> None:
    #     self.__model = model

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

    def details(self) -> str:
        return f"manufacturer: {self.__manufacturer}, model: {self.__model}, color: {self.__color}, cylinder: {self.__cylinder} other: {self._other}"

    #metodo str --> se ejecuta cuando se imprime el objeto
    def __str__(self) -> str:
        return f"manufacturer: {self.__manufacturer}, model: {self.__model}, color: {self.__color}, cylinder: {self.__cylinder} other: {self._other}"

    #metodo repr --> se ejecuta cuando se imprime el objeto en consola y sirve para debugging
    def __repr__(self) -> str:
        return f"manufacturer: {self.__manufacturer}, model: {self.__model}, color: {self.__color}, cylinder: {self.__cylinder} other: {self._other}"