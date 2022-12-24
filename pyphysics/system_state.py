from .rigid_body_systems.rigid_body import RigidBody

from .math.vector import Vector2


class SystemState:
    def __init__(self) -> None:
        self.bodies: list[RigidBody] = []

        self.positions: list[Vector2] = []
        self.velocities: list[Vector2] = []
        self.accelerations: list[Vector2] = []
        self.forces: list[Vector2] = []

        self.angles: list[float] = []
        self.angular_velocities: list[float] = []
        self.angular_accelerations: list[float] = []
        self.torques: list[float] = []
    
    def local_to_world(self, body: RigidBody, local_point: Vector2) -> Vector2:
        index = self.bodies.index(body)
        return local_point.rotate(self.angles[index]) + self.positions[index]
    
    def velocity_at_point(self, body: RigidBody, local_point: Vector2) -> Vector2:
        index = self.bodies.index(body)
        return self.velocities[index] + self.angular_velocities[index] * (self.local_to_world(body, local_point) - self.positions[index])

    def apply_force(self, body: RigidBody, force: Vector2, local_point: Vector2) -> None:
        index = self.bodies.index(body)
        self.forces[index] += force
        self.torques[index] += force.cross(self.local_to_world(body, local_point) - self.positions[index])