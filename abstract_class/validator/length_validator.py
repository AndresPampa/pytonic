from abstract_class.validator.validator import Validator
import sys

class LengthValidator(Validator):

    def __init__(self, min_length: int = 0, max_length: int = sys.maxsize):
        super().__init__('El campo %s debe tener un MIN de %d y MAX de %d caracteres')
        self._min_length = min_length
        self._max_length = max_length

    
    def is_valid(self, value: str | None) -> bool:
        self._message = self._message % ('%s', self._min_length, self._max_length)

        if value is None:
            return True
        return self._min_length <= len(value) <= self._max_length