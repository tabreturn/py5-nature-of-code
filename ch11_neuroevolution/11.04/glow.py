from py5 import circle, fill, get_current_sketch, Py5Vector2D, stroke, stroke_weight


class Glow:

    def __init__(self):
        self.tx = 0
        self.ty = 10_000

        self.position = Py5Vector2D()
        self.r = 24;

    def step(self) -> None:
        # x- and y-position mapped from noise.
        self.x = remap(noise(self.tx), 0, 1, 0, get_current_sketch().width)
        self.y = remap(noise(self.ty), 0, 1, 0, get_current_sketch().height)
        # Move forward through time.
        self.tx += 0.01
        self.ty += 0.01

    def show(self) -> None:
        stroke_weight(2)
        fill(127)
        stroke(0)
        circle(self.x, self.y, self.r * 2)
