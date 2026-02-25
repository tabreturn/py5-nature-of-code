# PY5 IMPORTED MODE CODE


class Box:

    def __init__(self, x: float, y: float):
        # A box has an (x, y) position and a width.
        self.x = x
        self.y = y
        self.w = 16

    def show(self) -> None:
        # The box is drawn as a square().
        rect_mode(CENTER)
        fill(127)
        stroke(0)
        stroke_weight(2)
        square(self.x, self.y, self.w)
