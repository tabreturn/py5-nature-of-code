# PY5 IMPORTED MODE CODE

from pymunk import *

import sys, os; sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from pymunk_constants import *  # Matter.js <-> Pymunk calibration constants.


class Windmill:

    def __init__(self, space: Space, x: float, y: float, w: float, h: float):
        self.w = w
        self.h = h

        # The rotating body.
        self.body = Bodies.rectangle(x, y, w, h)
        Composite.add(engine.world, this.body)

        # The revolute constraint.
        options = {
          body_a: self.body,
          point_b: { x: x, y: y },
          length: 0,
          stiffness: 1,
        }
        self.constraint = Constraint.create(options)
        Composite.add(engine.world, this.constraint)

    def show(self) -> None:
        rect_mode(CENTER)
        fill(127)
        stroke(0)
        stroke_weight(2)
        push()
        translate(*self.body.position)
        push()
        rotate(self.body.angle)
        rect(0, 0, self.w, self.h)
        pop()
        line(0, 0, 0, height)  # Draw stand for windmill (not part of physics).
        pop()
