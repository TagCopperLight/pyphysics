from ..math.vector import Vector2


class RigidBody:
    def __init__(self) -> None:
        self.position = Vector2()
        self.velocity = Vector2()

        self.mass: float

        self.angle: float
        self.angular_velocity: float

        self.inertia: float
    
    def local_to_world(self, point: Vector2) -> Vector2:
        return point.rotate(self.angle) + self.position

    def world_to_local(self, point: Vector2) -> Vector2:
        return (point - self.position).rotate(-self.angle)

    def energy(self) -> float:
        return 0.5 * self.mass * self.velocity.length_squared() + 0.5 * self.inertia * self.angular_velocity ** 2