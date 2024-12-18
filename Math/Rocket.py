from Vector import Vector
from Constants import *
from Functions import pressure, density, calculate_apocenter, cd
from math import pi, sqrt
from Satellite import Satellite
from Center_of_gravity import Celestial


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

    def use_fuel(self, throttle: float):
        if self.fuel_mass <= 0:
            return -1
        self.fuel_mass -= self.fuel_usage * dt * throttle
        return 0

    def __repr__(self):
        return f"(fuel={self.fuel_mass}; mass={self.fuel_mass + self.solid_mass}; thrust={self.thrust_earth})"


class Rocket(Vector):
    MUN_DELTA_VECTOR = Vector(-11843727.359355858, 4389155.821897084)

    def __init__(
        self,
        x: float,
        y: float,
        Mun: Satellite,
        center: Celestial,
        stages: list[Stage] = [],
    ):
        self.x = x
        self.y = y
        self.stages = stages
        self.angle_to_radius = 0
        self.Force = Vector()
        self.is_engine_off = False
        self.center = center
        self.acceleration = Vector()
        self.velocity = Vector(0, 0)
        self.Mun = Mun
        self.MUN_DELTA_VECTOR = Vector(-7258411.322963381, 9749851.296890123)
        self.throttle = 1

    def change_center_to_satellite(self) -> None:
        d = self - self.Mun
        self.center = Celestial(self.Mun.radius, self.Mun.mass, self.Mun.SOI)
        self.x = d.x
        self.y = d.y
        self.angle_to_radius = pi

    def set_angle_function(self, angle_function, low: float, high: float) -> None:
        self.low = low
        self.high = high
        self.angle_function = angle_function

    def get_lunar_gravity(self) -> Vector:
        d = self.Mun - self
        if d.length() > self.Mun.SOI:
            return Vector()
        return Vector(
            self.Mun.GRAVITY_PARAMETER * self.get_mass() / d.length() ** 2, 0
        ).turn_by_angle(d.angle())

    def get_gravity(self) -> Vector:
        return -Vector(
            self.center.GRAVITY_PARAMETER * self.get_mass() / (self.length() ** 2), 0
        ).turn_by_angle(self.angle())

    def get_drag(self) -> Vector:

        if self.length() > 70_000 + self.center.radius:
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
        if self.length() > 70_000 + self.center.radius:
            return (
                Vector(
                    self.stages[0].thrust_vacuum,
                    0,
                ).turn_by_angle(self.angle_to_radius + self.angle())
                * self.throttle
            )
        return (
            Vector(
                self.stages[0].thrust_vacuum
                + (self.stages[0].thrust_earth - self.stages[0].thrust_vacuum)
                * pressure(self.length() - KERBIN_RADIUS),
                0,
            ).turn_by_angle(self.angle_to_radius + self.angle())
            * self.throttle
        )

    def get_thrust_velocity(self) -> Vector:
        if self.stages[0].fuel_mass <= 0 or self.is_engine_off:
            return Vector()
        if self.length() > 70_000 + self.center.radius:
            return (
                Vector(
                    self.stages[0].thrust_vacuum,
                    0,
                ).turn_by_angle(self.velocity.angle())
                * self.throttle
            )
        return (
            Vector(
                self.stages[0].thrust_vacuum
                + (self.stages[0].thrust_earth - self.stages[0].thrust_vacuum)
                * pressure(self.length() - KERBIN_RADIUS),
                0,
            ).turn_by_angle(self.velocity.angle())
            * self.throttle
        )

    def get_thrust_opposing_velocity(self) -> Vector:
        return -self.get_thrust_velocity()

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
        return self.stages[0].use_fuel(self.throttle)

    def add_vector(self, v: Vector):
        self.x += v.x
        self.y += v.y

    def get_mass(self) -> float:
        return sum(map(lambda x: x.get_mass(), self.stages))

    def update_launch(self) -> float:
        if self.Mun:
            self.Mun.update_position()
        if self.stages[0].fuel_mass < 0.5 and not self.is_engine_off:
            self.stage_disattach()
        if calculate_apocenter(self, self.velocity, self.center) >= APOCENTER + 1000:
            self.is_engine_off = True

        self.angle_to_radius = self.angle_function(self.length(), self.low, self.high)
        self.Force = self.get_gravity() + self.get_thrust() + self.get_drag()
        self.acceleration = self.Force / self.get_mass()
        self.velocity += self.acceleration * dt
        self.add_vector(self.velocity * dt)
        if not self.is_engine_off:
            self.update_mass()
        return self.length()

    def update_orbit_setup(self) -> float:
        if self.Mun:
            self.Mun.update_position()
        if self.stages[0].fuel_mass < 0.5 and not self.is_engine_off:
            self.stage_disattach()

        if (
            calculate_apocenter(self, self.velocity, self.center) - self.length()
            < DIF_APOGEE
        ):
            self.is_engine_off = False

        self.Force = self.get_gravity() + self.get_thrust_velocity()
        self.acceleration = self.Force / self.get_mass()
        self.velocity += self.acceleration * dt
        self.add_vector(self.velocity * dt)
        if not self.is_engine_off:
            self.update_mass()
        return self.length()

    def update_orbit(self) -> float:
        if self.Mun:
            self.Mun.update_position()
        if self.stages[0].fuel_mass < 0.5 and not self.is_engine_off:
            self.stage_disattach()

        self.Force = self.get_gravity() + self.get_thrust_velocity() + self.get_drag()
        self.acceleration = self.Force / self.get_mass()
        self.velocity += self.acceleration * dt
        self.add_vector(self.velocity * dt)
        if not self.is_engine_off:
            self.update_mass()
        return self.length()

    def landing_orbit(self):
        if self.Mun:
            self.Mun.update_position()
        if self.stages[0].fuel_mass < 0.5 and not self.is_engine_off:
            self.stage_disattach()

        self.Force = (
            self.get_gravity() + self.get_thrust_opposing_velocity() + self.get_drag()
        )
        self.acceleration = self.Force / self.get_mass()
        self.velocity += self.acceleration * dt
        self.add_vector(self.velocity * dt)
        if not self.is_engine_off:
            self.update_mass()
        return self.length()

    def mun_transfer_check(self) -> bool:
        if not self.is_engine_off:
            self.update_mass()
        a = (self.length() + self.Mun.length()) / 2
        t = 26739
        Mun = self.Mun.position_in(t)
        temp = Vector(self.MUN_DELTA_VECTOR.x, self.MUN_DELTA_VECTOR.y).turn_by_angle(
            self.angle()
        )
        pos = self + temp
        if (
            MUN_DIST + self.Mun.radius
            <= (Mun - pos).length()
            < MUN_DIST + 30_000 + self.Mun.radius
            or MUN_DIST < 0
            and (Mun - pos).length() < -MUN_DIST + 30_000
        ):
            self.is_engine_off = False
            print(pos, pos.length())
            return True
        return False

    def mun_transfer(self) -> bool:
        if not self.is_engine_off:
            self.update_mass()
        self.Force = (
            self.get_gravity() + self.get_thrust_velocity() + self.get_lunar_gravity()
        )
        self.acceleration = self.Force / self.get_mass()
        self.velocity += self.acceleration * dt
        self.add_vector(self.velocity * dt)
        self.Mun.update_position()
        if (
            not self.is_engine_off
            and calculate_apocenter(self, self.velocity, self.center)
            > 12_000_000 + MUN_DIST
        ):
            self.is_engine_off = True
        if not self.is_engine_off:
            self.update_mass()
        return False

    def mun_escape(self) -> bool:
        if not self.is_engine_off:
            self.update_mass()
        self.Force = (
            self.get_gravity()
            + self.get_lunar_gravity()
            + self.get_thrust_opposing_velocity()
            + self.get_drag()
        )
        self.acceleration = self.Force / self.get_mass()
        self.velocity += self.acceleration * dt
        self.add_vector(self.velocity * dt)
