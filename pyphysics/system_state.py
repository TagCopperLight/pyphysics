#pyright: reportShadowedImports=false
from .math import Vector2

class SystemStateObject:
    def __init__(self) -> None:
        # Position
        self.position: Vector2
        self.velocity: Vector2
        self.acceleration: Vector2

        self.force: Vector2
        self.mass: float

        # Rotation
        self.angle: float
        self.angular_velocity: float
        self.angular_acceleration: float

        self.torque: float
        self.inertia: float
    
    def local_to_world(self, local_point: Vector2) -> Vector2:
        return local_point.rotate(self.angle) + self.position
    
    def velocity_at_point(self, local_point: Vector2) -> Vector2:
        return self.velocity + self.angular_velocity * (self.local_to_world(local_point) - self.position)

    def apply_force(self, force: Vector2, local_point: Vector2) -> None:
        self.force += force
        self.torque += force.cross(self.local_to_world(local_point) - self.position)
        