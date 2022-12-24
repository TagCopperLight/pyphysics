from .rigid_body import RigidBody

from .math.vector import Vector2


class SystemState:
    def __init__(self) -> None:
        self.bodies: list[RigidBody]

    def local_to_world(self, body: int, local_point: Vector2) -> Vector2:
        ...

    def velocity_at_point(self, body: int, local_point: Vector2) -> Vector2:
        ...

    def apply_force(self, body: int, force: Vector2, local_point: Vector2) -> None:
        ...