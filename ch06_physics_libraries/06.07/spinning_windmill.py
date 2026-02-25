# https://natureofcode.com/physics-libraries/#revolute-constraints

# Note Matter.js uses 'aliases'; for py5 just import Pymunk symbols directly.
from pymunk import Space
from particle_pm import Particle
from windmill_pm import Windmill

import sys, os; sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from pymunk_constants import *  # Matter.js <-> Pymunk calibration constants.

particles: list[Particle] = []  # A list to store all Particle objects.


def setup():
    global windmill, engine  # The engine is now a global variable!
    size(640, 240)

    engine = Space()  # Create the engine; Pymunk's "world/engine" is a Space.
    # Change the engine's gravity to point downward.
    engine.gravity = (0, 1.0 * SCALE_GRAVITY)

    windmill = Windmill(engine, width / 2, height - 50, 120, 10)


def draw():
    background(255)

    engine.step(DT)  # Step the engine forward in time!

    if random() < 0.05:
        particles.append(Particle(engine, width / 2 + random(-60, 60), 0))

    windmill.show()

    # Iterate over a copy to remove particles safely (instead of backwards).
    for particle in particles[:]:
        # Display all the Particle objects.
        particle.show()
        # Remove the Body(+shape) from the world and the list.
        if particle.check_edge():
            particle.remove_body()
            particles.remove(particle)
