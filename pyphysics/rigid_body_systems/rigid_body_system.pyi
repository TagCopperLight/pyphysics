from ..system_state import SystemState
from ..rigid_body_systems.rigid_body import RigidBody


class RigidBodySystem:
    def __init__(self) -> None:
        self.bodies: list[RigidBody]

        self.system_state: SystemState

    def process(self, dt: float, steps: int) -> None:
        ...

    def populate_system_state(self) -> None:
        ...
        
    def process_forces(self) -> None:
        ...