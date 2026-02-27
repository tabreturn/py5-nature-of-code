# PY5 IMPORTED MODE CODE

from pymunk import *

import sys, os; sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from pymunk_constants import *  # Matter.js <-> Pymunk calibration constants.


class Particle:

    # Needs "space" parameter because Python modules have isolated namespaces.
    # (p5.js sketches share a single global scope)
    def __init__(self, space: Space, x: float, y: float):
#        self.r = 8
        self.r = random(4, 8)
        self.col = color(127)

        options = {  # Specify the properties of this body in a dictionary.
          'friction': 0.01 * SCALE_FRICTION,
          'restitution': 0.6,
          'mass': 1.0,
        }
        self.body = Body(
          options['mass'], moment_for_circle(options['mass'], 0, self.r)
        )
        self.body.position = (x, y)
        self.shape = Circle(self.body, self.r)
        self.shape.friction = options['friction']
        self.shape.elasticity = options['restitution']

        # "self" refers to this Particle (a reference to access it later).
        self.shape.particle = self

        self.space = space  # Store reference for remove_body/etc.
        self.space.add(self.body, self.shape)

    def show(self) -> None:
        pos = self.body.position
        a = self.body.angle

        rect_mode(CENTER)
#        fill(127)
        fill(self.col)
        stroke(0)
        stroke_weight(2)
        push()
        translate(*pos)
        rotate(a)
        circle(0, 0, self.r * 2)
        line(0, 0, self.r, 0)
        pop()

    def remove_body(self) -> None:
        """This function removes a body from the Matter.js world."""

        self.space.remove(self.shape, self.body)

    def check_edge(self) -> bool:
        return self.body.position.y > height + self.r

    def change(self) -> None:
        """Change color when hit."""

        self.col = color(random(100, 255), 0, random(100, 255))
