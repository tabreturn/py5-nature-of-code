# PY5 IMPORTED MODE CODE

from pymunk import *
from pymunk.constraints import *

import sys, os; sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from pymunk_constants import *  # Matter.js <-> Pymunk calibration constants.


class Windmill:

    # Needs "space" parameter because Python modules have isolated namespaces.
    # (p5.js sketches share a single global scope)
    def __init__(self, space: Space, x: float, y: float, w: float, h: float):
        self.w = w
        self.h = h

        """
        NOTE:
        Matter.js uses Constraint.create({...}) for a revolute joint. In Pymunk,
        specific joint types are classes (e.g., PivotJoint).
        """

        options = {  # Specify the properties of this body in a dictionary.
          'restitution': 1.0,
          'mass': 10.0,
        }
        # Create a body at a given position with width and height.
        self.body = Body(options['mass'], moment_for_box(options['mass'], (w, h)))
        self.body.position = x, y
        self.shape = Poly.create_box(self.body, (w, h))  # The rotating body.
        self.shape.friction = 0.5
        self.shape.elasticity = options['restitution']
        space.add(self.body, self.shape)

        # Create PivotJoint (Pymunk has no "Constraint") and add to the world.
        self.pivot = PivotJoint(self.body, space.static_body, (x, y))
        space.add(self.pivot)

    def show(self) -> None:
        rect_mode(CENTER)
        fill(127)
        stroke(0)
        stroke_weight(2)
        push()
        translate(*self.body.position)
        rotate(self.body.angle)
        rect(0, 0, self.w, self.h)
        pop()
        # Draw stand for windmill (not part of physics).
        line(*self.pivot.anchor_b, self.pivot.anchor_b.x, height)
