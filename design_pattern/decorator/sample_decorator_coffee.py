from abc import ABC, abstractmethod


class Configurable(ABC):
    """Componente: define la interfaz común del café y sus decoradores."""

    @abstractmethod
    def get_base_price(self) -> float:
        """Devuelve el precio del café con sus agregados."""
        pass

    @abstractmethod
    def get_ingredients(self) -> list[str]:
        """Devuelve los ingredientes del café con sus agregados."""
        pass


class Coffee(Configurable):
    """Componente concreto: representa el café base sin decoradores."""

    def __init__(self, base_price: float, ingredients: list[str]) -> None:
        self._base_price = base_price
        self._ingredients = ingredients

    def get_base_price(self) -> float:
        return self._base_price

    def get_ingredients(self) -> list[str]:
        return self._ingredients.copy()


class CoffeeDcorator(Configurable, ABC):
    """Decorador base: envuelve un café y conserva la interfaz Configurable."""

    def __init__(self, coffee: Configurable) -> None:
        self._coffee = coffee

    # @abstractmethod
    # def get_base_price(self) -> float: ...
    #     pass
    def get_base_price(self) -> float: ... 
    #los 3 puntos indican que es un método abstracto, pero no es necesario poner el decorador @abstractmethod, ya que la clase CoffeeDecorator hereda de Configurable, que ya tiene ese método como abstracto.
    """Cada decorador concreto define cómo cambia el precio."""

    @abstractmethod
    def get_ingredients(self) -> list[str]:
        """Cada decorador concreto define qué ingrediente agrega."""
        pass


class WithCreamDecorator(CoffeeDcorator):
    """Decorador concreto que agrega crema y su costo al café envuelto."""

    def get_base_price(self) -> float:
        return self._coffee.get_base_price() + 0.50

    def get_ingredients(self) -> list[str]:
        return self._coffee.get_ingredients() + ["crema"]


class WithMilkDecorator(CoffeeDcorator):
    """Decorador concreto que agrega leche y su costo al café envuelto."""

    def get_base_price(self) -> float:
        return self._coffee.get_base_price() + 0.40

    def get_ingredients(self) -> list[str]:
        return self._coffee.get_ingredients() + ["leche"]


class WithChocolateDecorator(CoffeeDcorator):
    """Decorador concreto que agrega chocolate y su costo al café envuelto."""

    def get_base_price(self) -> float:
        return self._coffee.get_base_price() + 0.70

    def get_ingredients(self) -> list[str]:
        return self._coffee.get_ingredients() + ["chocolate"]


def show_coffee(name: str, coffee: Configurable) -> None:
    """Muestra el precio y los ingredientes de cualquier café configurable."""
    ingredients = ", ".join(coffee.get_ingredients())
    print(f"{name}: ${coffee.get_base_price():.2f}")
    print(f"  Ingredientes: {ingredients}")


if __name__ == "__main__":
    # Cada decorador envuelve el café anterior y suma su ingrediente y precio.
    mocha: Configurable = WithChocolateDecorator(
        WithMilkDecorator(Coffee(2.00, ["café espresso"]))
    )
    cappuccino: Configurable = WithCreamDecorator(
        WithMilkDecorator(Coffee(2.00, ["café espresso"]))
    )
    espresso: Configurable = Coffee(2.00, ["café espresso"])

    show_coffee("Café mocha", mocha)
    show_coffee("Café capuchino", cappuccino)
    show_coffee("Café expresso", espresso)
    