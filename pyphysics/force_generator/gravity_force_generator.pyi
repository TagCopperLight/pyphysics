from .force_generator import ForceGenerator
from ..system_state import SystemStateObject


class GravityForceGenerator(ForceGenerator):
    def __init__(self) -> None:
        ...

    def apply(self, system_state: SystemStateObject) -> None:
        ...