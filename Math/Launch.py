from Constants import *
from Vector import Vector
from Rocket import Rocket
from math import pi
from Functions import *

height = KERBIN_MASS
velocity = Vector(0, 0)
acceleration = Vector(0, 0)
rocket = Rocket(0, KERBIN_RADIUS, ROCKET_MASS, FUEL, FUEL_USAGE)
is_engine_on = True
allow = False
dv = 0
t = 0
print(rocket)

while True:
    Force = Vector(0, 0)
    R = Vector(
        ROCKET_D
        * SURFACE
        * velocity.length() ** 2
        * density(rocket.length() - KERBIN_RADIUS)
        / 2,
        0,
    )
    R.turn_by_angle(pi + velocity.angle())
    Force += R

    Gravity = Vector(GRAVITY_PARAMETER * rocket.get_mass() / (rocket.length() ** 2), 0)
    Gravity.turn_by_angle(rocket.angle())

    Force += Gravity
    if is_engine_on:
        Thrust = Vector(
            THRUST_VACUUM
            + (THRUST_EARTH - THRUST_VACUUM)
            * pressure(rocket.length() - KERBIN_RADIUS),
            0,
        )
        Thrust.turn_by_angle(rocket.angle() + angle(rocket.length()))
        Force += Thrust

    acceleration = Force / rocket.get_mass()
    velocity += acceleration * dt
    rocket.addVector(velocity * dt)
    if is_engine_on:
        res_of_update = rocket.update_mass()
    if res_of_update or rocket.length() >= KERBIN_RADIUS + 5_000:
        is_engine_on = False

    if t < 34 and t > 30:
        print(acceleration.length())
    if rocket.length() < KERBIN_RADIUS and allow:
        break
    if not allow and rocket.length() > KERBIN_RADIUS + 6_000:
        allow = True
    dv += acceleration.length() * dt
    t += dt
    height = max(height, rocket.length())
    print(
        int(t),
        rocket,
        R,
        Gravity,
        round(rocket.length() - KERBIN_RADIUS, 2),
        round(velocity.length(), 2),
        is_engine_on,
        Thrust.length(),
        rocket.angle(),
    )

print(
    t,
    rocket,
    height - KERBIN_RADIUS,
)

print("END")
