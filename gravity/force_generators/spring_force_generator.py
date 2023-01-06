from ..system_state import SystemState
from .force_generator import ForceGenerator
from ..rigid_body_systems.rigid_body import RigidBody

from ..math.vector import Vector2


class SpringForceGenerator(ForceGenerator):
    def __init__(self, rest_length: float, spring_constant: float, damping: float, body1: RigidBody, body2: RigidBody, local_pos1: Vector2 = Vector2(), local_pos2: Vector2 = Vector2()) -> None:
        self.rest_length: float = rest_length
        self.spring_constant: float = spring_constant
        self.damping: float = damping

        self.body_1: RigidBody = body1
        self.body_2: RigidBody = body2

        self.local_position_1: Vector2 = local_pos1
        self.local_position_2: Vector2 = local_pos2

    def apply(self, system_state: SystemState) -> None:
        position1 = system_state.local_to_world(self.body_1, self.local_position_1)
        position2 = system_state.local_to_world(self.body_2, self.local_position_2)

        velocity1 = system_state.velocity_at_point(self.body_1, self.local_position_1)
        velocity2 = system_state.velocity_at_point(self.body_2, self.local_position_2)

        delta = position2 - position1

        delta_length = delta.length()

        if delta_length != 0:
            delta /= delta_length
        else:
            delta = Vector2(1, 0)

        delta_velocity = velocity2 - velocity1

        velocity = delta.dot(delta_velocity)
        length = delta_length - self.rest_length

        force = delta * (self.spring_constant * length + self.damping * velocity)

        system_state.apply_force(self.body_1, force, self.local_position_1)
        system_state.apply_force(self.body_2, -force, self.local_position_2)

