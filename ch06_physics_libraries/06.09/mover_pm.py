# PY5 IMPORTED MODE CODE

from pymunk import *

import sys, os; sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from pymunk_constants import *  # Matter.js <-> Pymunk calibration constants.


class Mover:

    # Needs "space" parameter because Python modules have isolated namespaces.
    # (p5.js sketches share a single global scope)
    def __init__(self, space: Space, x: float, y: float, radius: float):
        self.radius = radius

        # 1.0 = no damping (global); conceptual equivalent to "frictionAir".
        space.damping = 1.0  # Optional -- Pymunk damping is 1.0 by default.

        options = {  # Specify the properties of this body in a dictionary.
          'restitution': 0.2,
          'friction': 0.01 * SCALE_FRICTION,
          'mass': PI * self.radius ** 2 * 0.001,  # Density = 0.001.
        }
        self.body = Body(
          options['mass'],
          moment_for_circle(options['mass'], 0, self.radius)
        )
        self.body.position = (x, y)
        self.shape = Circle(self.body, self.radius)
        self.shape.friction = options['friction']
        self.shape.elasticity = options['restitution']

        angle = random(TAU)
        vel = Vec2d(2 * cos(angle), 2 * sin(angle))
        self.body.velocity = vel * SCALE_VELOCITY

        space.add(self.body, self.shape)

    def apply_force(self, force: Vec2d) -> None:
        """Calling Body's apply_force_at_world_point() function."""
        self.body.apply_force_at_world_point(force, self.body.position)

    def show(self) -> None:
        fill(127)
        stroke(0)
        stroke_weight(2)
        push()
        translate(*self.body.position)
        rotate(self.body.angle)
        circle(0, 0, self.radius * 2)
        line(0, 0, self.radius, 0)
        pop()
