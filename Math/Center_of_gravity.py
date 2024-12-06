from Satellite import Satellite


class Celestial:
    def __init__(self, radius: float, mass: float, SOI: float):
        self.radius = radius
        self.mass = mass
        self.SOI = SOI
        self.GRAVITY_PARAMETER = mass * 6.67430 * 10**-11
