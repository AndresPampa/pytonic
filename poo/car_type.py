from enum import Enum

class CarType(Enum):
    
    SEDAN: tuple[str, str, int] = ('Sedan', 'Auto Mediano', 4)
    SUV: tuple[str, str, int] = ('SUV', 'Auto Grande', 4)
    PICKUP: tuple[str, str, int] = ('Pickup', 'Auto Grande', 4)
    COUPE: tuple[str, str, int] = ('Coupe', 'Auto Mediano', 2)
    CONVERTIBLE: tuple[str, str, int] = ('Convertible', 'Auto Mediano', 2)
    HATCHBACK: tuple[str, str, int] = ('Hatchback', 'Auto Mediano', 4)
    WAGON: tuple[str, str, int] = ('Wagon', 'Auto Grande', 4)
    MINIVAN: tuple[str, str, int] = ('Minivan', 'Auto Grande', 4)
    FAMILY: tuple[str, str, int] = ('Family', 'Auto Grande', 4)
    SPORTS: tuple[str, str, int] = ('Sports', 'Auto Mediano', 2)
    ELECTRIC: tuple[str, str, int] = ('Electric', 'Auto Mediano', 2)
    HYBRID: tuple[str, str, int] = ('Hybrid', 'Auto Mediano', 2)

    def __init__(self, name: str, description: str, doors_count: int) -> None:
        self.__name = name
        self.__description = description
        self.__doors_count = doors_count

    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def description(self) -> str:
        return self.__description
    
    @property
    def doors_count(self) -> int:
        return self.__doors_count
    
    def __str__(self) -> str:
        return f"{self.__name} - {self.__description} - {self.__doors_count} puertas"
    