from abc import ABC, abstractmethod

class FormElement(ABC):

    def __init__(
        self,
        name:str,
        value: str | None = None
    ):
        self._name = name
        self._value = value


    def set_value(self, value: str):
        self._value = value
    

    @abstractmethod
    def draw_thml(self) -> str:
        pass