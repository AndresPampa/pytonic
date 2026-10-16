from dataclasses import dataclass, field

@dataclass
class Component:
    name: str
    #El field() sirve para especificar un valor predeterminado para el atributo children, que es una lista vacía. Esto permite que cada instancia de Component tenga su propia lista de hijos, evitando problemas de referencia compartida entre instancias.
    children: list['Component'] = field(default_factory=list)
    level: int = 0

    def add_children(self, c:'Component')-> 'Component':
        # c.level = self.level + 1
        self.children.append(c)
        return self

    def has_children(self) -> bool:
        return len(self.children) > 0

    # def print_tree(self) -> None:
    #     for child in self.children:
    #         print(f"Nivel{self.level}: Hijo {child}")