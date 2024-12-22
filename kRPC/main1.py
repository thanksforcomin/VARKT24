import krpc
from krpc.services.spacecenter import SASMode, Vessel
import threading
import stageMonitor
import toOrbit
import toOrbit1
import munTransfer
import orbitMun
import math

from time import sleep

sleep(10)


conn = krpc.connect()
space_center = conn.space_center
vessel: Vessel = space_center.active_vessel


# set up the stage monitor
stage_monitor = threading.Thread(target=stageMonitor.monitor, args=(vessel,))
stage_monitor.start()

# get to the orbit
toOrbit1.engage(conn, 0.5)


# mun transfer burn
munTransfer.engage(conn)
time_to_warp = (
    vessel.orbit.next_orbit.time_to_periapsis + vessel.orbit.time_to_soi_change
)
space_center.warp_to(
    space_center.ut + time_to_warp - 60 * 5
)  # 5 minutes before periapsis of mun encounter

# START OF NEW FILE

stage_monitor.do_run = False

# running experiments
for exp in vessel.parts.experiments:
    exp.run()
    sleep(3)
    exp.transmit()
    sleep(3)

while vessel.orbit.body.name != "Kerbin":
    space_center.rails_warp_factor = 5

space_center.rails_warp_factor = 0

vessel.control.activate_next_stage()

vessel.auto_pilot.engage()
vessel.auto_pilot.reference_frame = vessel.orbital_reference_frame
vessel.auto_pilot.target_direction = (0, 1, 0)

periapsisStream = conn.add_stream(getattr, vessel.orbit, "periapsis_altitude")

for engine in vessel.parts.engines:
    engine.active = True

sleep(5)

vessel.control.throttle = 1.0

while periapsisStream() < 65000:
    # print("waiting")
    sleep(0.1)

vessel.control.throttle = 0

timeToPeriapsisStream = conn.add_stream(getattr, vessel.orbit, "time_to_periapsis")


while timeToPeriapsisStream() > 100:
    space_center.rails_warp_factor = 5

space_center.rails_warp_factor = 0

vessel.auto_pilot.engage()
vessel.auto_pilot.reference_frame = vessel.orbital_reference_frame
vessel.auto_pilot.target_direction = (0, -1, 0)

apoapsisStream = conn.add_stream(getattr, vessel.orbit, "apoapsis_altitude")

while apoapsisStream() > 65000:
    while timeToPeriapsisStream() > 150 and apoapsisStream() > 65000:
        sleep(0.1)
    space_center.rails_warp_factor = 0
    while timeToPeriapsisStream() > 90 and apoapsisStream() > 65000:
        sleep(0.1)
    vessel.auto_pilot.engage()
    vessel.auto_pilot.reference_frame = vessel.orbital_reference_frame
    vessel.auto_pilot.target_direction = (0, -1, 0)
    flag = True
    while flag:
        vessel.control.throttle = 1
        sleep(0.1)
        if timeToPeriapsisStream() > 100 or apoapsisStream() <= 65000:
            flag = False
    vessel.control.throttle = 0
    sleep(1)
    space_center.rails_warp_factor = 7


def Vec3Abs(t: tuple) -> float:
    return math.sqrt(t[0] ** 2 + t[1] ** 2 + t[2] ** 2)


Sun = vessel.orbit.body.orbit.body
Kerbin = Sun.satellites[2]
KerbinRf = Kerbin.reference_frame
are_sp_gone = False

while Vec3Abs(vessel.velocity(KerbinRf)) > 500:
    vessel.auto_pilot.engage()
    vessel.auto_pilot.reference_frame = vessel.orbital_reference_frame
    vessel.auto_pilot.target_direction = (0, -1, 0)
    vessel.control.throttle = 1
    if not are_sp_gone and Vec3Abs(vessel.position(KerbinRf)) < 45_000 + 600_000:
        are_sp_gone = True
        vessel.auto_pilot.target_direction = (0, 1, 0)
        sleep(2)
        vessel.control.throttle = 0
        sleep(2)
        vessel.control.activate_next_stage()
        vessel.control.activate_next_stage()


vessel.control.throttle = 0

sleep(1)
# vessel.control.activate_next_stage()

vessel.control.activate_next_stage()

vessel.parts.parachutes[0].deploy()
