from inheritance.models.person import Person
from typing import Optional

class Student(Person):

    def __init__(
        self,
        first_name: Optional[str] | None = None, 
        last_name: Optional[str] | None = None, 
        email: Optional[str] | None = None,
        institution: str | None = None,
        math_grade: float | None = 0.00,
        language_grade: float | None = 0.00,
        history_grade: float | None = 0.00
    ):
        super().__init__(first_name, last_name, email)
        self.institution = institution
        self.math_grade = math_grade
        self.language_grade = language_grade
        self.history_grade = history_grade

    def speak(self):
        print("Estudiante hace una pregunta al profesor!")

    def write_black_board(self):
        print("Estudiante escribe en el pizarrón!")