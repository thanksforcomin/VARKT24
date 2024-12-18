from re import I
import krpc
import threading
import logger as log
from time import sleep
from math import sqrt


def angle_linear(height: float, low: float, high: float) -> float:
    if height < low:
        return 0
    if height > high:
        return -180 / 2
    return -(180 / 2) * (height - low) / (high - low)


def angle_parabolic(height: float, low: float, high: float) -> float:
    if height < low:
        return 0
    if height > high:
        return -180 / 2
    k = -180 / (2 * (high - low) ** 2)
    return k * (height - low) ** 2


def angle_elliptic(height: float, low: float, high: float) -> float:
    if height < low:
        return 0
    if height > high:
        return -180 / 2
    return -180 / 2 * sqrt(1 - ((height - high) / (high - low)) ** 2)


def engage(connection, ascentProfileConstant=1.25):
    """Sends vessel to orbit 75 x 70km in prep for transfer burn"""
    space_center = connection.space_center
    vessel = space_center.active_vessel

    logger = log.Logger()
    logger.create_log_file("to_orbit")

    # set up the logging thread
    logging = threading.Thread(
        target=log.collect_data_and_log,
        args=(
            logger,
            vessel,
        ),
    )
    logging.start()

    vessel.control.rcs = True

    vessel.control.throttle = 1
    vessel.control.activate_next_stage()

    apoapsisStream = connection.add_stream(getattr, vessel.orbit, "apoapsis_altitude")

    vessel.auto_pilot.engage()
    vessel.auto_pilot.target_heading = 90

    altitude = connection.add_stream(getattr, vessel.flight(), "mean_altitude")

    # Get to proper apoapsis/complete gravity turn
    while apoapsisStream() < 75000:
        # Collect values
        targetPitch = 90 + angle_linear(altitude(), 1000, 30000)
        print("Current target pitch:", targetPitch, "with apoapsis", apoapsisStream())

        # Set autopilot
        vessel.auto_pilot.target_pitch = targetPitch

        sleep(0.1)

    vessel.control.throttle = 0

    timeToApoapsisStream = connection.add_stream(
        getattr, vessel.orbit, "time_to_apoapsis"
    )
    periapsisStream = connection.add_stream(getattr, vessel.orbit, "periapsis_altitude")
    # Now, wait and perform circularization burn
    while timeToApoapsisStream() > 27:
        if timeToApoapsisStream() > 60:
            space_center.rails_warp_factor = 4
        else:
            space_center.rails_warp_factor = 0

        sleep(0.5)

    vessel.control.throttle = 0.5
    vessel.auto_pilot.target_pitch = 0
    lastUT = space_center.ut
    lastTimeToAp = timeToApoapsisStream()
    while periapsisStream() < 70500:
        sleep(0.2)
        timeToAp = timeToApoapsisStream()
        UT = space_center.ut
        deltaTimeToAp = (timeToAp - lastTimeToAp) / (space_center.ut - lastUT)

        print("Estimated change in time to apoapsis per second:", deltaTimeToAp)

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

    logger.stop_logging()

    print()
