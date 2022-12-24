from ..system_state import SystemState


class RigidBodySystem:
    def __init__(self) -> None:
        self.system_state: SystemState

    def process(self, dt: float, steps: int) -> None:
        ...

    def populate_system_state(self) -> None:
        ...

    def process_forces(self) -> None:
        ...