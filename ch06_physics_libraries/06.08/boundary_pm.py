# PY5 IMPORTED MODE CODE

from pymunk import *


class Boundary:

    # Needs "space" parameter because Python modules have isolated namespaces.
    # (p5.js sketches share a single global scope)
    def __init__(self, space: Space, x: float, y: float, w: float, h: float):
        # A boundary is a simple rectangle with x, y, width, and height.
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        # Lock the body in place by setting body_type to Body.STATIC!
        self.body = Body(body_type=Body.STATIC)
        self.body.position = (self.x, self.y)
        self.shape = Poly.create_box(self.body, (self.w, self.h))
        self.shape.friction = 2.0
        self.shape.elasticity = 0.2

        space.add(self.body, self.shape)

    def show(self) -> None:
        # Since boundary can never move, show() can draw it old-fashioned way,
        # using the original variables. No need to query Pymunk.
        rect_mode(CENTER)
        fill(127)
#        stroke(0)
#        stroke_weight(2)
        no_stroke()
        rect(self.x, self.y, self.w, self.h)
