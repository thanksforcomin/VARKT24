from Vector import Vector
from math import cos, sin, pi, sqrt
from Constants import *


class Satellite(Vector):
    def __init__(
        self, distance: float, angle: float, radius: float, mass: float, SOI: float
    ):
        super().__init__(distance * cos(angle), distance * sin(angle))
        self.radius = radius
        self.mass = mass
        self.SOI = SOI
        self.force = Vector()
        self.velocity = Vector(sqrt(GRAVITY_PARAMETER / distance), 0).turn_by_angle(
            angle - pi / 2
        )
        self.acceleration = Vector()
        self.GRAVITY_PARAMETER = self.mass * 6.67430 / 10**11

    def gravity_kerbin(self) -> Vector:
        return -Vector(
            GRAVITY_PARAMETER * self.mass / self.length() ** 2, 0
        ).turn_by_angle(self.angle())

    def update_position(self):
        self.force = self.gravity_kerbin()
        self.acceleration = self.force / self.mass
        self.velocity += self.acceleration * dt
        self.x += self.velocity.x * dt
        self.y += self.velocity.y * dt

    def position_in(self, time: float) -> Vector:
        angle = -self.velocity.length() * time / self.length()
        return Vector(self.x, self.y).turn_by_angle(angle)
