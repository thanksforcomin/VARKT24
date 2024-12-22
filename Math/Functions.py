from turtle import pos
from Vector import Vector
from Constants import *
from math import acos, pi, sin, sqrt, e, sqrt, tan, atan
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


def calculate_eccentricity_vector(
    position: Vector, velocity: Vector, center: Celestial
) -> Vector:
    return (
        position
        * (velocity.length() ** 2 / center.GRAVITY_PARAMETER - 1 / position.length())
        - velocity
        * (position.x * velocity.x + position.y + velocity.y)
        / center.GRAVITY_PARAMETER
    )


def true_anomaly(rocket: Vector, velocity: Vector, center: Celestial):
    e = calculate_eccentricity_vector(rocket, velocity, center)
    u = e.x * rocket.x + e.y * rocket.y
    v = acos(u / (e.length() * rocket.length()))
    if rocket.x * velocity.x + rocket.y * velocity.y < 0:
        return 2 * pi - v
    return v


def calculate_eccentric_anomaly(rocket: Vector, velocity: Vector, center: Celestial):
    tr_an = true_anomaly(rocket, velocity, center)
    e = calculate_eccentricity(rocket, velocity, center)
    u = sqrt((1 - e) / (1 + e)) * tan(tr_an / 2)
    E = 2 * atan(u)
    if E < 0:
        E = 2 * pi - E
    return E


def calculate_mean_anomaly(rocket: Vector, velocity: Vector, center: Celestial):
    E = calculate_eccentric_anomaly(rocket, velocity, center)
    e = calculate_eccentricity(rocket, velocity, center)

    return E - e * sin(E)


def time_to_periapsis(
    rocket: Vector, velocity: Vector, center: Celestial, direction: float
):
    ...
    return 0


def time_to_apoapsis(rocket: Vector, velocity: Vector, center: Celestial):
    a = calculate_semi_major_axis(rocket, velocity, center)
    coef = sqrt(a**3 / center.GRAVITY_PARAMETER)
    dM = pi - calculate_mean_anomaly(rocket, velocity, center)
    return dM * coef
