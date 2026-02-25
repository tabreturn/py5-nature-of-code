# PY5 IMPORTED MODE CODE

from pymunk import *

import sys, os; sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from pymunk_constants import *  # Matter.js <-> Pymunk calibration constants.


class Pendulum:

    # Needs "space" parameter because Python modules have isolated namespaces.
    # (p5.js sketches share a single global scope)
    def __init__(self, space, x: float, y: float, len_: float):
        self.r = 12
        self.len_ = len_
        self.x = x
        self.y = y

        # Create two bodies: one for anchor, one for bob. The anchor is static.
        self.anchor_body = Body(body_type=Body.STATIC)
        self.anchor_body.position = (self.x, self.y)
        self.anchor_shape = Circle(self.anchor_body, self.r)

        self.bob_body = Body(1.0, moment_for_circle(1.0, 0.0, self.r))
        self.bob_body.position = (self.x + self.len_, self.y - self.len_)
        self.bob_shape = Circle(self.bob_body, self.r)
        self.bob_shape.elasticity = 0.6  # Pymunk restitution.

        # Create a constraint connecting the anchor and the bob.
        options = {
          'body_a': self.anchor_body,
          'body_b': self.bob_body,
          'length': self.len_,
        }
        self.arm = pymunk.PinJoint(
          options['body_a'], options['body_b'], (0, 0), (0, 0)
        )
        self.arm.distance = options['length']
        
        self.space = space  # Store reference for remove_body/etc.
        space.damping = 0.5  # Global air drag to match Matter.js energy loss.

        # Add all bodies and constraints to the world.
        self.space.add(self.anchor_body, self.anchor_shape)
        self.space.add(self.bob_body, self.bob_shape)
        self.space.add(self.arm)

    def show(self) -> None:
        fill(127)
        stroke(0)
        stroke_weight(2)

        # Draw a line representing the pendulum arm.
        line(*self.anchor_body.position, *self.bob_body.position)

        # Draw the anchor.
        push()
        translate(*self.anchor_body.position)
        rotate(self.anchor_body.angle)
        circle(0, 0, self.r * 2)
        line(0, 0, self.r, 0)
        pop()

        # Draw the bob.
        push()
        translate(*self.bob_body.position)
        rotate(self.bob_body.angle)
        circle(0, 0, self.r * 2)
        line(0, 0, self.r, 0)
        pop()
