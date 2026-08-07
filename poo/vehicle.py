class Vehicle:

    def __init__(self, *args) -> None:
        self.manufacturer = None
        self.model = None
        self.color = None
        self.cylinder = None
        self.tank_capacity = None

        args_names = ['manufacturer', 'model', 'color', 'cylinder', 'tank_capacity']
        for name, value in zip(args_names, args):
            setattr(self, name, value)

        # total = len(args)
        # if total == 0:
        #     pass
        # elif total == 1:
        #     self.manufacturer = args
        # elif total == 2:
        #     self.manufacturer, self.model = args
        # elif total == 3:
        #     self.manufacturer, self.model, self.color = args
        # elif total == 4:
        #     self.manufacturer, self.model, self.color, self.cylinder = args
        # elif total == 5:
        #     self.manufacturer, self.model, self.color, self.cylinder, self.tank_capacity = args
        # else:
        #     raise ValueError("Invalid number of arguments")

    #metodo para acelerar el auto
    def accelerate(self, rpm:int, speed:int) -> str:
        return f'El auto {self.manufacturer} acelera a {rpm} y a {speed} km/h'

    def brake(self) -> str:
        return f'El auto {self.manufacturer} {self.model} frenando!!'
    
    def accelerate_n_brake(self, rpm:int, speed:int) -> str:
        accelerating = self.accelerate(rpm, speed)
        braking = self.brake()
        return f'{accelerating} and {braking}'
    
    def calculate_consumption(self, km:int, fuel_percentage:float) -> float:
        if isinstance(fuel_percentage, int):
            fuel_percentage = fuel_percentage/100.00
        return km/(fuel_percentage * self.tank_capacity)


    #metodo str --> se ejecuta cuando se imprime el objeto
    def __str__(self) -> str:
        return f"manufacturer: {self.manufacturer}, model: {self.model}, color: {self.color}, cylinder: {self.cylinder} tank_capacity: {self.tank_capacity}"

    #metodo repr --> se ejecuta cuando se imprime el objeto en consola y sirve para debugging
    def __repr__(self) -> str:
        return f"manufacturer: {self.manufacturer}, model: {self.model}, color: {self.color}, cylinder: {self.cylinder} tank_capacity: {self.tank_capacity}"