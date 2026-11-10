from abc import ABC, abstractmethod
from decimal import Decimal


class Observer(ABC):
    @abstractmethod
    def update(self, company: "Company") -> None:
        pass


class Company:
    def __init__(self, name: str, price: Decimal) -> None:
        self.name = name
        self.price = price
        self.observers: list[Observer] = []

    def subscribe(self, observer: Observer) -> None:
        self.observers.append(observer)

    def unsubscribe(self, observer: Observer) -> None:
        self.observers.remove(observer)

    def set_price(self, new_price: Decimal) -> None:
        if new_price == self.price:
            return

        self.price = new_price
        for observer in self.observers.copy():
            observer.update(self)


class Investor(Observer):
    def __init__(self, name: str) -> None:
        self.name = name

    def update(self, company: Company) -> None:
        print(
            f"{self.name}: {company.name} cambió su cotización a "
            f"{format_price(company.price)}."
        )


def format_price(price: Decimal) -> str:
    integer_part, _, decimal_part = f"{price:,.2f}".partition(".")
    return f"ARS {integer_part.replace(',', '.')},{decimal_part}"


def main() -> None:
    ypf = Company("YPF", Decimal("28000.00"))
    galicia = Company("Grupo Financiero Galicia", Decimal("9500.00"))
    pampa = Company("Pampa Energía", Decimal("3200.00"))

    ana = Investor("Ana")
    bruno = Investor("Bruno")
    carla = Investor("Carla")

    ypf.subscribe(ana)
    ypf.subscribe(bruno)
    galicia.subscribe(bruno)
    galicia.subscribe(carla)
    pampa.subscribe(ana)
    pampa.subscribe(carla)

    print("Actualizaciones de cotizaciones en la bolsa argentina:")
    ypf.set_price(Decimal("28500.00"))
    galicia.set_price(Decimal("9700.00"))
    pampa.set_price(Decimal("3150.00"))
    print("Si el precio no cambia, no se envía ninguna notificación.")
    ypf.set_price(Decimal("28500.00"))


if __name__ == "__main__":
    main()