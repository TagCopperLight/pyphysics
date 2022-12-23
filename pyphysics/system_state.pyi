from .math.vector import Vector2


class SystemStateObject:
    def __init__(self) -> None:
        self.position: Vector2
        self.force: Vector2

        self.mass: float

    def local_to_world(self, local_point: Vector2) -> Vector2:
        ...

    def velocity_at_point(self, local_point: Vector2) -> Vector2:
        ...

    def apply_force(self, force: Vector2, local_point: Vector2) -> None:
        ...