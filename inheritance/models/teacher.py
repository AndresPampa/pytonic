from inheritance.models.person import Person
from typing import Optional
from inheritance.models.subjects import Subjects

class Teacher(Person):

    def __init__(
        self, 
        first_name: Optional[str] | None = None, 
        last_name: Optional[str] | None = None, 
        email: Optional[str] | None = None,
        subject: Optional[Subjects] | None = None
    ):
        super().__init__(first_name, last_name, email)
        self.subject = subject
    
    def greet(self) -> str:
        # return super().greet()
        return f"{super().greet()}, Soy un profesor"

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
    