from abstract_class.validator.validator import Validator
import re

class EmailValidator(Validator):

    # EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    EMAIL_REGEX = re.compile(r'^(.+)@(.+)$')

    def __init__(self):
        super().__init__('El campo %s debe ser un email valido')


    def is_valid(self, value: str | None) -> bool:
        if value is None:
            return True

        return bool(self.EMAIL_REGEX.match(value))