from inheritance.models.student import Student
from inheritance.models.teacher import Teacher
from inheritance.models.subjects import Subjects
from inheritance.models.person import Person
from typing import cast, List

student: Person = Student(
    first_name="Pampa", 
    last_name="Bhattacharya", 
    email="pampa@gmail.com", 
    institution = "UTN"
)
student.history_grade = 8.5 #SETTER

teacher = Teacher(
    first_name="Maria", 
    last_name="Garcia", 
    email="maria@gmail.com", 
    subject=Subjects.MATH.value
)


print(
    student.first_name, 
    student.last_name, 
    student.email, 
    student.institution,
)
print("".center(50, "-"))
print(
    teacher.first_name, 
    teacher.last_name, 
    teacher.email,
    teacher.subject
)
print("".center(50, "-"))

persons: List[Person] = [student, teacher]
for person in persons:
    if isinstance(person, Student):
        person.write_black_board()
    else:
        print("No es un estudiante")