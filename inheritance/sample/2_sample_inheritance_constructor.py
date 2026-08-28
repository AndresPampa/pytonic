from inheritance.models.student import Student
from inheritance.models.teacher import Teacher
from inheritance.models.subjects import Subjects
from inheritance.models.person import Person
from typing import cast, List
from inheritance.models.international_student import InternationalStudent

def print_person(person:Person):
    print('Imprimiendo datos en comun del tipo Persona'.center(50, "-"))
    print(f'person.first_name: {person.first_name} - person.last_name: {person.last_name} - person.email: {person.email}')
    print("".center(50, "-"))
    if isinstance(person, Student):
        print('Imprimiendo datos del tipo Estudiante'.center(50, "-"))
        print(f'Institucion: {person.institution}')
        print(f'Promedio de matematicas: {person.math_grade}')
        print(f'Promedio de lenguaje: {person.language_grade}')
        print(f'Promedio de historia: {person.history_grade}')
        print("".center(50, "-"))

        if isinstance(person, InternationalStudent):
            print('Imprimiendo datos del tipo Estudiante Internacional'.center(50, "-"))
            print(f'Pais: {person.country}')
            print(f'Promedio de lenguaje extranjero: {person.foreing_language_grade}')
            print("".center(50, "-"))

    elif isinstance(person, Teacher):
        print('Imprimiendo datos del tipo Profesor'.center(50, "-"))
        print(f'Materia: {person.subject}')
        print("".center(50, "-"))
    else:
        print('No es un estudiante, profesor o estudiante internacional')

student: Person = Student(
    first_name="Pampa", 
    last_name="Bhattacharya", 
    email="pampa@gmail.com", 
    institution = "UTN"
)
student.history_grade = 8.5 #SETTER
student.language_grade = 6.0
student.math_grade = 7.0

teacher = Teacher(
    first_name="Maria", 
    last_name="Garcia", 
    email="maria@gmail.com", 
    subject=Subjects.MATH.value
)


international_student:Person = InternationalStudent(
    first_name="joane",
    last_name="dalmo",
    email="joane@mail.com",
    institution="universite de france",
    math_grade=8.0,
    language_grade=7.0,
    history_grade=6.0,
    country="francia",
    foreing_language_grade=7.56
)


# print(
#     student.first_name, 
#     student.last_name, 
#     student.email, 
#     student.institution,
# )
# print("".center(50, "-"))
# print(
#     teacher.first_name, 
#     teacher.last_name,  
#     teacher.email,
#     teacher.subject
# )
# print("".center(50, "-"))

# print_person(student)
# print_person(international_student)
# print_person(teacher)

persons: List[Person] = [student, teacher, international_student]
for person in persons:
    if isinstance(person, Student):
        person.write_black_board()
        print_person(person)
    else:
        print("No es un estudiante")
        print_person(person)