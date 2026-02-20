# https://natureofcode.com/fractals/#example-82-recursive-circles-twice


def setup():
    size(640, 240)


def draw():
    background(255)
    draw_circles(width / 2, height / 2, 320)
    no_loop()


def draw_circles(x: float, y: float, radius: float) -> None:
    stroke(0)
    stroke_weight(2)
    circle(x, y, radius * 2)

    if radius > 4:  # Exit condition: stop when the radius is too small.
        # draw_circles() calls itself twice. For every circle, draw a --
        draw_circles(x - radius / 2, y, radius / 2)  # smaller to the left ...
        draw_circles(x + radius / 2, y, radius / 2)  # and the right.
