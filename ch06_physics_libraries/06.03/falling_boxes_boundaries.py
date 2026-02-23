# https://natureofcode.com/physics-libraries/#static-matterjs-bodies

# Note Matter.js uses 'aliases'; for py5 just import Pymunk symbols directly.
from pymunk import Space
from box_pm import Box
from boundary_pm import Boundary

import sys, os; sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from pymunk_constants import *  # Matter.js → Pymunk calibration constants.

boxes: list[Box] = []  # A list to store all Box objects.


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

    # Boxes fall from the top every so often.
    if random() < 0.1:
        b = Box(engine, width / 2, 50)
        boxes.append(b)

    # Display all the boundaries.
    for boundary in boundaries:
        boundary.show()

    # Iterate over a copy to remove boxes safely (instead of backwards).
    for box_ in boxes[:]:
        # Display all the Box objects.
        box_.show()
        # Remove the Body(+shape) from the world and the list.
        if box_.check_edge():
            box_.remove_body()
            boxes.remove(box_)
