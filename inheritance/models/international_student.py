from inheritance.models.student import Student
from typing import Optional

class InternationalStudent(Student):

    def __init__(
        self,
        first_name: Optional[str] | None = None, 
        last_name: Optional[str] | None = None, 
        email: Optional[str] | None = None,
        institution: str | None = None,
        math_grade: float | None = 0.00,
        language_grade: float | None = 0.00,
        history_grade: float | None = 0.00,
        country: str | None = None,
        foreing_language_grade: float | None = None
    ):
        super().__init__(
            first_name, 
            last_name, 
            email, 
            institution, 
            math_grade, 
            language_grade, 
            history_grade
        )
        self.country = country
        self.foreing_language_grade = foreing_language_grade

    def greet(self) -> str:
        # return super().greet()
        return f"{super().greet()}, Soy un estudiante internacional"

    def calcular_average_grade(self) -> float:
        base_average = super().calcular_average_grade()*3
        return (base_average + self.foreing_language_grade) / 4
    
    def __str__(self) -> str:
        return super().__str__() + f'\n Pais: {self.country} \n Promedio de lenguaje extranjero: {self.foreing_language_grade}'