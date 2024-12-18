from Vector import Vector
from Constants import *
from math import pi, sin, sqrt, e, sqrt
from Center_of_gravity import Celestial


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
    return k * (height - high) ** 2 - pi / 2


def angle_elliptic(height: float, low: float, high: float) -> float:
    if height < low:
        return 0
    if height > high:
        return -pi / 2
    return -pi / 2 + pi / 2 * sqrt(1 - ((height - low) / (high - low)) ** 2)


def calculate_eccentricity(
    position: Vector, velocity: Vector, center: Celestial
) -> float:
    angle = position.angle(velocity)
    h = position.length() * velocity.length() * sin(angle)
    epsilon = velocity.length() ** 2 / 2 - center.GRAVITY_PARAMETER / position.length()
    return sqrt(1 + 2 * epsilon * h * h / (center.GRAVITY_PARAMETER**2))


def calculate_semi_major_axis(position: Vector, velocity: Vector, center: Celestial):
    return 1 / (
        2 / position.length() - velocity.length() ** 2 / center.GRAVITY_PARAMETER
    )


def calculate_apocenter(position: Vector, velocity: Vector, center: Celestial) -> float:
    e = calculate_eccentricity(position, velocity, center)
    return (1 + e) * calculate_semi_major_axis(position, velocity, center)


def calculate_pericenter(
    position: Vector, velocity: Vector, center: Celestial
) -> float:
    e = calculate_eccentricity(position, velocity, center)
    return (1 - e) * calculate_semi_major_axis(position, velocity, center)


def calculate_velocity_at_periapsis(
    position: Vector, velocity: Vector, center: Celestial
):
    peri = calculate_pericenter(position, velocity, center)
    a = calculate_semi_major_axis(position, velocity, center)
    return sqrt(center.GRAVITY_PARAMETER * (2 / peri - 1 / a))


def pressure(height: float):
    return e ** (-height / 5600)


def density(height: float):
    return DENSITY_TO_PRESSURE_RATIO * pressure(height)


def cd(height: float):
    return 0
