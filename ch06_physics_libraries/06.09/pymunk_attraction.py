# https://natureofcode.com/physics-libraries/#revolute-constraints

# Note Matter.js uses 'aliases'; for py5 just import Pymunk symbols directly.
from pymunk import Space
from attractor_pm import Attractor
from mover_pm import Mover

import sys, os; sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from pymunk_constants import *  # Matter.js <-> Pymunk calibration constants.


def setup():
    global attractor, movers, engine
    size(640, 240)

    engine = Space()  # Create the engine; Pymunk's "world/engine" is a Space.
    # Disable the gravity. 
    engine.gravity = (0, 0)  # Optional -- Pymunk gravity is (0, 0) by default.

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
