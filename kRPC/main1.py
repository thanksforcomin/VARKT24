import krpc
import threading
import stageMonitor
import toOrbit
import munTransfer


conn = krpc.connect()
space_center = conn.space_center
vessel = space_center.active_vessel


# set up the stage monitor
threading.Thread(target=stageMonitor.monitor, args=(vessel))

# get to the orbit
toOrbit.engage(conn, 0.5)


# mun transfer burn
munTransfer.engage(conn)
time_to_warp = (
    vessel.orbit.next_orbit.time_to_periapsis + vessel.orbit.time_to_soi_change
)
space_center.warp_to(
    space_center.ut + time_to_warp - 60 * 5
)  # 5 minutes before periapsis of mun encounter
