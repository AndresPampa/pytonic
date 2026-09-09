from abstract_class.form.form_element import FormElement

class InputForm(FormElement):

    def __init__(
        self,
        name:str,
        value: str = None,
        type_ : str = 'text'
    ):
        super().__init__(name, value)
        self._type_ = type_

    def draw_thml(self) -> str:
        return f'<input type="{self._type_}" name="{self._name}" value="{self._value}">'

