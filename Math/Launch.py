from Constants import *
from Rocket import Rocket, Stage
from math import pi, cos
from Functions import *
from Satellite import Satellite
from Center_of_gravity import Celestial


def launch(angle_function, low, high):
    f = open("log.txt", "w")
    height = 0
    Mun = Satellite(12_000_000, 0, 200_000, 9.7599066 * 10**22, 2_429_559)
    stage1 = Stage(
        MASS_SOLID_1, MASS_FUEL_1, FUEL_USAGE_1, THRUST_EARTH_1, THRUST_VACUUM_1
    )
    stage2 = Stage(
        MASS_SOLID_2, MASS_FUEL_2, FUEL_USAGE_2, THRUST_EARTH_2, THRUST_VACUUM_2
    )
    stage3 = Stage(
        MASS_SOLID_3, MASS_FUEL_3, FUEL_USAGE_3, THRUST_EARTH_3, THRUST_VACUUM_3
    )
    rocket = Rocket(
        0,
        KERBIN_RADIUS,
        Mun,
        Celestial(KERBIN_RADIUS, KERBIN_MASS, KERBIN_SOI),
        [stage1, stage2, stage3],
    )
    # print(rocket.stages, sum(map(lambda x: x.get_mass(), rocket.stages)))
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
    """
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
    """
    rocket.is_engine_off = False
    rocket.stage_disattach()

    rocket.angle_to_radius = -pi / 2

    if times_under_surface >= 5000:
        return times_under_surface < 5000, t, rocket, dv

    # while calculate_eccentricity(rocket, rocket.velocity) > 0.012:
    apocenter_current = rocket.length()
    while (
        sqrt(GRAVITY_PARAMETER / apocenter_current) - rocket.velocity.length() > 0.001
    ):
        rocket.update_orbit_setup()
        t += dt
        dv += rocket.get_thrust().length() / rocket.get_mass() * dt
    rocket.is_engine_off = True
    """
    print("Apocenter:", calculate_apocenter(rocket, rocket.velocity, rocket.center))
    print("Pericenter:", calculate_pericenter(rocket, rocket.velocity, rocket.center))
    print("Eccentricity: ", calculate_eccentricity(rocket, rocket.velocity, rocket.center))
    print("Velocity: ", rocket.velocity.length())
    print("dv: ", dv)
    """
    rocket.stage_disattach()
    print("On orbit")

    return times_under_surface < 5000, t, rocket, dv


def mun_launch(is_on_orbit: bool, t: float, rocket: Rocket, dv: float):
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

    while rocket.distance_to_mun() > 50_000:
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
            )
        if rocket.length() >= 12_000_000 - rocket.Mun.radius - 35_000:
            print(
                (rocket - current).turn_by_angle(-current.angle()),
                current.angle(),
                rocket.distance_to_mun(),
            )
            break

        t += dt
        t1 += dt
        dv += rocket.get_thrust().length() / rocket.get_mass()
    print("Got to the Mun")
    return is_on_orbit, t, rocket, dv


def mun_orbit(is_on_orbit: bool, t: float, rocket: Rocket, dv: float):
    if not is_on_orbit:
        return is_on_orbit, t, rocket, dv
    rocket.change_center_to_satellite()
    print(rocket, rocket.velocity, rocket.acceleration)
    rocket.is_engine_off = False
    print(calculate_pericenter(rocket, rocket.velocity, rocket.center))
    print(calculate_apocenter(rocket, rocket.velocity, rocket.center))
    while rocket.length() > rocket.center.radius:
        rocket.update_orbit()
        t += dt
        if abs(int(t) - t) < dt:
            print(
                int(t),
                rocket.length(),
                rocket.velocity.length(),
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
        r = Rocket(0, 0, [])
        print(
            f"Some thread is working with pace: {(start - lower_start) / (upper_start - lower_start)}"
        )
        for end in range(start + 1000, upper_end, step):
            on_orbit, t, rocket, dv = launch(
                angle_function, start + KERBIN_RADIUS, end + KERBIN_RADIUS
            )
            if on_orbit and best_dv > dv:
                best_dv = dv
                best_start = start
                best_end = end
                r = rocket
        out.write(
            f"{start})min_dv = {best_dv}; low = {best_start}; high = {best_end}; e={calculate_eccentricity(r, r.velocity, r.center)}\n"
        )
        print(
            f"{start})min_dv = {best_dv}; low = {best_start}; high = {best_end}; e={calculate_eccentricity(r, r.velocity, r.center)}\n"
        )

    print("Out")
    # 5106.006154031641 10000 32000
    out.close()
    return best_dv, best_start, best_end

    print("END")


if __name__ == "__main__":
    is_on_orbit, t, r, dv = mun_orbit(
        *mun_launch(
            *launch(angle_elliptic, 10000 + KERBIN_RADIUS, 51000 + KERBIN_RADIUS)
        )
    )
    print(is_on_orbit)
