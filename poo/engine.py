from enum import Enum

class EngineType(Enum):
    DIESEL = 'Diesel'
    GASOLINE = 'Gasoline'
    ELECTRIC = 'Electric'
    HYBRID = 'Hybrid'

class Engine:

    def __init__(self, cylinder:float, engine_type:EngineType = None) -> None:
        self.cylinder = cylinder
        self.engine_type = engine_type

    def __str__(self) -> str:
        return f"cylinder={self.cylinder}, type={self.engine_type}"