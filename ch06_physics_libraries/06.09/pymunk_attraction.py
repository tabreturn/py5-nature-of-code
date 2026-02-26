# https://natureofcode.com/physics-libraries/#revolute-constraints

# Note Matter.js uses 'aliases'; for py5 just import Pymunk symbols directly.
from pymunk import Space
from attractor_pm import Attractor
from mover_pm import Mover

import sys, os; sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from pymunk_constants import *  # Matter.js <-> Pymunk calibration constants.

##particles: list[Particle] = []  # A list to store all Particle objects.


def setup():
    global attractor, movers, engine
    size(640, 240)

    engine = Space()  # Create the engine; Pymunk's "world/engine" is a Space.
    # Disable the gravity. Optional -- Pymunk gravity already (0, 0) by default.
    engine.gravity = (0, 0)  

    movers = [
      Mover(engine, random(width), random(height), random(4, 8))
      for _ in range(100)
    ]

    attractor = Attractor(engine, width / 2, height / 2)


def draw():
    background(255)

    engine.step(DT)  # Step the engine forward in time!

    for mover in movers:
        force = attractor.attract(mover)
        mover.apply_force(force)
        mover.show()

    attractor.show()
