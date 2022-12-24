from .rigid_body_system import RigidBodySystem


class GenericRigidBodySystem(RigidBodySystem):
    def __init__(self) -> None:
        ...

    def process(self, dt: float, steps: int) -> None:
        ...