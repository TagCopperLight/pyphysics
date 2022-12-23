#pyright: reportShadowedImports=false
from ..system_state import SystemStateObject
from .force_generator import ForceGenerator


class StaticForceGenerator(ForceGenerator):
    def __init__(self) -> None:
        ...

    def apply(self, system_state: SystemStateObject) -> None:
        ...