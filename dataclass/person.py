from dataclasses import dataclass
from typing import ClassVar
# class Person:

#     def __init__(self, name:str, lastname:str):
#         self.name =name 
#         self.lastname = lastname
    

#     def __repr__(self):
#         return f"Person(name={self.name}, lastname={self.lastname})"

#     # compara 2 objetos por instancia y no por valor
#     def __eq__(self, other):
#         return self.name == other.name and self.lastname == other.lastname

@dataclass(frozen=True, order=True)
#frozen: no se puede mutar el objeto
#order: ordena los objetos por el nombre y el apellido
class Person:
    name: str
    lastname: str
    #estatico para la clase, no para cada instancia
    count: ClassVar[int] = 0
    


if __name__ == "__main__":

    person1 = Person("Juan", "Perez")
    person2 = Person("John", "Doe")
    person3 = Person(name="John", lastname="Doe")

    # person1.name = "Juan" # error de mutacion

    print(person1)
    print(person2)
    print(person1 == person2)
    print(person2 == person3)

    Person.count += 2

    print(person1.count)
    print(person2.count)
    print(person3.count)