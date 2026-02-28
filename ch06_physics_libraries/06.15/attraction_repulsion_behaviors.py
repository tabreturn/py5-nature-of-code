# https://natureofcode.com/physics-libraries/#attraction-and-repulsion-behaviors

from toxi.geom import Rect
from toxi.physics2d import VerletPhysics2D

from attractor_pl import Attractor
from particle_pl import Particle


def setup():
    global physics, particles, attractor
    size(640, 240)

    # Create a Toxiclibs.js Verlet physics world.
    physics = VerletPhysics2D()
    physics.setWorldBounds(Rect(0, 0, width, height))
    physics.setDrag(0.01)

    particles = [
      Particle(physics, random(width), random(height), 4)
      for _ in range(50)
    ]

    attractor = Attractor(physics, width / 2, height / 2, 16)


def draw():
    background(255)

    # Must update the physics.
    physics.update()

    attractor.show()

    for particle in particles:
        particle.show()

    if is_mouse_pressed:
        attractor._p.lock()
        attractor.set(mouse_x, mouse_y)
    else:
        attractor._p.unlock()
