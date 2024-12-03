from Vector import Vector
from Constants import *
from math import pi, sin, sqrt, e, sqrt


def angle_linear(height: float, low: float, high: float) -> float:
    if height < low:
        return 0
    if height > high:
        return -pi / 2
    return -(pi / 2) * (height - low) / (high - low)


def angle_parabolic(height: float, low: float, high: float) -> float:
    if height < low:
        return 0
    if height > high:
        return -pi / 2
    k = -pi / (2 * (high - low) ** 2)
    return k * (height - low) ** 2


def angle_elliptic(height: float, low: float, high: float) -> float:
    if height < low:
        return 0
    if height > high:
        return -pi / 2
    return -pi / 2 * sqrt(1 - ((height - high) / (high - low)) ** 2)


def calculate_eccentricity(position: Vector, velocity: Vector) -> float:
    angle = position.angle(velocity)
    h = position.length() * velocity.length() * sin(angle)
    epsilon = velocity.length() ** 2 / 2 - GRAVITY_PARAMETER / position.length()
    return sqrt(1 + 2 * epsilon * h * h / (GRAVITY_PARAMETER**2))


def calculate_apocenter(position: Vector, velocity: Vector) -> float:
    e = calculate_eccentricity(position=position, velocity=velocity)
    a_inverse = 2 / position.length() - velocity.length() ** 2 / GRAVITY_PARAMETER
    return (1 + e) / a_inverse


def calculate_pericenter(position: Vector, velocity: Vector) -> float:
    e = calculate_eccentricity(position=position, velocity=velocity)
    a_inverse = 2 / position.length() - velocity.length() ** 2 / GRAVITY_PARAMETER
    return (1 - e) / a_inverse


def pressure(height: float):
    return e ** (-height / H)


def density(height: float):
    return DENSITY_TO_PRESSURE_RATIO * pressure(height)
