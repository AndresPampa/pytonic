class Wheel:

    def __init__(self, manufacturer:str, rim_size:int, width:float) -> None:
        self.manufacturer = manufacturer
        self.rim_size = rim_size
        self.width = width

    def __str__(self) -> str:
        return f'{self.manufacturer} {self.rim_size} {self.width}'

    def __repr__(self) -> str:
        return self.__str__()
    
    