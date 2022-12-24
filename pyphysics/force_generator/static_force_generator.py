from ..system_state import SystemState
from .force_generator import ForceGenerator
from ..rigid_body import RigidBody

from ..math.vector import Vector2


class StaticForceGenerator(ForceGenerator):
    def __init__(self) -> None:
        self.position = Vector2()
        self.force = Vector2()

        self.body: RigidBody

    def apply(self, system_state: SystemState) -> None:
        system_state.apply_force(self.body, self.force, self.position)