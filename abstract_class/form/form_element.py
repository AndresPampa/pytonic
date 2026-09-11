from abc import ABC, abstractmethod
from abstract_class.validator.validator import Validator
from typing import List

class FormElement(ABC):

    def __init__(
        self,
        name:str,
        value: str | None = None
    ):
        self._name = name
        self._value = value
        self._validators: List[Validator] = []
        self._errors: List[str] = []

    def add_validator(self, validator: Validator):
        self._validators.append(validator)
    
    @property
    def errors(self) -> List[str]:
        return self._errors

    # @errors.setter
    
    def set_value(self, value: str):
        self._value = value
    
    def is_valid(self) -> bool:
        self._errors.clear() # limpia la lista de errores
        for v in self._validators:
            if not v.is_valid(self._value):
                self._errors.append(v.message % self._name)
        return len(self._errors) == 0

    @abstractmethod
    def draw_thml(self) -> str:
        pass