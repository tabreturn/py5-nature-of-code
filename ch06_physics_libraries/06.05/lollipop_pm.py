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
          'restitution': 0.2,
          'mass': 1.0,
        }

        # Offsets (body-local) like the JS version:
        self.part_1_offset = Vec2d(0, 0)
        self.part_2_offset = Vec2d(self.w / 2, 0)

        m = options['mass']

        # Circle offset inline (like x + w/2 in Matter)
        circle_offset = Vec2d(self.w / 2, 0)

        # Compound moment
        self.body = Body(
          m,
          moment_for_box(m * 0.6, (self.w, self.h))
          + moment_for_circle(m * 0.4, 0, self.r, offset=circle_offset),
        )
        self.body.position = (x, y)

        # Rectangle part (centered on body)
        self.part1 = Poly.create_box(self.body, (self.w, self.h))

        # Circle part (offset from body)
        self.part2 = Circle(self.body, self.r, offset=circle_offset)

        for s in (self.part1, self.part2):
            s.friction = options['friction']
            s.elasticity = options['restitution']

        # Initial motion (Matter-like)
        self.body.velocity = Vec2d(random(-5, 5) * SCALE_VELOCITY, 0)
        self.body.angular_velocity = 0.1 * SCALE_ANG_VELOCITY


        self.space = space  # Store reference for removing/etc.
        self.space.add(self.body, self.part1, self.part2)  # Don't forget to add it to world!


    def show(self) -> None:
        # Need the body's position and angle.
        position1 = self.body.local_to_world(self.part_1_offset)
        position2 = self.body.local_to_world(self.part_2_offset)
        angle = self.body.angle

        fill(127)
        stroke(0)
        stroke_weight(2)

        # Translate and rotate the rectangle (part1)
        push_matrix()
        translate(position1.x, position1.y)
        rotate(angle)
        rect_mode(CENTER)
        rect(0, 0, self.w, self.h)
        pop_matrix()

        # Translate and rotate the circle (part2)
        push_matrix()
        translate(position2.x, position2.y)
        rotate(angle)
        fill(200)
        circle(0, 0, self.r * 2)
        pop_matrix()

    def remove_body(self) -> None:
        """This function removes a body from the Matter.js world."""

        self.space.remove(self.part1, self.part2, self.body)

    def check_edge(self) -> bool:
        return self.body.position.y > height + self.h * 2
