# https://natureofcode.com/fractals/#drawing-the-cantor-set-with-recursion


def setup():
    size(640, 240)
    background(255)

    stroke_weight(2)
    cantor(10, 10, 620)


def draw():
    no_loop()


def cantor(x: float, y: float, length: float) -> None:

    if length > 1:  # Keep going as long as the length is greater than 1 pixel.
        line(x, y, x + length, y)

        # Two recursive calls. Note that 20 pixels are added to y.
        cantor(x, y + 20, length / 3)  # From start to one-third.
        cantor(x + (2 * length / 3), y + 20, length / 3)  # Two-thirds to end.
