from Vector import Vector
from Constants import *
from Functions import pressure, angle, density, calculate_apogee
from math import pi


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
        self.angle_to_radius = 0
        self.Force = Vector()
        self.is_engine_off = False
        self.acceleration = Vector()
        self.velocity = Vector()

    def get_gravity(self) -> Vector:
        return -Vector(
            GRAVITY_PARAMETER * self.get_mass() / (self.length() ** 2), 0
        ).turn_by_angle(self.angle())

    def get_drag(self) -> Vector:
        return Vector()
        return -Vector(
            ROCKET_D
            * 0.008
            * self.get_mass()
            * self.velocity.length() ** 2
            * density(self.length() - KERBIN_RADIUS)
            / 2,
            0,
        ).turn_by_angle(self.velocity.angle())

    def get_thrust(self) -> Vector:
        if self.stages[0].fuel_mass <= 0 or self.is_engine_off:
            return Vector()
        return Vector(
            self.stages[0].thrust_vacuum
            + (self.stages[0].thrust_earth - self.stages[0].thrust_vacuum)
            * pressure(self.length() - KERBIN_RADIUS),
            0,
        ).turn_by_angle(self.angle_to_radius + self.angle())

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

    def add_vector(self, v: Vector):
        self.x += v.x
        self.y += v.y

    def get_mass(self) -> float:
        return sum(map(lambda x: x.get_mass(), self.stages))

    def update_launch(self) -> float:
        if self.stages[0].fuel_mass < 0.5 and not self.is_engine_off:
            self.stage_disattach()
        if calculate_apogee(self, self.velocity) >= APOGEE:
            self.is_engine_off = True

        self.angle_to_radius = angle(self.length())
        self.Force = self.get_gravity() + self.get_drag() + self.get_thrust()
        self.acceleration = self.Force / self.get_mass()
        self.velocity += self.acceleration * dt
        self.add_vector(self.velocity * dt)
        if not self.is_engine_off:
            self.update_mass()
        return self.length()
