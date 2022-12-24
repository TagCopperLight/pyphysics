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