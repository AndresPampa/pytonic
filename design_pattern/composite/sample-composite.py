from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    @abstractmethod
    def show(self, level: int = 0) -> None:
        pass

    @abstractmethod
    def search(self, name: str) -> bool:
        pass


class File(Component):
    def __init__(self, name: str) -> None:
        self.name = name

    def show(self, level: int = 0) -> None:
        indent = "\t" * level
        print(f"{indent}- {self.name}")

    def search(self, name: str) -> bool:
        return self.name == name


class Directory(Component):
    def __init__(self, name: str) -> None:
        self.name = name
        self.children: List[Component] = []

    def add(self, component: Component) -> None:
        self.children.append(component)

    def show(self, level: int = 0) -> None:
        indent = "\t" * level
        print(f"{indent}+ {self.name}/")
        for child in self.children:
            child.show(level + 1)

    def search(self, name: str) -> bool:
        return self.name == name or any(
            child.search(name) for child in self.children
        )


if __name__ == "__main__":
    documentos = Directory("Documentos")

    trabajo = Directory("Trabajo")
    trabajo.add(File("informe.docx"))
    trabajo.add(File("presentacion.pptx"))

    fotos = Directory("Fotos")
    fotos.add(File("vacaciones.jpg"))
    fotos.add(File("familia.png"))

    documentos.add(trabajo)
    documentos.add(fotos)
    documentos.add(File("notas.txt"))

    documentos.show()

    for name in ("informe.docx", "Fotos", "musica.mp3"):
        print(f"¿Se encontró '{name}'? {documentos.search(name)}")