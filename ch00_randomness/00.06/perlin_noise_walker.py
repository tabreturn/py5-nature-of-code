# https://natureofcode.com/random/#a-smoother-approach-with-perlin-noise


class Walker:

    def __init__(self):
        self.tx = 0
        self.ty = 10_000

    def step(self) -> None:
        # x- and y-position mapped from noise.
        self.x = remap(noise(self.tx), 0, 1, 0, width)
        self.y = remap(noise(self.ty), 0, 1, 0, height)
        # Move forward through time.
        self.tx += 0.01
        self.ty += 0.01

    def show(self) -> None:
        stroke_weight(2)
        fill(127)
        stroke(0)
        circle(self.x, self.y, 48)


def setup():
    global walker
    size(640, 240)
    walker = Walker()
    background(255)


def draw():
    walker.step()
    walker.show()
