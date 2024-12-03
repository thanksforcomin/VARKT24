from Vector import Vector
from Constants import *
from Functions import pressure, density, calculate_apocenter
from math import pi, sqrt


class NoStagesLeftException(Exception): ...


class Stage:
    def __init__(
        self,
        end_mass: float,
        start_mass: float,
        fuel_usage: float,
        thrust_earth: float,
        thrust_vacuum: float,
    ):
        self.end_mass = end_mass
        self.start_mass = start_mass
        self.fuel_usage = fuel_usage
        self.thrust_earth = thrust_earth
        self.thrust_vacuum = thrust_vacuum


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
        self.current_mass = stages[0].start_mass
        self.angle_to_radius = 0
        self.Force = Vector()
        self.is_engine_off = False
        self.acceleration = Vector()
        self.velocity = Vector(0, 0)

    def use_fuel(self) -> int:
        if self.is_engine_off or self.current_mass - self.stages[0].end_mass < 0.1:
            return -1
        self.current_mass -= self.stages[0].fuel_usage * dt
        return 0

    def set_angle_function(self, angle_function, low: float, high: float):
        self.low = low
        self.high = high
        self.angle_function = angle_function

    def get_gravity(self) -> Vector:
        return -Vector(
            GRAVITY_PARAMETER * self.get_mass() / (self.length() ** 2), 0
        ).turn_by_angle(self.angle())

    def get_drag(self) -> Vector:
        if self.length() > 20_000:
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
        if self.current_mass <= self.stages[0].end_mass or self.is_engine_off:
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
            self.current_mass = self.stages[0].start_mass
        else:
            raise NoStagesLeftException

    def add_vector(self, v: Vector):
        self.x += v.x
        self.y += v.y

    def get_mass(self) -> float:
        return self.current_mass

    def update_launch(self) -> float:
        if calculate_apocenter(self, self.velocity) >= APOCENTER:
            self.is_engine_off = True
        self.angle_to_radius = self.angle_function(self.length(), self.low, self.high)
        self.Force = self.get_gravity() + self.get_thrust() + self.get_drag()
        self.acceleration = self.Force / self.get_mass()
        self.velocity += self.acceleration * dt
        self.add_vector(self.velocity * dt)
        res = self.use_fuel()
        if res == -1 and not self.is_engine_off:
            self.is_engine_off = True
            self.stage_disattach()
        return self.length()

    def update_orbit_setup(self):
        self.Force = self.get_gravity() + self.get_thrust()
        self.acceleration = self.Force / self.get_mass()
        self.velocity += self.acceleration * dt
        self.add_vector(self.velocity * dt)
        res = self.use_fuel()
        if res == -1 and not self.is_engine_off:
            self.is_engine_off = True
        return self.length()

    def update_orbit(self):

        self.Force = self.get_gravity() + self.get_thrust()
        self.acceleration = self.Force / self.get_mass()
        self.velocity += self.acceleration * dt
        self.add_vector(self.velocity * dt)
        res = self.use_fuel()
        if res == -1 and not self.is_engine_off:
            self.stage_disattach()
        return self.length()
