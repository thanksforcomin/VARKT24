from Satellite import Satellite
from Constants import dt

mun = Satellite(12_000_000, 0, 200_000, 9.7599066 * 10**22, 2_429_559)
t = 5000
pos = mun.position_in(t)

for _ in range(int(t / dt)):
    mun.update_position()

print((mun - pos).length())
