from .rigid_body import RigidBody

from .math.vector import Vector2


class SystemState:
    def __init__(self) -> None:
        self.bodies: list[RigidBody] = []
    
    def local_to_world(self, body: int, local_point: Vector2) -> Vector2:
        return local_point.rotate(self.bodies[body].angle) + self.bodies[body].position
    
    def velocity_at_point(self, body: int, local_point: Vector2) -> Vector2:
        return self.bodies[body].velocity + self.bodies[body].angular_velocity * (self.local_to_world(body, local_point) - self.bodies[body].position)

    def apply_force(self, body: int, force: Vector2, local_point: Vector2) -> None:
        self.bodies[body].force += force
        self.bodies[body].torque += force.cross(self.local_to_world(body, local_point) - self.bodies[body].position)