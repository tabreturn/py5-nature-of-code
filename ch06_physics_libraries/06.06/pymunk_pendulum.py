# https://natureofcode.com/physics-libraries/#distance-constraints

# Note Matter.js uses 'aliases'; for py5 just import Pymunk symbols directly.
from pymunk import Space
from pendulum_pm import Pendulum

import sys, os; sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from pymunk_constants import *  # Matter.js <-> Pymunk calibration constants.


def setup():
    global pendulum, engine  # The engine is now a global variable!
    size(640, 240)

    engine = Space()  # Create the engine; Pymunk's "world/engine" is a Space.
    # Change the engine's gravity to point downward.
    engine.gravity = (0, 1.0 * SCALE_GRAVITY)

    pendulum = Pendulum(engine, width / 2, 10, 100)


def draw():
    background(255)

    engine.step(DT)  # Step the engine forward in time!

    pendulum.show()
