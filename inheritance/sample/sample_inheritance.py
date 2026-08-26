from inheritance.models.student import Student
from inheritance.models.teacher import Teacher
from inheritance.models.subjects import Subjects
from inheritance.models.person import Person
from typing import cast, List

student: Person = Student()
student.first_name = "Pampa"
student.last_name = "Bhattacharya"
student.email = "pampa@gmail.com"
student.institution = "UTN"

alumno = cast(Student, student)
alumno.institution = "UNCuyo"

teacher = Teacher()
teacher.first_name = "Maria"
teacher.last_name = "Garcia"
teacher.email = "maria@gmail.com"
teacher.subject = Subjects.MATH.value

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

student.speak()
alumno.speak()
alumno.write_black_board()

print(isinstance(student, Student))
print(isinstance(alumno, Student))
print(isinstance(teacher, Person))
print(isinstance(teacher, Student))

persons: List[Person] = [student, teacher]
for person in persons:
    if isinstance(person, Student):
        person.write_black_board()
    else:
        print("No es un estudiante")