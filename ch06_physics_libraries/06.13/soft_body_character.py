# https://natureofcode.com/physics-libraries/#a-soft-body-character

from toxi.geom import Vec2D, Rect
from toxi.physics2d import VerletPhysics2D
from toxi.physics2d.behaviors import GravityBehavior2D

from particle_pl import Particle
from spring_pl import Spring


def setup():
    global physics, particles, springs  # Store all particles & springs in lists.
    size(640, 240)

    # Create a Toxiclibs.js Verlet physics world.
    physics = VerletPhysics2D()
    physics.setWorldBounds(Rect(0, 0, width, height))
    physics.addBehavior(GravityBehavior2D(Vec2D(0, 0.5)))

    # Create the vertex positions of the character as particles.
    particles = [
      # Particles at vertices of the character.
      Particle(physics, 200, 25, 16),
      Particle(physics, 400, 25, 16),
      Particle(physics, 350, 125, 16),
      Particle(physics, 400, 225, 16),
      Particle(physics, 200, 225, 16),
      Particle(physics, 250, 125, 16),
    ]

    # Connect the vertices with springs.
    springs = [
      # Springs connecting vertices of the character.
      Spring(physics, particles[0], particles[1]),
      Spring(physics, particles[1], particles[2]),
      Spring(physics, particles[2], particles[3]),
      Spring(physics, particles[3], particles[4]),
      Spring(physics, particles[4], particles[5]),
      Spring(physics, particles[5], particles[0]),
      # Three internal springs!
      Spring(physics, particles[5], particles[2]),
      Spring(physics, particles[0], particles[3]),
      Spring(physics, particles[1], particles[4]),
    ]


def draw():
    # Must update the physics.
    physics.update()

    background(255)

    # Draw the character as one shape.
    fill(127)
    stroke(0)
    stroke_weight(2)
    begin_shape()
    for particle in particles:
        vertex(particle.x, particle.y)
    end_shape(CLOSE)

    # Mouse interaction.
    if is_mouse_pressed:
        # First lock the particle, then set the x and y, then unlock() it.
        particles[0].lock()
        particles[0].x = mouse_x
        particles[0].y = mouse_y
        particles[0].unlock()
