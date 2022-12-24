from ..system_state import SystemState
from .rigid_body import RigidBody
from ..force_generators.force_generator import ForceGenerator

from ..math.vector import Vector2


class RigidBodySystem:
    def __init__(self) -> None:
        self.bodies: list[RigidBody] = []
        self.force_generators: list[ForceGenerator] = []

        self.system_state = SystemState()

    def process(self, dt: float, steps: int) -> None:
        raise NotImplementedError

    def populate_system_state(self) -> None:
        self.system_state.bodies = self.bodies

        for i in range(len(self.bodies)):
            self.system_state.accelerations[i] = Vector2()
            self.system_state.velocities[i] = self.bodies[i].velocity
            self.system_state.positions[i] = self.bodies[i].position

            self.system_state.masses[i] = self.bodies[i].mass
            
            self.system_state.angular_accelerations[i] = 0
            self.system_state.angular_velocities[i] = self.bodies[i].angular_velocity
            self.system_state.angles[i] = self.bodies[i].angle

            self.system_state.inertias[i] = self.bodies[i].inertia
        
    def process_forces(self) -> None:
        for body in self.system_state.bodies:
            index = self.system_state.bodies.index(body)
            
            self.system_state.forces[index] = Vector2()
            self.system_state.torques[index] = 0
        
        for generator in self.force_generators:
            generator.apply(self.system_state)