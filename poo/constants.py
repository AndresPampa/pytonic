from dataclasses import dataclass

@dataclass(frozen=True)
class Constants():
    MAX_SPEED_HIGHWAY: int = 120
    COLOR_RED:str = 'Red'
    COLOR_WHITE: str = 'Blanco'
    COLOR_GREY: str = 'Gris'
    COLOR_BLUE: str = 'Azul'
    COLOR_PURPLE: str = 'Purpura'