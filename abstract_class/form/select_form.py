from abstract_class.form.form_element import FormElement

class Option:
    def __init__(
        self,
        value: str = None,
        name: str = None, 
    ):
        self.value = value
        self.name = name
        self.selected = False
    
    def set_selected(self) -> None:
        self.selected = True
        return self

class SelectForm(FormElement):

    def __init__(
        self,
        name:str,
        value: str = None,
        options: list[Option] | None = None
    ):
        super().__init__(name, value)
        self.options = options if options is not None else []

    def add_option(self, value: Option) -> None:
        self.options.append(value)


    def draw_thml(self) -> str:
        html = f'<select name="{self._name}">'

        for option in self.options:
            select_attr = ''
            if option.selected:
                select_attr = 'selected'
                self._value = option.value 
            html += f'<option value="{option.value}" {select_attr}>{option.name}</option>'

        html += '</select>'
        return html