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
        self.body.position = Vec2d(x, y)
        self.shape = Circle(self.body, self.radius)
        self.shape.friction = 2.0
        self.shape.elasticity = 0.2
        space.add(self.body, self.shape)

    def attract(self, mover: 'Mover') -> Vec2d:
        # The attract() method now uses Pymunk vectors.
        force = self.body.position - mover.body.position
        distance = force.length
        distance = constrain(distance, 5, 25)

        # Use a small value for G to keep the system stable, but ...
        G = 0.02 * 1_000_000  # ... scale massively for Pymunk's unit system.

        # Attractor's mass is absorbed into G since it is a fixed (static) body.
        strength = (G * mover.body.mass) / (distance ** 2)

        # More vector methods/calculations.
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
        pop()
