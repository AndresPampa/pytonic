from abstract_class.validator.validator import Validator

class NumberValidator(Validator):

    def __init__(self):
        super().__init__('El campo %s debe ser un numero')

    
    def is_valid(self, value: str) -> bool:
        if value is None:
            return False
        try:
            int(value)
            return True
        except (ValueError, TypeError):
            return False

