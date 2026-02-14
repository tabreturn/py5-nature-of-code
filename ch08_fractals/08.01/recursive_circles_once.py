# https://natureofcode.com/fractals/#example-81-recursive-circles-once


def setup():
    size(640, 240)


def draw():
    background(255)
    draw_circles(width / 2, height / 2, width / 2)
    no_loop()


def draw_circles(x: float, y: float, r: float) -> None:
    stroke(0)
    stroke_weight(2)
    circle(x, y, r * 2)

    if r > 4:  # Exit condition: stop when the radius is too small.
        r *= 0.75
        # Call the function inside the function (aka recursion!).
        draw_circles(x, y, r)  # Is this a paradox?
