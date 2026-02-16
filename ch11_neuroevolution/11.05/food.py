# PY5 IMPORTED MODE CODE


class Food:

    def __init__(self):
        """A piece of food has a random position and a fixed radius."""
        self.position = Py5Vector2D(random(width), random(height))
        self.r = 50

    def show(self) -> None:
        no_stroke()
        fill(0, 100)
        circle(self.position.x, self.position.y, self.r * 2)
