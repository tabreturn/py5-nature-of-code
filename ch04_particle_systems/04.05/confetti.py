# PY5 IMPORTED MODE CODE

from particle import Particle


class Confetti(Particle):

    def __init__(self, x: float, y: float):
        super().__init__(x, y)

    # Other methods like update() are inherited from the parent.

    def show(self) -> None:  # Override the show() method.
        angle = remap(self.position.x, 0, width, 0, TWO_PI * 2)

        rect_mode(CENTER)
        fill(127, self.lifespan)
        stroke(0, self.lifespan)
        stroke_weight(2)
        # To rotate() a shape, transformations are necessary.
        push()
        translate(*self.position)
        rotate(angle)
        rect_mode(CENTER)
        square(0, 0, 12)
        pop()
