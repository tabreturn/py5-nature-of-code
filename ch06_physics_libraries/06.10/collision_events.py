# https://natureofcode.com/physics-libraries/#collision-events

# Note Matter.js uses 'aliases'; for py5 just import Pymunk symbols directly.
from pymunk import Space
from boundary_pm import Boundary
from particle_pm import Particle

import sys, os; sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from pymunk_constants import *  # Matter.js <-> Pymunk calibration constants.

particles: list[Particle] = []


def setup():
    global wall, engine
    size(640, 240)

    engine = Space()  # Create the engine; Pymunk's "world/engine" is a Space.
    # Disable the gravity.
    engine.gravity = (0, 0)  # Optional -- Pymunk gravity is (0, 0) by default.

    wall = Boundary(engine, width / 2, height - 5, width, 10)


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
