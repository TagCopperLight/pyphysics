from ..system_state import SystemStateObject


class ForceGenerator:
    def __init__(self) -> None:
        ...

    def apply(self, system_state: SystemStateObject) -> None:
        ...