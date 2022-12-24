from .rigid_body_systems.rigid_body import RigidBody

from .math.vector import Vector2


class SystemState:
    def __init__(self) -> None:
        self.bodies: list[RigidBody] = []
    
    def local_to_world(self, body: RigidBody, local_point: Vector2) -> Vector2:
        return local_point.rotate(body.angle) + body.position
    
    def velocity_at_point(self, body: RigidBody, local_point: Vector2) -> Vector2:
        return body.velocity + body.angular_velocity * (self.local_to_world(body, local_point) - body.position)

    def apply_force(self, body: RigidBody, force: Vector2, local_point: Vector2) -> None:
        body.force += force
        body.torque += force.cross(self.local_to_world(body, local_point) - body.position)