from math import sqrt
from math import acos


class Vector:
    def __init__(self):
        self.__init__(0, 0)

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def length(self) -> float:
        return sqrt(self.x * self.x + self.y + self.y)

    def __repr__(self):
        return f"({self.x}; {self.y})"

    def __add__(self, vec):
        return Vector(self.x + vec.x, self.y + vec.y)

    def __sub__(self, vec):
        return Vector(self.x - vec.x, self.y - vec.y)

    def __mul__(self, value: float):
        return Vector(self.x * value, self.y * value)

    def angle(self, vec) -> float:
        return acos((self.x * vec.x + self.y * vec.y) / (self.length() * vec.length()))


v1 = Vector(1, 0)
v2 = Vector(1, 6)

print(v1.angle(v2))
