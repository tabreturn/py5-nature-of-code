# NOTE: In py5, modules don't automatically know about the sketch.
# Use get_current_sketch() to retrieve the active Sketch instance.
from py5 import get_current_sketch

from py5 import circle, fill, Py5Vector2D, stroke, stroke_weight, random


class Mover:

    def __init__(self):
        # Get the current sketch to access values like width and height.
        self.cs = get_current_sketch()
        # The object has two vectors: position and velocity.
        self.position = Py5Vector2D(random(self.cs.width), random(self.cs.height))
        self.velocity = Py5Vector2D(random(-2, 2), random(-2, 2))

    def update(self) -> None:
        # Motion 101: position changes by velocity.
        self.position += self.velocity  # The mover moves.

    def show(self) -> None:
        stroke(0)
        stroke_weight(2)
        fill(127)
        # The mover is drawn as a circle.
        circle(self.position.x, self.position.y, 48)

    def check_edges(self) -> None:
        """When it reaches one edge, set the position to the other edge."""

        if self.position.x > self.cs.width:
            self.position.x = 0
        elif self.position.x < 0:
            self.position.x = self.cs.width

        if self.position.y > self.cs.height:
            self.position.y = 0
        elif self.position.y < 0:
            self.position.y = self.cs.height
