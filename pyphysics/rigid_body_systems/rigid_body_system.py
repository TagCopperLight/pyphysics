from ..system_state import SystemState
from .rigid_body import RigidBody
from ..force_generators.force_generator import ForceGenerator

from ..math.vector import Vector2


class RigidBodySystem:
    def __init__(self) -> None:
        self.bodies: list[RigidBody] = []
        self.force_generators: list[ForceGenerator] = []

        self.system_state = SystemState()

    def process(self, dt: float, steps: int) -> None:
        raise NotImplementedError

    def populate_system_state(self) -> None:
        self.system_state.bodies = self.bodies
        
    def process_forces(self) -> None:
        for body in self.system_state.bodies:
            body.force = Vector2()
            body.torque = 0
        
        for generator in self.force_generators:
            generator.apply(self.system_state)