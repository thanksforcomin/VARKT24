from Constants import *
from Vector import Vector
from Rocket import Rocket
from math import pi
from Functions import *

velocity = Vector(0, 0)
acceleration = Vector(0, 0)
rocket = Rocket(0, KERBIN_RADIUS, ROCKET_MASS, FUEL, FUEL_USAGE)
is_engine_on = True
dv = 0

while rocket.length() < APOGEE:
    Force = Vector(0, 0)
    R = Vector(
        ROCKET_D
        * SURFACE
        * velocity.length() ** 2
        * density(rocket.length() - KERBIN_RADIUS),
        0,
    )
    R.turn_by_angle(pi + velocity.angle())
    Force += R

    Gravity = Vector(GRAVITY_PARAMETER * rocket.get_mass() / rocket.length() ** 2, 0)
    Gravity.turn_by_angle(pi + rocket.angle())
    Force += Gravity

    if is_engine_on:
        Thurst = Vector(
            THRUST_VACUUM
            + (THRUST_EARTH - THRUST_VACUUM)
            * pressure(rocket.length() - KERBIN_RADIUS),
            0,
        )
        Thurst.turn_by_angle(rocket.angle() + angle(rocket.length() - KERBIN_RADIUS))
        Force += Thurst

    acceleration = Force / rocket.get_mass() - velocity * FUEL_USAGE
    velocity += acceleration * dt
    rocket.addVector(velocity * dt)
    if is_engine_on:
        res_of_update = rocket.update_mass()
    if res_of_update or calculate_apogee(rocket, velocity) >= APOGEE:
        is_engine_on = False

    dv += acceleration.length() * dt
    print(rocket)

print
