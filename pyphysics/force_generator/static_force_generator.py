#pyright: reportShadowedImports=false
from ..system_state import SystemStateObject
from .force_generator import ForceGenerator
from ..math.vector import Vector2


class StaticForceGenerator(ForceGenerator):
    def __init__(self) -> None:
        self.position = Vector2()
        self.force = Vector2()

    def apply(self, system_state: SystemStateObject) -> None:
        system_state.apply_force(self.force, self.position)