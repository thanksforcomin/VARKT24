from Vector import Vector
from Constants import dt


class Rocket(Vector):
    def __init__(self, x: float, y: float, m: float, fuel: float, dm: float):
        self.x = x
        self.y = y
        self.m = m
        self.fuel = fuel
        self.dm = dm

    def update_mass(self) -> int:
        self.fuel -= self.dm * dt
        if self.fuel < 0:
            self.fuel = 0
            return -1
        return 0

    def addVector(self, v: Vector):
        self.x += v.x
        self.y += v.y

    def get_mass(self) -> float:
        return self.m + self.fuel