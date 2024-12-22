import krpc
import threading
import stageMonitor
import toOrbit
import munTransfer
import orbitMun
import returnHome
import math
from time import sleep

conn = krpc.connect()
space_center = conn.space_center
vessel = space_center.active_vessel

# set up the stage monitor
stage_monitor = threading.Thread(target=stageMonitor.monitor, args=(vessel,))
stage_monitor.start()

# get to the orbit
toOrbit.engage(conn)

# mun transfer burn
munTransfer.engage(conn)
time_to_warp = (
    vessel.orbit.next_orbit.time_to_periapsis + vessel.orbit.time_to_soi_change
)
space_center.warp_to(
    space_center.ut + time_to_warp - 60 * 5
)  # 5 minutes before periapsis of mun encounter

# return to Kerbin from the Mun
returnHome.engage(conn)
