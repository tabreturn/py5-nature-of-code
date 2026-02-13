# PY5 IMPORTED MODE CODE


class Glow:

    def __init__(self):
        # Two Perlin noise offsets.
        self.xoff = 0
        self.yoff = 1_000

        self.position = Py5Vector2D()
        self.r = 24

    def update(self) -> None:
        # Assign the position according to the Perlin noise.
        self.position.x = noise(self.xoff) * width
        self.position.y = noise(self.yoff) * height
        # Move along the Perlin noise space.
        self.xoff += 0.01
        self.yoff += 0.01

    def show(self) -> None:
        stroke(0)
        stroke_weight(2)
        fill(175)
        circle(self.position.x, self.position.y, self.r * 2)
