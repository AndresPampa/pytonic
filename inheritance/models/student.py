from inheritance.models.person import Person

class Student(Person):

    def __init__(self):
        super().__init__()
        self.institution = None
        self.math_grade = None
        self.language = None
        self.history = None

    def speak(self):
        print("Estudiante hace una pregunta al profesor!")

    def write_black_board(self):
        print("Estudiante escribe en el pizarrón!")