from abstract_class.form.form_element import FormElement

class TextareaForm(FormElement):

    def __init__(
        self,
        name:str,
        value: str = None,
        rows: int = 4,
        cols: int = 6
    ):
        super().__init__(name, value)
        self.rows = rows
        self.cols = cols


    def draw_thml(self) -> str:
        return (f'<textarea name="{self._name}" rows="{self.rows}" cols="{self.cols}">{self._value}</textarea>')

        