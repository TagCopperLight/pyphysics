from ..math.vector import Vector2


class RigidBody:
    def __init__(self) -> None:
        self.position: Vector2
        self.velocity: Vector2

        self.mass: float

        self.angle: float
        self.angular_velocity: float

        self.inertia: float
    
    def local_to_world(self, point: Vector2) -> Vector2:
        ...

    def world_to_local(self, point: Vector2) -> Vector2:
        ...

    def energy(self) -> float:
        ...