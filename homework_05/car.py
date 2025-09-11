          # Определение класса Car
from HW05_12.base import Vehicle
from HW05_12.engine import Engine

class Car(Vehicle):
    def __init__(self, weight: float = 0, fuel: float = 0, fuel_consumption: float = 0):
        super().__init__(weight, fuel, fuel_consumption)
        self.engine = None

    def set_engine(self, engine: Engine):
        self.engine = engine
