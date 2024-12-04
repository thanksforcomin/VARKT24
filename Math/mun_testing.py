from Satellite import Satellite
from Constants import dt

mun = Satellite(12_000_000, 0, 200_000, 9.7599066 * 10**22, 2_429_559)
t = 0

while True:
    mun.update_position()
    if abs(int(t) - t) < dt and int(t) % 1000 == 0:
        print(int(t), mun.length(), mun)
    t += dt
