from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel

class Vehicle(ABC):
    weight = 0
    started = False
    fuel = 0
    fuel_consumption = 0

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):

        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError()

    def move(self, distance):
        fuel_to_use = self.fuel_consumption * distance
        if self.fuel >= fuel_to_use:
            self.fuel -= fuel_to_use
        else:
            raise NotEnoughFuel()

