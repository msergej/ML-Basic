          # Определение класса Plane
from HW05_12.base import Vehicle

class Plane(Vehicle):
    def __init__(self, weight: float = 0, fuel: float = 0, fuel_consumption: float = 0, max_cargo: float = 0):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self.cargo = 0

    def load_cargo(self, additional_cargo: float):
        if self.cargo + additional_cargo > self.max_cargo: raise CargoOverload("Превышена максимальная грузоподъемность")
        self.cargo += additional_cargo

    def remove_all_cargo(self) -> float:
        old_cargo = self.cargo
        self.cargo = 0
        return old_cargo
