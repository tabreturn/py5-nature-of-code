# https://natureofcode.com/physics-libraries/#example-65-multiple-shapes-on-one-body

# Note Matter.js uses 'aliases'; for py5 just import Pymunk symbols directly.
from pymunk import Space
from boundary_pm import Boundary
from lollipop_pm import Lollipop

import sys, os; sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from pymunk_constants import *  # Matter.js <-> Pymunk calibration constants.

lollipops: list[Lollipop] = []  # A list to store all Lollipop objects.


def setup():
    global boundaries, engine  # The engine is now a global variable!
    size(640, 240)
    engine = Space()  # Create the engine; Pymunk's "world/engine" is a Space.
    # Change the engine's gravity to point downward.
    engine.gravity = (0, 1.0 * SCALE_GRAVITY)

    # Add a bunch of fixed boundaries.
    boundaries = [
        Boundary(engine, width / 4, height - 5, width / 2 - 50, 10),
        Boundary(engine, (3 * width) / 4, height - 50, width / 2 - 50, 10),
    ]


def draw():
    background(255)

    engine.step(DT)  # Step the engine forward in time!

    # Lollipops fall from the top every so often.
    if random() < 0.025:
        lollipop = Lollipop(engine, width / 2, 50)
        lollipops.append(lollipop)

    # Display all the boundaries.
    for boundary in boundaries:
        boundary.show()

    # Iterate over a copy to remove lollipops safely (instead of backwards).
    for lollipop in lollipops[:]:
        # Display all the Lollipop objects.
        lollipop.show()
        # Remove the Body(+shape) from the world and the list.
        if lollipop.check_edge():
            lollipop.remove_body()
            lollipops.remove(lollipop)
