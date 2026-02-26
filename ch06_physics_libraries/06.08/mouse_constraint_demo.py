# https://natureofcode.com/physics-libraries/#distance-constraints

"""
NOTE:
Pymunk has no direct equivalent to the Matter.js MouseConstraint. Instead, this
adaptation simulates it using a kinematic 'mouse' body plus a PivotJoint, with
velocity clamping ('stiffness') and temporary rotation locking (0, float('inf')).
"""

# Note Matter.js uses 'aliases'; for py5 just import Pymunk symbols directly.
from pymunk import Body, Space, PivotJoint, ShapeFilter, Vec2d
# (Matter.js example imports Mouse, MouseConstraint, among others.)

from box_pm import Box
from boundary_pm import Boundary

import sys, os; sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from pymunk_constants import *  # Matter.js <-> Pymunk calibration constants.


def setup():
    global boundaries, box_1, box_2, mouse, engine
    size(640, 240)  # Pymunk needs no reference to the canvas.

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

    # Create a mouse attached to the engine.
    mouse = Body(body_type=Body.KINEMATIC)
    mouse.position = (mouse_x, mouse_y)
    engine.add(mouse)


def draw():
    background(255)

    engine.step(DT)  # Step the engine forward in time!

    for boundary in boundaries:
        boundary.show()

    box_1.show()
    box_2.show()

    options = {
      # Customize the constraint with additional properties.
      'constraint': {'stiffness': 2000}  # Box delay catching up to cursor.
    }
    if mouse_constraint:
        vel = (Vec2d(mouse_x, mouse_y) - mouse.position) / DT
        mouse.velocity = (
          vel.normalized() * options['constraint']['stiffness']
          if vel.length > options['constraint']['stiffness']
          else vel
        )


# The function(s) below are for mouse/key interaction

mouse_constraint = dragged_body = dragged_moment = None

def mouse_pressed():
    global mouse_constraint, dragged_body, dragged_moment
    p = Vec2d(mouse_x, mouse_y)
    if (h := engine.point_query_nearest(p, 5, ShapeFilter())
    ) and h.shape.body.body_type == Body.DYNAMIC:
        b = h.shape.body; mouse.position, mouse.velocity = p, (0, 0)
        dragged_body, dragged_moment = b, b.moment
        # Stop spin + lock rotation while dragging (try disable to test).
        b.angular_velocity, b.moment = 0, float('inf')
        # Attach mouse body to box via PivotJoint (MouseConstraint analogue).
        mouse_constraint = PivotJoint(mouse, b, (0, 0), b.world_to_local(p))
        engine.add(mouse_constraint)

def mouse_released():
    global mouse_constraint, dragged_body, dragged_moment
    if mouse_constraint:
        engine.remove(mouse_constraint); mouse_constraint = None
    if dragged_body:
        dragged_body.moment = dragged_moment; dragged_body = dragged_moment = None
