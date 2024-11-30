from Vector import Vector
from Constants import *
from math import pi, sin, sqrt, e, sqrt


def angle(height: float) -> float:
    if height < TURNING_START:
        return 0
    if height > TURNING_END:
        return pi / 2
    return (pi / 2) * (height - TURNING_START) / (TURNING_END - TURNING_START)


def eccentricity(position: Vector, velocity: Vector) -> float:
    angle = position.angle(velocity)
    h = position.length() * velocity.length()
    epsilon = velocity.length() ** 2 / 2 - GRAVITY_PARAMETER / position.length()
    return sqrt(1 + 2 * epsilon * h * h / (GRAVITY_PARAMETER**2))


def calculate_apogee(position: Vector, velocity: Vector) -> float:
    h_squared = (
        position.x * velocity.y - position.y * velocity.x
    ) ** 2  # specific relative angular momentum в квадрате
    epsilon = (
        velocity.length() ** 2
    ) / 2 - GRAVITY_PARAMETER / position.length()  # specific orbital energy
    eccentricity = sqrt(
        1 + 2 * epsilon * h_squared / (GRAVITY_PARAMETER**2)
    )  # эксцентриситет
    semi_major = 1 / (
        2 / position.length() - (velocity.x**2 + velocity.y**2) / GRAVITY_PARAMETER
    )

    return (1 + eccentricity) * semi_major


def pressure(height: float):
    return e ** (-height / H)


def density(height: float):
    return DENSITY_TO_PRESSURE_RATIO * pressure(height)
