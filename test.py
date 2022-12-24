import time

from pyphysics.rigid_body_systems.generic_rigid_body_system import GenericRigidBodySystem
from pyphysics.solvers.euler_ode_solver import EulerOdeSolver
from pyphysics.force_generators.gravity_force_generator import GravityForceGenerator
from pyphysics.rigid_body_systems.rigid_body import RigidBody

system = GenericRigidBodySystem()
system.ode_solver = EulerOdeSolver()
system.force_generators = [GravityForceGenerator()]
body = RigidBody()
body.mass = 5
body.angle = 0
body.angular_velocity = 0
body.inertia = 5
system.bodies.append(body)

while True:
    system.process(1, 1)
    print(system.bodies[0].position)
    time.sleep(1)
