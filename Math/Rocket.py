from Vector import Vector
from Constants import *
from Functions import pressure, density, calculate_apocenter
from math import pi, sqrt
from Satellite import Satellite


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
        Mun: Satellite,
        stages: list[Stage] = [],
    ):
        self.x = x
        self.y = y
        self.stages = stages
        self.angle_to_radius = 0
        self.Force = Vector()
        self.is_engine_off = False
        self.acceleration = Vector()
        self.velocity = Vector(0, 0)
        self.Mun = Mun

    def set_angle_function(self, angle_function, low: float, high: float):
        self.low = low
        self.high = high
        self.angle_function = angle_function

    def get_lunar_gravity(self) -> Vector:
        d = self.Mun - self
        if d.length() > self.SOI:
            return Vector()
        return Vector(
            self.Mun.GRAVITY_PARAMETER * self.get_mass() / d.length() ** 2, 0
        ).turn_by_angle(d.angle())

    def get_gravity(self) -> Vector:
        return -Vector(
            GRAVITY_PARAMETER * self.get_mass() / (self.length() ** 2), 0
        ).turn_by_angle(self.angle())

    def get_drag(self) -> Vector:
        if self.length() > 70_000:
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
        if self.length() > 70_000:
            return Vector(
                self.stages[0].thrust_vacuum,
                0,
            ).turn_by_angle(self.angle_to_radius + self.angle())
        return Vector(
            self.stages[0].thrust_vacuum
            + (self.stages[0].thrust_earth - self.stages[0].thrust_vacuum)
            * pressure(self.length() - KERBIN_RADIUS),
            0,
        ).turn_by_angle(self.angle_to_radius + self.angle())

    def distance_to_mun(self) -> float:
        return (self - self.Mun).length()

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
        self.Mun.update_position()
        if self.stages[0].fuel_mass < 0.5 and not self.is_engine_off:
            self.stage_disattach()
        if calculate_apocenter(self, self.velocity) >= APOCENTER + 1000:
            self.is_engine_off = True

        if APOCENTER - self.length() < 1200:
            self.is_engine_off = False

        self.angle_to_radius = self.angle_function(self.length(), self.low, self.high)
        self.Force = self.get_gravity() + self.get_thrust() + self.get_drag()
        self.acceleration = self.Force / self.get_mass()
        self.velocity += self.acceleration * dt
        self.add_vector(self.velocity * dt)
        if not self.is_engine_off:
            self.update_mass()
        return self.length()

    def update_orbit_setup(self):
        self.Mun.update_position()
        if self.stages[0].fuel_mass < 0.5 and not self.is_engine_off:
            self.stage_disattach()

        self.Force = self.get_gravity() + self.get_thrust()
        self.acceleration = self.Force / self.get_mass()
        self.velocity += self.acceleration * dt
        self.add_vector(self.velocity * dt)
        if not self.is_engine_off:
            self.update_mass()
        return self.length()

    def update_orbit(self):
        self.Mun.update_position()
        if self.stages[0].fuel_mass < 0.5 and not self.is_engine_off:
            self.stage_disattach()

        self.Force = self.get_gravity() + self.get_thrust()
        self.acceleration = self.Force / self.get_mass()
        self.velocity += self.acceleration * dt
        self.add_vector(self.velocity * dt)
        if not self.is_engine_off:
            self.update_mass()
        return self.length()

    def mun_transfer_check(self):
        a = (self.length() + self.Mun.length() - 40_000) / 2
        t = 2 * pi * sqrt(a**3 / GRAVITY_PARAMETER)
        Mun = self.Mun.position_in(t)
        pos = -self / self.length() * (self.Mun.length() - 40_000)
        if (Mun - pos).length() < 50_000:
            self.is_engine_off = False
            return True
        return False

    def mun_transfer(self):
        self.Force = self.get_gravity() + self.get_thrust()
        self.acceleration = self.Force / self.get_mass()
        self.velocity += self.acceleration * dt
        self.add_vector(self.velocity * dt)
        self.Mun.update_position()
        if (
            not self.is_engine_off
            and calculate_apocenter(self, self.velocity) > self.Mun.length() - 40_000
        ):
            self.is_engine_off = True
        if not self.is_engine_off:
            self.update_mass()
