# https://natureofcode.com/physics-libraries/#collision-events

# Note Matter.js uses 'aliases'; for py5 just import Pymunk symbols directly.
from pymunk import Arbiter, Space, Shape
from boundary_pm import Boundary
from particle_pm import Particle

import sys, os; sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from pymunk_constants import *  # Matter.js <-> Pymunk calibration constants.

particles: list[Particle] = []


def setup():
    global wall, engine
    size(640, 240)

    engine = Space()  # Create the engine; Pymunk's "world/engine" is a Space.
    # Change the engine's gravity to point downward.
    engine.gravity = (0, 1.0 * SCALE_GRAVITY)

    wall = Boundary(engine, width / 2, height - 5, width, 10)

    # Matter.js "collisionStart" substitute. 0 is Pymunk default collision_type.
    engine.on_collision(0, 0, begin=handle_collisions)
    # (since we haven't assigned custom types, all shapes are type 0)


def handle_collisions(arbiter: Arbiter, space: Space, _) -> bool:
    shape_a, shape_b = arbiter.shapes

    # Retrieve particles associated with colliding bodies via .particle reference.
    particle_a = getattr(shape_a, 'particle', None)
    particle_b = getattr(shape_b, 'particle', None)

    # If they are both particles, change their color!
    if isinstance(particle_a, Particle) and isinstance(particle_b, Particle):
        particle_a.change()
        particle_b.change()

    return True


def draw():
    background(255)

    engine.step(DT)  # Step the engine forward in time!

    if random() < 0.05:
        particles.append(Particle(engine, random(width), 0))

    # Iterate over a copy to remove particles safely (instead of backwards).
    for particle in particles[:]:
        # Display all the Particle objects.
        particle.show()
        # Remove the Body(+shape) from the world and the list.
        if particle.check_edge():
            particle.remove_body()
            particles.remove(particle)

    wall.show()
