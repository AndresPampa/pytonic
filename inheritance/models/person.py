from typing import Optional


class Person:

    def __init__(
        self, 
        first_name: Optional[str] | None = None, 
        last_name: Optional[str] | None = None, 
        email: Optional[str] | None = None
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
    
    # @property
    # def first_name(self):
    #     return self._first_name
    
    # @property
    # def last_name(self):
    #     return self._last_name
    
    # @property
    # def email(self):
    #     return self._email
    
    # @first_name.setter
    # def first_name(self, first_name):
    #     self._first_name = first_name
    
    # @last_name.setter
    # def last_name(self, last_name):
    #     self._last_name = last_name
    
    # @email.setter
    # def email(self, email):
    #     self._email = email

    def speak(self) -> str:
        return "Persona conversa un tema"

    def greet(self) -> str:
        return "Hola, como estas?"