from math import sqrt, acos, cos, sin, pi, atan


class Vector:
    def __init__(self, x: float = 0, y: float = 0):
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

    def __mul__(self, value):
        if isinstance(value, Vector):
            return self.x * value.x + self.y * value.y
        return Vector(self.x * value, self.y * value)

    def __truediv__(self, value: float | int):
        return self.__mul__(1 / value)

    def __neg__(self):
        return self.__mul__(-1)

    def __pos__(self):
        return self

    def angle(self, vec=None) -> float:
        if vec == None:
            if abs(self.x) < 0.01:
                return pi / 2 if self.y >= 0 else 3 * pi / 2
            if self.x < 0:
                return atan(self.y / self.x) + pi
            return atan(self.y / self.x)
        if self.length() == 0 or vec.length() == 0:
            return pi / 2
        cos_alpha = (self.x * vec.x + self.y * vec.y) / (self.length() * vec.length())
        if cos_alpha > 1:
            return 0
        elif cos_alpha < -1:
            return pi
        return acos(cos_alpha)

    def turn_by_angle(self, angle: float):
        self.x, self.y = self.x * cos(angle) - self.y * sin(angle), self.x * sin(
            angle
        ) + self.y * cos(angle)
        return self
