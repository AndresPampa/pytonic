from abstract_class.validator.validator import Validator

class NotNoneValidator(Validator):

    def __init__(self):
        super().__init__('El campo %s no puede ser None')

    def is_valid(self, value: str | None) -> bool:
        return value is not None

