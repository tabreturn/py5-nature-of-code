from py5 import CORNER, Py5Vector2D, fill, rect, rect_mode, stroke, stroke_weight


class Obstacle:

    def __init__(self, x: float, y: float, w: float, h: float):
        self.position = Py5Vector2D(x, y)
        self.w = w
        self.h = h

    def contains(self, spot: Py5Vector2D) -> bool:
        return (
          spot.x > self.position.x and
          spot.x < self.position.x + self.w and
          spot.y > self.position.y and
          spot.y < self.position.y + self.h
        )

    def show(self) -> None:
        stroke(0)
        fill(175)
        stroke_weight(2)
        rect_mode(CORNER)
        rect(self.position.x, self.position.y, self.w, self.h)
