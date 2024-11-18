import krpc

print(1)

try:
    conn = krpc.connect(address="192.168.57.165", rpc_port=50000, stream_port=50001)
    print(conn)
except Exception as e:
    print(e)

vessel = conn.space_center.active_vessel

print(vessel)

Sun = vessel.orbit.body.orbit.body
Sun_rf = Sun.reference_frame
Kerbin = Sun.satellites[2]
for s in Kerbin.satellites:
    print(s)
