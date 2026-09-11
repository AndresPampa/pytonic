from abc import ABC, abstractmethod


class Validator(ABC):

    def __init__(self, message: str):
        self._message = message

    @property
    def message(self) -> str:
        return self._message


    @abstractmethod
    def is_valid(self, value: str) -> bool:
        ... #literal especial de python que se llama ellipsis, que significa que el metodo no tiene implementacion
    

