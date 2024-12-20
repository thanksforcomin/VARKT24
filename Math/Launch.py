from operator import le
from Constants import *
from Rocket import Rocket, Stage, NoStagesLeftException
from math import pi
from Functions import *
from Satellite import Satellite
from Center_of_gravity import Celestial
from Logger import Logger


def launch(angle_function, low, high):
    height = 0
    Mun = Satellite(12_000_000, 0, 200_000, 9.7599066 * 10**20, 2_429_559)
    height_logger = Logger("height.json")
    velocity_logger = Logger("velocity_launch.json")
    mass_logger = Logger("mass_launch.json")
    acc_logger = Logger("acc.json")
    angle_logger = Logger("angle.json")
    stage1 = Stage(
        MASS_SOLID_1,
        MASS_FUEL_1,
        FUEL_USAGE_1,
        THRUST_EARTH_1,
        THRUST_VACUUM_1,
    )
    stage2 = Stage(
        MASS_SOLID_2, MASS_FUEL_2, FUEL_USAGE_2, THRUST_EARTH_2, THRUST_VACUUM_2
    )
    stage3 = Stage(
        MASS_SOLID_3, MASS_FUEL_3, FUEL_USAGE_3, THRUST_EARTH_3, THRUST_VACUUM_3
    )
    stage4 = Stage(
        MASS_SOLID_4, MASS_FUEL_4, FUEL_USAGE_4, THRUST_EARTH_4, THRUST_VACUUM_4
    )
    rocket = Rocket(
        0,
        KERBIN_RADIUS,
        Mun,
        Celestial(KERBIN_RADIUS, KERBIN_MASS, KERBIN_SOI),
        [stage1, stage2, stage3, stage4],
    )
    # print(rocket.stages, sum(map(lambda x: x.get_mass(), rocket.stages)))
    rocket.set_angle_function(angle_function, low, high)
    dv = 0
    t = 0
    times_under_surface = 0
    rocket.throttle = 1
    m = 0

    while not rocket.is_engine_off:
        if abs(int(t) - t) < dt or 0.5 - dt < abs(int(t) - t) < 0.5 + dt:
            height_logger.insert(round(t, 2), rocket.length() - rocket.center.radius)
            mass_logger.insert(round(t, 2), rocket.get_mass())
            velocity_logger.insert(round(t, 2), rocket.velocity.length())
            acc_logger.insert(round(t, 2), rocket.acceleration.length())
            angle_logger.insert(round(t, 2), rocket.angle_to_radius * 180 / 3.14 + 90)
        if rocket.length() < KERBIN_RADIUS:
            times_under_surface += 1
        height = max(height, rocket.update_launch() - KERBIN_RADIUS)
        if rocket.stages[0].fuel_mass < 1:
            rocket.stage_disattach()
        m = max(rocket.velocity.length(), m)
        # print(APOCENTER, calculate_apocenter(rocket, rocket.velocity, rocket.center))

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
    print(
        "Angle function in apogee: ", rocket.angle_function(rocket.length(), low, high)
    )
    print("Velocity: ", rocket.velocity.length())

    print(
        "semi",
        calculate_apocenter(rocket, rocket.velocity, rocket.center)
        - rocket.center.radius,
    )
    print(
        "Apocenter:",
        calculate_apocenter(rocket, rocket.velocity, rocket.center)
        - rocket.center.radius,
    )
    print(
        "Pericenter:",
        calculate_pericenter(rocket, rocket.velocity, rocket.center)
        - rocket.center.radius,
    )
    print(
        "Eccentricity: ", calculate_eccentricity(rocket, rocket.velocity, rocket.center)
    )
    # print(rocket.stages)
    # rocket.stage_disattach()
    print(rocket.stages)
    rocket.angle_to_radius = -pi / 2

    if times_under_surface >= 5000:
        return times_under_surface < 5000, t, rocket, dv

    # while calculate_eccentricity(rocket, rocket.velocity) > 0.012:
    apocenter_current = rocket.length()
    rocket.throttle = 0.65
    print(calculate_apocenter(rocket, rocket.velocity, rocket.center))
    while (
        # sqrt(GRAVITY_PARAMETER / apocenter_current) - rocket.velocity.length() > 0.001
        calculate_pericenter(rocket, rocket.velocity, rocket.center)
        < 70_500 + rocket.center.radius
    ):
        if abs(int(t) - t) < dt or 0.5 - dt < abs(int(t) - t) < 0.5 + dt:
            height_logger.insert(round(t, 2), rocket.length() - rocket.center.radius)
            mass_logger.insert(round(t, 2), rocket.get_mass())
            velocity_logger.insert(round(t, 2), rocket.velocity.length())
            acc_logger.insert(round(t, 2), rocket.acceleration.length())

        if len(rocket.stages) == 1 and rocket.stages[0].fuel_mass < 0.5:
            rocket.is_engine_off = True
        height = max(height, rocket.length())
        if rocket.length() < rocket.center.radius:
            print("CRASHED")
            break
        if abs(int(t) - t) < dt:
            print(
                int(t),
                rocket.length() - rocket.center.radius,
                rocket.is_engine_off,
                calculate_apocenter(rocket, rocket.velocity, rocket.center),
                calculate_pericenter(rocket, rocket.velocity, rocket.center),
                rocket.Force.length(),
                rocket.acceleration.length(),
                rocket.velocity.length(),
                time_to_apoapsis(rocket, rocket.velocity, rocket.center),
            )
        rocket.update_orbit_setup()
        t += dt
        dv += rocket.get_thrust_velocity().length() / rocket.get_mass() * dt
    rocket.is_engine_off = True

    while True:
        if abs(int(t) - t) < dt:
            print(
                int(t),
                rocket.length() - 600_000,
                calculate_apocenter(rocket, rocket.velocity, rocket.center) - 600_000,
                calculate_pericenter(rocket, rocket.velocity, rocket.center) - 600_000,
                time_to_apoapsis(rocket, rocket.velocity, rocket.center),
                calculate_mean_anomaly(rocket, rocket.velocity, rocket.center),
            )

        t += dt
        rocket.update_orbit()
    print(rocket.stages)
    rocket.is_engine_off = True

    print(
        "Apocenter:",
        calculate_apocenter(rocket, rocket.velocity, rocket.center)
        - rocket.center.radius,
    )
    print(
        "Pericenter:",
        calculate_pericenter(rocket, rocket.velocity, rocket.center)
        - rocket.center.radius,
    )
    print(
        "Eccentricity: ", calculate_eccentricity(rocket, rocket.velocity, rocket.center)
    )
    print("Velocity: ", rocket.velocity.length())
    print("dv: ", dv)
    print("Reached: ", height)
    print(rocket.stages)
    print("On orbit")
    height_logger.dump()
    acc_logger.dump()
    mass_logger.dump()
    velocity_logger.dump()
    angle_logger.dump()
    return times_under_surface < 5000, t, rocket, dv


def mun_launch(is_on_orbit: bool, t: float, rocket: Rocket, dv: float):
    rocket.throttle = 1
    if not is_on_orbit:
        print("Didn't get to the orbit")
        return is_on_orbit, t, rocket, dv
    while not rocket.mun_transfer_check():
        rocket.update_orbit()
        t += dt

    current = Vector(rocket.x, rocket.y)
    print("Launching", t, current.length(), current)
    t1 = 0
    rocket.is_engine_off = False

    while rocket.length() < rocket.Mun.length() + MUN_DIST - 1000:
        rocket.mun_transfer()
        dv += rocket.get_thrust().length() / rocket.get_mass() * dt
        if abs(int(t) - t) < dt:
            print(
                int(t),
                int(t1),
                rocket.length() > rocket.Mun.length(),
                int(rocket.length()),
                int(rocket.velocity.length()),
                int(rocket.distance_to_mun()),
                calculate_eccentricity(rocket, rocket.velocity, rocket.center),
                calculate_pericenter(rocket, rocket.velocity, rocket.center),
                calculate_apocenter(rocket, rocket.velocity, rocket.center),
                rocket.is_engine_off,
                int(dv),
                len(rocket.stages),
            )
        if rocket.distance_to_mun() < rocket.Mun.radius:
            print(
                "Crashed",
                (rocket - current).turn_by_angle(-current.angle()),
                current.angle(),
                rocket.distance_to_mun(),
            )
            break

        t += dt
        t1 += dt
        dv += rocket.get_thrust().length() / rocket.get_mass() * dt
    print("Got to the Mun")
    return is_on_orbit, t, rocket, dv


def mun_return(is_on_orbit: bool, t: float, rocket: Rocket, dv: float):
    print("Going back")
    while rocket.distance_to_mun() <= rocket.Mun.SOI:
        t += dt
        rocket.mun_transfer()
        if abs(int(t) - t) < dt:
            print(
                "tranfer",
                int(t),
                rocket.length(),
                rocket.velocity.length(),
                rocket.distance_to_mun(),
                rocket.stages,
            )
    rocket.is_engine_off = False
    while rocket.length() < 70_000 + rocket.center.radius:
        while (
            calculate_velocity_at_periapsis(rocket, rocket.velocity, rocket.center)
            < MAX_RETURN_VELOCITY
        ):
            t += dt
            rocket.mun_escape()
            if abs(int(t) - t) < dt:
                print(
                    "slowing down",
                    int(t),
                    int(rocket.length()),
                    int(rocket.velocity.length()),
                    int(rocket.distance_to_mun()),
                    rocket.stages,
                )
        rocket.is_engine_off = True
        while rocket.length() > calculate_pericenter(
            rocket, rocket.velocity, rocket.center
        ):
            print("in")
            t += dt
            rocket.update_orbit()
            if abs(int(t) - t) < dt:
                print(
                    "going to periapsis",
                    int(t),
                    rocket.length(),
                    rocket.velocity.length(),
                    rocket.distance_to_mun(),
                    rocket.stages,
                )
        rocket.is_engine_off = False
        while calculate_eccentricity(rocket, rocket.velocity, rocket.center) > 0.1:
            t += dt
            rocket.mun_escape()
            if abs(int(t) - t) < dt:
                print(
                    "going to apoapsis, slowing",
                    int(t),
                    rocket.length(),
                    rocket.velocity.length(),
                    rocket.distance_to_mun(),
                    rocket.stages,
                )
        while rocket.length() < calculate_apocenter(
            rocket, rocket.velocity, rocket.center
        ):
            t += dt
            rocket.update_orbit()
            if abs(int(t) - t) < dt:
                print(
                    "going to apoapsis",
                    int(t),
                    rocket.length(),
                    rocket.velocity.length(),
                    rocket.distance_to_mun(),
                    rocket.stages,
                )
    return is_on_orbit, t, rocket, dv


def calculate_best(
    angle_function, lower_start, upper_start, upper_end, step, output_file_name
):
    out = open(output_file_name, "w")

    print("Entered")
    for start in range(lower_start, upper_start, step):
        best_dv = 10**9
        best_start = 0
        best_end = 0
        best_e = 0
        r = Rocket(0, 0, Satellite(1, 1, 1, 1, 1), Celestial(1, 1, 1), [])
        print(
            f"Some thread is working with pace: {(start - lower_start) / (upper_start - lower_start)}"
        )
        for end in range(start + 1000, upper_end, step):
            try:
                on_orbit, t, rocket, dv = launch(
                    angle_function, start + KERBIN_RADIUS, end + KERBIN_RADIUS
                )
            except NoStagesLeftException:
                continue
            if on_orbit and best_dv > dv:
                best_dv = dv
                best_start = start
                best_end = end
                r = rocket
        if not r.center:
            continue
        out.write(
            f"{start})min_dv = {best_dv}; low = {best_start}; high = {best_end}; e={calculate_eccentricity(r, r.velocity, r.center)}\n"
        )

    print("Out")
    # 5106.006154031641 10000 32000
    out.close()
    return best_dv, best_start, best_end

    print("END")


if __name__ == "__main__":
    is_on_orbit, t, r, dv = launch(angle_linear, TURNING_START, TURNING_END)
    print(is_on_orbit, r.length())
