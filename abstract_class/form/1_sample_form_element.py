from abstract_class.form.input_form import InputForm
from abstract_class.form.textarea_form import TextareaForm
from abstract_class.form.select_form import SelectForm, Option

username = InputForm(name='username')
password = InputForm(name='password', type_='password')
email = InputForm(name='email', type_='email')
age = InputForm(name='age', type_='number')
experience = TextareaForm(name='experience', rows=5, cols=9)
programing = SelectForm(name='programing')

programing.add_option(Option(value='1', name='Python').set_selected())
programing.add_option(Option(value='2', name='Java'))
programing.add_option(Option(value='3', name='JavaScript'))

username.set_value('John Doe')
password.set_value('john123')
email.set_value('john.doe@example.com')
age.set_value('25')
experience.set_value('I have 10 years of experience in programming')

elements = [username, password, email, age, experience, programing]
for element in elements:
    print(element.draw_thml())
    print('<br>')