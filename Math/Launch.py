from Constants import *
from Vector import Vector
from Rocket import Rocket, Stage, NoStagesLeftException
from math import pi
from Functions import *
from time import sleep


def launch():
    height = 0
    stage1 = Stage(
        MASS_SOLID_1, MASS_FUEL_1, FUEL_USAGE_1, THRUST_EARTH_1, THRUST_VACUUM_1
    )
    stage2 = Stage(
        MASS_SOLID_2, MASS_FUEL_2, FUEL_USAGE_2, THRUST_EARTH_2, THRUST_VACUUM_2
    )
    # stage3 = Stage(MASS_SOLID_3, MASS_FUEL_3, FUEL_USAGE_3, THRUST_EARTH_3, THRUST_VACUUM_3)
    rocket = Rocket(0, KERBIN_RADIUS, [stage1, stage2])
    dv = 0
    t = 0
    times_under_surface = 0
    m = 0

    while APOCENTER - rocket.length() > 80:
        if rocket.length() < KERBIN_RADIUS:
            times_under_surface += 1
        height = max(height, rocket.update_launch() - KERBIN_RADIUS)
        if rocket.stages[0].fuel_mass < 1:
            rocket.is_engine_off = True
        m = max(rocket.velocity.length(), m)

        t += dt
        dv += rocket.get_thrust().length() / rocket.get_mass() * dt
        if times_under_surface == 5000:
            break
    print("Rocket got to apocenter: ", times_under_surface < 5000)
    print("Time:", round(t, 2))
    print("Position:", rocket)
    print("Height:", rocket.length() - KERBIN_RADIUS)
    print("Reached:", height)
    print("Stages: ", rocket.stages)
    print("Delta v spent:", round(dv, 2))
    print("Max speed:", m)
    print("Angle:", rocket.angle_to_radius)
    print("Velocity: ", rocket.velocity.length())
    rocket.is_engine_off = False
    rocket.stage_disattach()
    rocket.angle_to_radius = -pi / 2

    if times_under_surface >= 5000:
        return times_under_surface < 5000, t, rocket, dv

    while calculate_eccentricity(rocket, rocket.velocity) > 0.012:
        rocket.update_orbit_setup()
        t += dt
        dv += rocket.get_thrust().length() / rocket.get_mass() * dt
    rocket.is_engine_off = True
    print("Apocenter:", calculate_apocenter(rocket, rocket.velocity))
    print("Pericenter:", calculate_pericenter(rocket, rocket.velocity))
    print("Eccentricity: ", calculate_eccentricity(rocket, rocket.velocity))
    print("Velocity: ", rocket.velocity.length())
    print(rocket.length())
    while True:
        rocket.update_orbit()
        print(int(t), int(rocket.length()))
        t += dt
    return times_under_surface < 5000, t, rocket, dv


launch()

print("END")
