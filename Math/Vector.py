from math import sqrt, acos, cos, sin, pi, atan
from typing import overload


class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def length(self) -> float:
        return sqrt(self.x * self.x + self.y * self.y)

    def __repr__(self):
        return f"({self.x}; {self.y})"

    def __add__(self, vec):
        return Vector(self.x + vec.x, self.y + vec.y)

    def __sub__(self, vec):
        return Vector(self.x - vec.x, self.y - vec.y)

    def __mul__(self, value: float | int):
        return Vector(self.x * value, self.y * value)

    def __truediv__(self, value: float | int):
        return self.__mul__(1 / value)

    def __neg__(self):
        return self.__mul__(-1)

    def __pos__(self):
        return self

    def angle(self) -> float:
        if self.x == 0:
            return pi / 2
        return atan(self.y / self.x)

    def angle(self, vec=None) -> float:
        if vec == None:
            if self.x == 0:
                return pi / 2
            return atan(self.y / self.x)
        if self.length() == 0 or vec.length() == 0:
            return pi / 2
        return acos((self.x * vec.x + self.y * vec.y) / (self.length() * vec.length()))

    def turn_by_angle(self, angle: float):
        self.x, self.y = self.x * cos(angle) - self.y * sin(angle), self.x * sin(
            angle
        ) + self.y * cos(angle)
        return self
