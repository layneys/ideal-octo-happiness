"""
создайте класс `Plane`, наследник `Vehicle`
"""

from homework_02.car import Car
from homework_02.exceptions import CargoOverload


class Plane(Car):
    cargo = 0
    max_cargo = 0

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super(Plane, self).__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, cargo_weight):
        if self.cargo + cargo_weight <= self.max_cargo:
            self.cargo += cargo_weight
        else:
            raise CargoOverload()

    def remove_all_cargo(self):
        cargo_sum = self.cargo
        self.cargo = 0
        return cargo_sum