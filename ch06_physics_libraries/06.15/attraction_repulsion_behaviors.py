# https://natureofcode.com/physics-libraries/#attraction-and-repulsion-behaviors

from toxi.physics2d import VerletPhysics2D, VerletParticle2D, VerletSpring2D

from attractor_pl import Attractor
from particle_pl import Particle


def setup():
    global physics, monospace, cluster
    size(640, 240)

    # Create a Toxiclibs.js Verlet physics world.
    physics = VerletPhysics2D()




def draw():
    global ...

    # Must update the physics.
    physics.update()
   



