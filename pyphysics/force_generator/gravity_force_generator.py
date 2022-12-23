from .force_generator import ForceGenerator
from ..system_state import SystemStateObject
from ..math.vector import Vector2


class GravityForceGenerator(ForceGenerator):
    def __init__(self) -> None:
        self.gravity = Vector2(0, -9.81)

    def apply(self, system_state: SystemStateObject) -> None:
        system_state.force += self.gravity * system_state.mass