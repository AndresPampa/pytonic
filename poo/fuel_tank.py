class FuelTank:

    def __init__(self, capacity:int = 40) -> None:
        self.capacity = capacity

    def __str__(self) -> str:
        return f"capacity={self.capacity}"