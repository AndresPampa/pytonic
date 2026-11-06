from abc import ABC, abstractmethod


class Formattable(ABC):
    @abstractmethod
    def format(self) -> str:
        pass


class Text(Formattable):
    def __init__(self, content: str) -> None:
        self._content = content

    def format(self) -> str:
        return self._content


class TextDecorator(Formattable, ABC):
    def __init__(self, text: Formattable) -> None:
        self._text = text

    @abstractmethod
    def format(self) -> str:
        pass


class UppercaseDecorator(TextDecorator):
    def format(self) -> str:
        return self._text.format().upper()


class ReverseDecorator(TextDecorator):
    def format(self) -> str:
        return self._text.format()[::-1]


class ReplaceSpaceDecorator(TextDecorator):
    def format(self) -> str:
        return self._text.format().replace(" ", "_")


class UnderLineDecorator(TextDecorator):
    def format(self) -> str:
        return "".join(character + "\u0332" for character in self._text.format())


if __name__ == "__main__":
    text: Formattable = Text("Hola que tal Andres!")

    text = UppercaseDecorator(text)
    text = ReverseDecorator(text)
    text = ReplaceSpaceDecorator(text)
    text = UnderLineDecorator(text)

    text2: Formattable = Text("Tu Vieja En Tanga!")
    text2 = UppercaseDecorator(
        ReverseDecorator(
            ReplaceSpaceDecorator(
                UnderLineDecorator(text2)
            )
        )
    )

    print(text.format())
    print(text2.format())
