from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    started = False
    weight = 1400
    fuel = 45
    fuel_consumption = 8

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError("Насяяяяльникеее!! Топлива нетунамана!")

    def move(self, distance):
        if distance * self.fuel_consumption > self.fuel:
            raise NotEnoughFuel("Насяяяяльникеее!! Топлива не хватаетнамана!")
        else:
            self.fuel -= distance * self.fuel_consumption
