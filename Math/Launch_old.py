from Constants import *
from Vector import Vector
from Rocket import Rocket, Stage, NoStagesLeftException
from math import pi
from Functions import *

height = KERBIN_RADIUS
velocity = Vector(0, 0)
acceleration = Vector(0, 0)
stage1 = Stage(MASS_SOLID_1, MASS_FUEL_1, FUEL_USAGE_1, THRUST_EARTH_1, THRUST_VACUUM_1)
stage2 = Stage(MASS_SOLID_2, MASS_FUEL_2, FUEL_USAGE_2, THRUST_EARTH_2, THRUST_VACUUM_2)
stage3 = Stage(MASS_SOLID_3, MASS_FUEL_3, FUEL_USAGE_3, THRUST_EARTH_3, THRUST_VACUUM_3)
rocket = Rocket(0, KERBIN_RADIUS, [stage1, stage2, stage3])
is_engine_on = True
allow = False
dv = 0
t = 0
times_under_surface = 0
print(rocket)
prev = 0

while (rocket.length() < APOGEE or prev < 2000) and times_under_surface < 5000:
    # print(int(t), rocket, rocket.length())
    if rocket.length() > APOGEE:
        prev += 1
    # Stage disattach when fuel is out
    if is_engine_on and rocket.stages[0].fuel_mass < 0.5:
        print(t, rocket.stages, rocket, calculate_apogee(rocket, velocity))
        try:
            rocket.stage_disattach()
        except NoStagesLeftException:
            print(rocket, calculate_apogee(rocket, velocity), "Engines are gone :)")
            is_engine_on = False
    Force = Vector()
    R = Vector(
        ROCKET_D
        * 0.008
        * rocket.get_mass()
        * velocity.length() ** 2
        * density(rocket.length() - KERBIN_RADIUS)
        / 2,
        0,
    )
    R.turn_by_angle(pi + velocity.angle())
    Force += R

    Gravity = Vector(GRAVITY_PARAMETER * rocket.get_mass() / (rocket.length() ** 2), 0)
    Gravity.turn_by_angle(rocket.angle() + pi)

    Force += Gravity
    if is_engine_on:
        Force += rocket.get_thrust()
    else:
        # print(int(t), acceleration)
        ...

    acceleration = Force / rocket.get_mass()
    velocity += acceleration * dt
    rocket.add_vector(velocity * dt)
    if is_engine_on:
        res_of_update = rocket.update_mass()
    if is_engine_on and calculate_apogee(rocket, velocity) >= APOGEE:
        print(calculate_apogee(rocket, velocity))
        is_engine_on = False

    if rocket.length() < KERBIN_RADIUS:
        if int(t / dt) % 100 == 0:
            print(t, times_under_surface, rocket)
        times_under_surface += 1

    if is_engine_on:
        dv += acceleration.length() * dt

    height = max(height, rocket.length())
    # print(int(t), rocket, rocket.length(), is_engine_on, height)
    t += dt


print(
    height - KERBIN_RADIUS,
    rocket.angle(velocity),
    velocity,
    prev,
    "Crashed" if times_under_surface >= 5000 or prev < 2000 else "On orbit",
    t,
    rocket,
    velocity,
    rocket.length() - KERBIN_RADIUS,
    dv,
)

print("END")
