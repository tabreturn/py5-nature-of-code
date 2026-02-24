# PY5 IMPORTED MODE CODE

# Note Matter.js uses 'aliases'; for py5 just import Pymunk symbols directly.
from pymunk import Body, Poly, moment_for_box, Vec2d

import sys, os; sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from pymunk_constants import *  # Matter.js <-> Pymunk calibration constants.


class Box:

    # Needs "space" parameter because Python modules have isolated namespaces.
    # (p5.js sketches share a single global scope)
    def __init__(self, space: 'Space', x: float, y: float):
#        # A box has an (x, y) position and a width.
#        self.x = x
#        self.y = y
        self.w = random(8, 16)
        self.h = random(8, 16)

        """
        NOTE:
        Pymunk separates Body (physics) from Shape (collision geometry).
        Multiple Shapes can attach to one Body.
        Think: Body = physics; Shape = collision skin.
        """

        options = {  # Specify the properties of this body in a dictionary.
          'friction': 0.01 * SCALE_FRICTION,
          'restitution': 0.75,
          'mass': 1.0,
        }
        # Instead of any of the usual variables, store a reference to a body.
        self.body = Body(
          options['mass'], moment_for_box(options['mass'], (self.w, self.h))
        )
        self.body.position = (x, y)
        self.shape = Poly.create_box(self.body, (self.w, self.h))
        self.shape.friction = options['friction']
        self.shape.elasticity = options['restitution']
        self.body.velocity = Vec2d(random(-5, 5) * SCALE_VELOCITY, 0.0)
        self.body.angular_velocity = 0.1 * SCALE_ANG_VELOCITY

        self.space = space  # Store reference for remove_body/etc.
        self.space.add(self.body, self.shape)  # Don't forget to add it to world!

    def show(self) -> None:
        # Need the body's position and angle.
        position = self.body.position
        angle = self.body.angle

        # The box is drawn as a square().
        rect_mode(CENTER)
        fill(127)
        stroke(0)
        stroke_weight(2)

        push()
        # Use the position and angle to translate and rotate the square.
        translate(position.x, position.y)
        rotate(angle)
        rect(0, 0, self.w, self.h)
        pop()

    def remove_body(self) -> None:
        """This function removes a body from the Matter.js world."""

        self.space.remove(self.shape, self.body)

    def check_edge(self) -> bool:
        return self.body.position.y > height + self.w
