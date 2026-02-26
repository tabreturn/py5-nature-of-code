# https://natureofcode.com/physics-libraries/#distance-constraints

# Note Matter.js uses 'aliases'; for py5 just import Pymunk symbols directly.
from pymunk import Body, Space, PivotJoint, ShapeFilter, Vec2d

from box_pm import Box
from boundary_pm import Boundary

import sys, os; sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from pymunk_constants import *  # Matter.js <-> Pymunk calibration constants.


def setup():
    global boundaries, box_1, box_2, space, mouse, engine
    size(640, 240)

    engine = Space()  # Create the engine; Pymunk's "world/engine" is a Space.
    # Change the engine's gravity to point downward.
    engine.gravity = (0, 1.0 * SCALE_GRAVITY)

    # Add a bunch of fixed boundaries.
    boundaries = [
      Boundary(engine, width / 2, height - 5, width, 10),
      Boundary(engine, width / 2, 5, width, 10),
      Boundary(engine, 5, height / 2, 10, height),
      Boundary(engine, width - 5, height / 2, 10, height),
    ]

    box_1 = Box(engine, 300, height / 2, 48, 48)
    box_2 = Box(engine, 400, height / 2, 48, 48)

    mouse = Body(body_type=Body.KINEMATIC)


def draw():
    background(255)

    engine.step(DT)  # Step the engine forward in time!

    # Display all the boundaries.
    for boundary in boundaries:
        boundary.show()

    box_1.show()
    box_2.show()

    mouse.position = (mouse_x, mouse_y)


# The function(s) below are for mouse/key interaction

mouse_joint = None

def mouse_pressed():
    global mouse_joint
    p = Vec2d(mouse_x, mouse_y)
    hit = engine.point_query_nearest(p, 5, ShapeFilter())
    if hit and hit.shape.body.body_type == Body.DYNAMIC:
        mouse.position = p
        b = hit.shape.body
        mouse_joint = PivotJoint(mouse, b, (0, 0), b.world_to_local(p))
        mouse_joint.max_force = 2_000_000
        engine.add(mouse_joint)

def mouse_released():
    global mouse_joint
    if mouse_joint:
        engine.remove(mouse_joint)
        mouse_joint = None
