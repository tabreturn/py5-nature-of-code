# https://natureofcode.com/fractals/#example-83-recursive-circles-four-times


def setup():
    size(640, 240)


def draw():
    background(255)
    draw_circles(width / 2, height / 2, 320)
    no_loop()


def draw_circles(x: float, y: float, radius: float) -> None:
    stroke(0)
    no_fill()
#    stroke_weight(2)
    circle(x, y, radius * 2)

    if radius > 16:  # Exit condition: stop when the radius is too small.
        # draw_circles() calls itself four times.
        draw_circles(x - radius / 2, y, radius / 2)
        draw_circles(x + radius / 2, y, radius / 2)
        draw_circles(x, y + radius / 2, radius / 2)
        draw_circles(x, y - radius / 2, radius / 2)
