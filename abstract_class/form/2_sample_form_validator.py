from abstract_class.form.input_form import InputForm
from abstract_class.form.textarea_form import TextareaForm
from abstract_class.form.select_form import SelectForm, Option

from abstract_class.validator.required_validator import RequiredValidator
from abstract_class.validator.email_validator import EmailValidator
from abstract_class.validator.number_validator import NumberValidator
from abstract_class.validator.length_validator import LengthValidator
from abstract_class.validator.not_none_validator import NotNoneValidator

username = InputForm(name='username')
username.add_validator(RequiredValidator())

password = InputForm(name='password', type_='password')
password.add_validator(RequiredValidator())
password.add_validator(LengthValidator(min_length=6, max_length=12))

email = InputForm(name='email', type_='email')
email.add_validator(RequiredValidator())
email.add_validator(EmailValidator())

age = InputForm(name='age', type_='number')
age.set_value('25')
age.add_validator(NumberValidator())

experience = TextareaForm(name='experience', rows=5, cols=9)
programing = SelectForm(name='programing')
programing.add_validator(NotNoneValidator())

programing.add_option(Option(value='1', name='Python').set_selected())
programing.add_option(Option(value='2', name='Java'))
programing.add_option(Option(value='3', name='JavaScript'))

username.set_value('John Doe')
password.set_value('john123')
email.set_value('john.doe@example.com')
# email.set_value('....')
age.set_value('28')
experience.set_value('I have 10 years of experience in programming')


# ------------------------------------------------------------------------ #
elements = [username, password, email, age, experience, programing]

for element in elements:
    print(element.draw_thml())
    print('<br>')

print("# VALIDATORS #")
for e in elements:
    if not e.is_valid():
        for err in e.errors:
            print(err)