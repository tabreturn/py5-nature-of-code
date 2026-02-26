# PY5 IMPORTED MODE CODE

from pymunk import *

import sys, os; sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from pymunk_constants import *  # Matter.js <-> Pymunk calibration constants.


class Attractor:

    # Needs "space" parameter because Python modules have isolated namespaces.
    # (p5.js sketches share a single global scope)
    def __init__(self, space: Space, x: float, y: float):
        # The attractor is a static body.
        self.radius = 32
        self.body = Body(body_type=Body.STATIC)
        self.body.position = (x, y)
        self.shape = Circle(self.body, self.radius)
        self.shape.friction = 2.0
        self.shape.elasticity = 0.2

        space.add(self.body, self.shape)

    def attract(self, mover: 'Mover') -> Vec2d:
        # The attract() method now uses vector functions.
        force = self.body.position - mover.body.position
        distance = force.length
        distance = constrain(distance, 5, 25)

        # Use a small value for G to keep the system stable.
        G = 0.02 * 1000_000  # Use a small value for G to keep the system stable.

        # The mover's mass is included here, but the attractor's mass is left out since,
        # as a static body, it is equivalent to infinity.
        strength = (G * mover.body.mass) / (distance ** 2)

        # More Matter.js vector functions.
        force = force.normalized()
        force *= strength

        return force

    def show(self) -> None:
        fill(0)
        stroke(0)
        stroke_weight(2)
        push()
        translate(*self.body.position)
        rotate(self.body.angle)
        circle(0, 0, self.radius * 2)
        line(0, 0, self.radius, 0)
        pop()
