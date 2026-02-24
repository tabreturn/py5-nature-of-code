# PY5 IMPORTED MODE CODE

# Note Matter.js uses 'aliases'; for py5 just import Pymunk symbols directly.
from pymunk import Body, Poly, moment_for_poly, Vec2d

import sys, os; sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from pymunk_constants import *  # Matter.js <-> Pymunk calibration constants.


class CustomShape:

    def __init__(self, space: 'Space', x: float, y: float):
        # A list of five vectors.
        vertices_ = [
          Vec2d(-10, -10),
          Vec2d(20, -15),
          Vec2d(15, 0),
          Vec2d(0, 10),
          Vec2d(-20, 15),
        ]

        """
        NOTE:
        Pymunk separates Body (physics) from Shape (collision geometry).
        Multiple Shapes can attach to one Body.
        Think: Body = physics; Shape = collision skin.
        """

        # Make a body shaped by the vertices.
        options = {  # Specify the properties of this body in a dictionary.
          'friction': 0.01 * SCALE_FRICTION,
          'restitution': 0.2,
          'mass': 1.0,
        }
        self.body = Body(
          options['mass'], moment_for_poly(options['mass'], vertices_)
        )
        self.body.position = (x, y)
        self.shape = Poly(self.body, vertices_)
        self.shape.friction = options['friction']
        self.shape.elasticity = options['restitution']

        self.body.velocity = Vec2d(random(-5, 5) * SCALE_VELOCITY, 0.0)
        self.body.angular_velocity = 0.1 * SCALE_ANG_VELOCITY

        self.space = space  # Store reference for removing/etc.
        self.space.add(self.body, self.shape)  # Don't forget to add it to world!

    def show(self) -> None:
        fill(127)
        stroke(0)
        stroke_weight(2)

        begin_shape()  # Start the shape.
        # Loop through the body vertices.
        for v in self.shape.get_vertices():  # Pymunk local coordinates ...
            w = self.body.local_to_world(v)  # ... convert to world coordinates.
            vertex(w.x, w.y)
        end_shape(CLOSE)  # End the shape, closing it.

    def remove_body(self) -> None:
        """This function removes a body from the Matter.js world."""

        self.space.remove(self.shape, self.body)

    def check_edge(self) -> bool:
        return self.body.position.y > height + 100
