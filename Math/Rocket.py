from Vector import Vector
from Constants import dt, KERBIN_RADIUS
from Functions import pressure, angle


class NoStagesLeftException(Exception): ...


class Stage:
    def __init__(
        self,
        solid_mass: float,
        fuel_mass: float,
        fuel_usage: float,
        thrust_earth: float,
        thrust_vacuum: float,
    ):
        self.solid_mass = solid_mass
        self.fuel_mass = fuel_mass
        self.fuel_usage = fuel_usage
        self.thrust_earth = thrust_earth
        self.thrust_vacuum = thrust_vacuum

    def get_mass(self):
        return self.solid_mass + self.fuel_mass

    def use_fuel(self):
        if self.fuel_mass <= 0:
            return -1
        self.fuel_mass -= self.fuel_usage * dt
        return 0

    def __repr__(self):
        return f"(fuel={self.fuel_mass}; mass={self.fuel_mass + self.solid_mass}; thrust={self.thrust_earth})"


class Rocket(Vector):
    def __init__(
        self,
        x: float,
        y: float,
        stages: list[Stage] = [],
    ):
        self.x = x
        self.y = y
        self.stages = stages

    def add_stage(self, stage: Stage):
        self.stages.append(stage)

    def stage_disattach(self):
        if len(self.stages) > 1:
            self.stages.pop(0)
        else:
            raise NoStagesLeftException

    def update_mass(self) -> int:
        if len(self.stages) == 0:
            return -1
        return self.stages[0].use_fuel()

    def addVector(self, v: Vector):
        self.x += v.x
        self.y += v.y

    def get_mass(self) -> float:
        return sum(map(lambda x: x.get_mass(), self.stages))

    def get_thrust(self) -> Vector:
        if self.stages[0].fuel_mass <= 0:
            return Vector(0, 0)
        return Vector(
            self.stages[0].thrust_vacuum
            + (self.stages[0].thrust_earth - self.stages[0].thrust_vacuum)
            * pressure(self.length() - KERBIN_RADIUS),
            0,
        ).turn_by_angle(self.angle() + angle(self.length()))
