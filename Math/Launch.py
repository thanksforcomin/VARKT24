from Constants import *
from Vector import Vector
from Rocket import Rocket, Stage, NoStagesLeftException
from math import pi
from Functions import *

height = 0
velocity = Vector(0, 0)
acceleration = Vector(0, 0)
stage1 = Stage(MASS_SOLID_1, MASS_FUEL_1, FUEL_USAGE_1, THRUST_EARTH_1, THRUST_VACUUM_1)
stage2 = Stage(MASS_SOLID_2, MASS_FUEL_2, FUEL_USAGE_2, THRUST_EARTH_2, THRUST_VACUUM_2)
stage3 = Stage(MASS_SOLID_3, MASS_FUEL_3, FUEL_USAGE_3, THRUST_EARTH_3, THRUST_VACUUM_3)
rocket = Rocket(0, KERBIN_RADIUS, [stage1, stage2, stage3])
is_engine_on = True
allow = False
dv = 0
t = 0
times_under_surface = 0
print(rocket)
prev = 0

while rocket.length() < APOGEE:
    height = max(height, rocket.update_launch() - KERBIN_RADIUS)
    if abs(int(t) - t) < 0.05:
        print(int(t), rocket, rocket.length())
    t += dt

print(t, height, rocket, rocket.angle(velocity))

print("END")
