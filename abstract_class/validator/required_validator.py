from abstract_class.validator.validator import Validator

class RequiredValidator(Validator):
    def __init__(self):
        super().__init__('El campo  %s es requerido')

    def is_valid(self, value: str) -> bool:
        return value is not None and len(value) > 0


