# https://natureofcode.com/physics-libraries/#example-64-polygon-shapes

# Note Matter.js uses 'aliases'; for py5 just import Pymunk symbols directly.
from pymunk import Space
from boundary_pm import Boundary
from custom_shape_pm import CustomShape

import sys, os; sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from pymunk_constants import *  # Matter.js <-> Pymunk calibration constants.

shapes: list[CustomShape] = []  # A list to store all CustomShape objects.


def setup():
    global boundaries, engine
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

    # Shapes fall from the top every so often.
    if random() < 0.025:
        cs = CustomShape(engine, width / 2, 50)
        shapes.append(cs)

    # Display all the boundaries.
    for boundary in boundaries:
        boundary.show()

    # Iterate over a copy to remove shapes safely (instead of backwards).
    for cs in shapes[:]:
        # Display all the CustomShape objects.
        cs.show()
        # Remove the Body(+shape) from the world and the list.
        if cs.check_edge():
            cs.remove_body()
            shapes.remove(cs)
