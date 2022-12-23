from ..system_state import SystemStateObject


class ForceGenerator:
    def __init__(self) -> None:
        raise NotImplementedError

    def apply(self, system_state: SystemStateObject) -> None:
        raise NotImplementedError