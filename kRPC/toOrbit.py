import krpc
from krpc.services.spacecenter import *
from math import sqrt, exp
from time import sleep


TARGET_APOAPSIS = 75000


def angle_linear(height: float, low: float, high: float) -> float:
    if height < low:
        return 0
    if height > high:
        return -90
    return -90 * (height - low) / (high - low)


def engage(connection: krpc.Client, ascentProfileConstant=1.25):
    """Sends vessel to orbit 75 x 70km in preparation for transfer burn"""
    space_center = connection.space_center
    vessel = space_center.active_vessel

    vessel.control.rcs = True
    vessel.control.throttle = 0.76

    vessel.control.activate_next_stage()

    apoapsisStream = connection.add_stream(getattr, vessel.orbit, "apoapsis_altitude")
    altitude = connection.add_stream(getattr, vessel.flight(), "mean_altitude")
    ut = connection.add_stream(getattr, connection.space_center, "ut")
    vessel.auto_pilot.engage()
    vessel.auto_pilot.target_heading = 90
    vessel.auto_pilot.target_pitch = 90

    while altitude() < 10000:
        sleep(0.1)

    # Get to proper apoapsis/complete gravity turn
    while apoapsisStream() < TARGET_APOAPSIS:
        print(vessel.auto_pilot.sas)
        # Calculate the target pitch
        targetPitch = 90 + angle_linear(altitude(), 2000, 50000)
        print("Current target pitch:", targetPitch, "with apoapsis", apoapsisStream())

        # Set autopilot target pitch
        vessel.auto_pilot.target_pitch = targetPitch

        sleep(0.1)

    vessel.control.throttle = 0
    timeToApoapsisStream = connection.add_stream(
        getattr, vessel.orbit, "time_to_apoapsis"
    )
    periapsisStream = connection.add_stream(getattr, vessel.orbit, "periapsis_altitude")
    #calculating delta v
    mu = vessel.orbit.body.gravitational_parameter
    r = vessel.orbit.apoapsis
    a1 = vessel.orbit.semi_major_axis
    a2 = r
    v1 = sqrt(mu * ((2.0 / r) - (1.0 / a1)))
    v2 = sqrt(mu * ((2.0 / r) - (1.0 / a2)))
    delta_v = v2 - v1
    #setting maneuver node and rotating to it
    node = vessel.control.add_node(ut() + timeToApoapsisStream(), prograde=delta_v)
    vessel.auto_pilot.reference_frame = node.reference_frame
    vessel.auto_pilot.target_direction = (0,1,0)
    # vessel.control.throttle = 0.2
    print(vessel.auto_pilot.reference_frame)
    print(vessel.auto_pilot.target_direction)
    print(node.reference_frame)
    sleep(1)
    vessel.control.activate_next_stage()
    # Calculate burn time (using rocket equation)
    F = vessel.available_thrust
    Isp = vessel.specific_impulse * 9.82
    m0 = vessel.mass
    m1 = m0 / exp(delta_v/Isp)
    flow_rate = F / Isp
    burn_time = (m0 - m1) / flow_rate   
    vessel.control.throttle = 0
    print(burn_time)
    # Now, wait and perform circularization burn
    while node.time_to - 20 > burn_time/2:
        print("Drifting to apoapsis.....")
        sleep(0.5)

    vessel.control.throttle = 1
    lastUT = ut()
    lastTimeToAp = timeToApoapsisStream()
    eps = 20000
    #Circulazation burn
    while abs(periapsisStream() - apoapsisStream()) > eps:
        sleep(0.2)
        print("Remaining delta V:", node.remaining_delta_v)
        liquid_fuel = vessel.resources.amount("LiquidFuel")
        timeToAp = timeToApoapsisStream()
        deltaTimeToAp = (timeToAp - lastTimeToAp) / (ut() - lastUT)
        vessel.auto_pilot.target_direction = (0,1,0)
        print("Estimated change in time to apoapsis per second:", deltaTimeToAp)

        # Adjust throttle according to the current deltaTimeToAp
        #if deltaTimeToAp < -0.3:
        #    vessel.control.throttle += 0.03
        #elif deltaTimeToAp < -0.1:
        #    vessel.control.throttle += 0.01

        #if deltaTimeToAp > 0.2:
        #    vessel.control.throttle -= 0.03
        #elif deltaTimeToAp > 0:
        #    vessel.control.throttle -= 0.01

        lastTimeToAp = timeToApoapsisStream()
        lastUT = ut()
    node.remove()
    vessel.auto_pilot.reference_frame = vessel.surface_velocity_reference_frame
    vessel.auto_pilot.target_direction = (0,1,0)
    eps = 1000
    vessel.control.throttle = 0.2
    while abs(periapsisStream() - apoapsisStream()) > eps:
        sleep(0.2)
    vessel.control.throttle = 0
    print("Apoapsis: ", apoapsisStream())
    print("Periapsis: ", periapsisStream())
    print("Orbit achieved!")
    print()
