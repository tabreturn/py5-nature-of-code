# PY5 IMPORTED MODE CODE

# Note Matter.js uses 'aliases'; for py5 just import Pymunk symbols directly.
from pymunk import Body, Poly, moment_for_box, Circle, moment_for_circle, Vec2d

import sys, os; sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from pymunk_constants import *  # Matter.js <-> Pymunk calibration constants.


class Lollipop:

    def __init__(self, space, x: float, y: float):
        self.w = 24
        self.h = 4
        self.r = 8

        options = {  # Specify the properties of this body in a dictionary.
          'friction': 0.01 * SCALE_FRICTION,
          'restitution': 1.0,
          'mass': 1.0,
        }

        # Add an offset from the x-position of the lollipop's stick.
        self.offset = Vec2d(self.w / 2, 0)

        # Join the two bodies together first (in Pymunk, make bodies is second).
        self.body = Body(
          options['mass'],
          moment_for_box(options['mass'], (self.w, self.h))
          + moment_for_circle(options['mass'], 0, self.r, self.offset),
        )

        # Make the bodies.
        self.part_1 = Poly.create_box(self.body, (self.w, self.h))
        self.part_1.friction = options['friction']
        self.part_1.elasticity = options['restitution']
        self.part_2 = Circle(self.body, self.r, self.offset)
        self.part_2.friction = options['friction']
        self.part_2.elasticity = options['restitution']

        self.body.position = (x, y)
        self.body.velocity = Vec2d(random(-5, 5) * SCALE_VELOCITY, 0)
        self.body.angular_velocity = 0.1 * SCALE_ANG_VELOCITY

        self.space = space  # Store reference for remove_body/etc.

        # Add the compound body to the world.
        self.space.add(self.body, self.part_1, self.part_2)


    def show(self) -> None:
        # The angle comes from the compound body.
        angle = self.body.angle

        # Get the position for each part.
        position_1 = self.body.position  # body center in world space ...
        position_2 = self.body.local_to_world(self.offset)  # offset is local.

        fill(175)
        stroke(0)
        stroke_weight(2)

        # Translate and rotate the rectangle (part1).
        push()
        translate(*position_1)
        rotate(angle)
        rect_mode(CENTER)
        rect(0, 0, self.w, self.h)
        pop()

        # Translate and rotate the circle (part2).
        push()
        translate(*position_2)
        rotate(angle)
        fill(175)
        circle(0, 0, self.r * 2)
        pop()

    def remove_body(self) -> None:
        """This function removes a body from the Matter.js world."""

        self.space.remove(self.part_1, self.part_2, self.body)

    def check_edge(self) -> bool:
        return self.body.position.y > height + self.h * 2
