from dataclasses import dataclass

@dataclass(frozen=True, order=True)
class Customer:
    name: str
    lastname: str


    # #otra forma es implementar el hash
    # def __hash__(self):
    #     return hash((self.name, self.lastname))