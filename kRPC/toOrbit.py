import krpc
from math import sqrt
from time import sleep


TARGET_APOAPSIS = 75000


def angle_elliptic(height: float, low: float, high: float) -> float:
    if height < low:
        return 0
    if height > high:
        return -90
    return -90 * sqrt(1 - ((height - high) / (high - low)) ** 2)


def engage(connection, ascentProfileConstant=1.25):
    """Sends vessel to orbit 75 x 70km in preparation for transfer burn"""
    space_center = connection.space_center
    vessel = space_center.active_vessel

    vessel.control.rcs = True
    vessel.control.sas = True
    vessel.control.throttle = 0.76

    vessel.control.activate_next_stage()

    apoapsisStream = connection.add_stream(getattr, vessel.orbit, "apoapsis_altitude")
    altitude = connection.add_stream(getattr, vessel.flight(), "mean_altitude")

    vessel.auto_pilot.engage()
    vessel.auto_pilot.target_heading = 90
    vessel.auto_pilot.target_pitch = 90

    while altitude() < 10000:
        sleep(0.1)

    # Get to proper apoapsis/complete gravity turn
    while apoapsisStream() < TARGET_APOAPSIS:
        # Calculate the target pitch
        targetPitch = 90 + angle_elliptic(altitude(), 10000, 51000)
        print("Current target pitch:", targetPitch, "with apoapsis", apoapsisStream())

        # Set autopilot target pitch
        vessel.auto_pilot.target_pitch = targetPitch

        sleep(0.1)

    vessel.control.throttle = 0
    timeToApoapsisStream = connection.add_stream(
        getattr, vessel.orbit, "time_to_apoapsis"
    )
    periapsisStream = connection.add_stream(getattr, vessel.orbit, "periapsis_altitude")
    # Now, wait and perform circularization burn
    while timeToApoapsisStream() > 22:
        if timeToApoapsisStream() > 60:
            space_center.rails_warp_factor = 4
        else:
            space_center.rails_warp_factor = 0

        sleep(0.5)

    vessel.control.activate_next_stage()

    vessel.control.throttle = 1
    lastUT = space_center.ut
    lastTimeToAp = timeToApoapsisStream()
    while periapsisStream() < TARGET_APOAPSIS:
        sleep(0.2)
        timeToAp = timeToApoapsisStream()
        deltaTimeToAp = (timeToAp - lastTimeToAp) / (space_center.ut - lastUT)

        print("Estimated change in time to apoapsis per second:", deltaTimeToAp)

        # Adjust throttle according to the current deltaTimeToAp
        if deltaTimeToAp < -0.3:
            vessel.control.throttle += 0.03
        elif deltaTimeToAp < -0.1:
            vessel.control.throttle += 0.01

        if deltaTimeToAp > 0.2:
            vessel.control.throttle -= 0.03
        elif deltaTimeToAp > 0:
            vessel.control.throttle -= 0.01

        lastTimeToAp = timeToApoapsisStream()
        lastUT = space_center.ut

    vessel.control.throttle = 0
    print("Apoapsis: ", apoapsisStream())
    print("Periapsis: ", periapsisStream())
    print("Orbit achieved!")
    print()
