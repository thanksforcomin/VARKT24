from Constants import *
from Rocket import Rocket, Stage
from math import pi
from Functions import *


def launch(angle_function, low, high):
    f = open("log.txt", "w")
    height = 0
    stage1 = Stage(
        MASS_SOLID_1, MASS_FUEL_1, FUEL_USAGE_1, THRUST_EARTH_1, THRUST_VACUUM_1
    )
    stage2 = Stage(
        MASS_SOLID_2, MASS_FUEL_2, FUEL_USAGE_2, THRUST_EARTH_2, THRUST_VACUUM_2
    )
    stage3 = Stage(
        MASS_SOLID_3, MASS_FUEL_3, FUEL_USAGE_3, THRUST_EARTH_3, THRUST_VACUUM_3
    )
    rocket = Rocket(0, KERBIN_RADIUS, [stage1, stage2, stage3])
    print(rocket.stages, sum(map(lambda x: x.get_mass(), rocket.stages)))
    rocket.set_angle_function(angle_function, low, high)
    dv = 0
    t = 0
    times_under_surface = 0
    m = 0

    while APOCENTER - rocket.length() > 80:
        if abs(int(t) - t) < dt:
            f.write(
                f"time={int(t)}; height={int(rocket.length())}; velocity={int(rocket.velocity.length())}; h={8.314 * 10**3 * 250 / (29 * GRAVITY_PARAMETER / (rocket.length() + KERBIN_RADIUS) ** 2)}\n"
            )
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
    f.close()
    print("Rocket got to apocenter: ", times_under_surface < 5000)
    print("Time:", round(t, 2))
    print("Position:", rocket)
    print("Height:", rocket.length() - KERBIN_RADIUS)
    print("Reached:", height)
    print("Stages: ", rocket.stages)
    print("Delta v spent:", round(dv, 2))
    print("Max speed:", m)
    print("Angle:", rocket.angle_to_radius)
    print(
        "Angle function in apogee: ", rocket.angle_function(rocket.length(), low, high)
    )
    print("Velocity: ", rocket.velocity.length())

    rocket.is_engine_off = False
    rocket.stage_disattach()

    rocket.angle_to_radius = -pi / 2

    if times_under_surface >= 5000:
        return times_under_surface < 5000, t, rocket, dv

    # while calculate_eccentricity(rocket, rocket.velocity) > 0.012:
    apocenter_current = rocket.length()
    while (
        sqrt(GRAVITY_PARAMETER / apocenter_current) - rocket.velocity.length()
        > 0.000000000001
    ):
        rocket.update_orbit_setup()
        t += dt
        dv += rocket.get_thrust().length() / rocket.get_mass() * dt
    rocket.is_engine_off = True

    print("Apocenter:", calculate_apocenter(rocket, rocket.velocity))
    print("Pericenter:", calculate_pericenter(rocket, rocket.velocity))
    print("Eccentricity: ", calculate_eccentricity(rocket, rocket.velocity))
    print("Velocity: ", rocket.velocity.length())
    print("dv: ", dv)

    # return times_under_surface < 5000, t, rocket, dv
    while True:
        rocket.update_orbit()

        t += dt


def calculate_best(
    angle_function, lower_start, upper_start, upper_end, step, output_file_name
):
    out = open(output_file_name, "a")
    best_dv = 10**9
    best_start = 0
    best_end = 0
    print("Entered")
    for start in range(lower_start, upper_start, step):
        print(
            f"Some thread is working with pace: {(start - lower_start) / (upper_start - lower_start)}"
        )
        out.write(
            f"{start})min_dv = {best_dv}; low = {best_start}; high = {best_end}\n"
        )
        for end in range(start + 1000, upper_end, step):
            on_orbit, t, rocket, dv = launch(
                angle_function, start + KERBIN_RADIUS, end + KERBIN_RADIUS
            )
            if on_orbit and best_dv > dv:
                best_dv = dv
                best_start = start
                best_end = end
    print("Out")
    # 5106.006154031641 10000 32000
    out.close()
    return best_dv, best_start, best_end

    print("END")


if __name__ == "__main__":
    print(launch(angle_elliptic, 10000 + KERBIN_RADIUS, 51000 + KERBIN_RADIUS))
