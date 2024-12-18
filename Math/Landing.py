from Rocket import *
from time import sleep


def print_data(*args, time: int = 0):
    if abs(int(time) - time) < dt and int(time) % 5 == 0:
        print(*args)


def landing(radius: float) -> bool:
    stage = Stage(
        MASS_SOLID_4, MASS_FUEL_4 / 2, FUEL_USAGE_4, THRUST_EARTH_4, THRUST_VACUUM_4
    )
    Kerbin = Celestial(KERBIN_RADIUS, KERBIN_MASS, KERBIN_SOI)
    r = Rocket(0, radius, None, Kerbin, [stage])
    r.velocity = Vector(sqrt(Kerbin.GRAVITY_PARAMETER / radius), 0)
    r.is_engine_off = True
    t = 0

    while t < 100:
        r.update_orbit()
        t += dt
        print_data(int(t), r.length() - KERBIN_RADIUS, time=t)
    print("Ready to get down")

    r.is_engine_off = False

    while r.velocity.length() > 500:
        r.landing_orbit()
        t += dt
        print_data(
            int(t),
            r.length() - KERBIN_RADIUS,
            r.velocity.length(),
            r.get_mass(),
            r.get_drag().length(),
            ROCKET_D
            * 0.008
            * r.get_mass()
            * r.velocity.length() ** 2
            * density(r.length() - KERBIN_RADIUS)
            / 2,
            time=t,
        )
        if abs(int(t) - t) < dt and int(t) % 50 == 0:
            sleep(0.5)


landing(75000 + KERBIN_RADIUS)
