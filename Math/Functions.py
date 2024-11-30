from Vector import Vector
from Constants import *
from math import pi, sin, sqrt, e


def angle(height: float) -> float:
    if height < TURNING_START or height > TURNING_END:
        return 0
    return (pi / 2) * (height - TURNING_START) / (TURNING_END - TURNING_START)


def eccentricity(position: Vector, velocity: Vector) -> float:
    angle = position.angle(velocity)
    h = position.length() * velocity.length() * sin(angle)
    epsilon = velocity.length() ** 2 / 2 - GRAVITY_PARAMETER / position.length()
    return sqrt(1 + epsilon * h * h / (GRAVITY_PARAMETER**2))


def calculate_apogee(position: Vector, velocity: Vector) -> float:
    e = eccentricity(position=position, velocity=velocity)
    a_inverse = 2 / position.length() - velocity.length() ** 2 / GRAVITY_PARAMETER
    return (1 + e) / a_inverse


def pressure(height: float):
    return e ** (-height / H)


def density(height: float):
    return DENSITY_TO_PRESSURE_RATIO * pressure(height)
