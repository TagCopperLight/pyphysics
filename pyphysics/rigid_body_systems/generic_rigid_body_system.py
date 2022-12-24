from .rigid_body_system import RigidBodySystem
from ..solvers.ode_solver import OdeSolver


class GenericRigidBodySystem(RigidBodySystem):
    def __init__(self) -> None:
        super().__init__()
        self.ode_solver: OdeSolver

    def process(self, dt: float, steps: int) -> None:
        self.populate_system_state()
        
        for _ in range(steps):
            self.ode_solver.start(self.system_state, dt / steps)

            while self.ode_solver.step(self.system_state):
                self.process_forces()
                self.ode_solver.solve(self.system_state)
            
            self.ode_solver.end()

        for i in range(len(self.bodies)):
            self.bodies[i].position = self.system_state.positions[i]
            self.bodies[i].velocity = self.system_state.velocities[i]
            
            self.bodies[i].angle = self.system_state.angles[i]
            self.bodies[i].angular_velocity = self.system_state.angular_velocities[i]