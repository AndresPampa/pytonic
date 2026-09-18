from genericos.customer import Customer
from typing import Any, Iterable, List, TypeVar


T = TypeVar("T", bound=Customer) #T es un tipo generico que puede ser cualquier tipo que sea subclase de Customer
#T es un tipo generico que puede ser cualquier tipo
def from_array_to_list(items: Iterable[T]) -> List[T]:
    return list(items)


#set de clientes
customers: set[Customer] = {Customer(name = "Andres", lastname="Garcia"),}
customers.add(Customer(name= "John", lastname= "Doe"))

#set de numeros
numbers: set[int] = {1, 2, 3, 4, 5, Customer(name= "Andres", lastname="Garcia")}

customers_list = from_array_to_list(customers)
numbers_list = from_array_to_list(numbers)

for c in customers_list:
    print(c)

for n in numbers_list:
    print(n)
