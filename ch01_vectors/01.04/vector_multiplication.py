# https://natureofcode.com/vectors/#vector-multiplication-and-division


def setup():
    size(640, 240)


def draw():
    background(255)

    # Two vectors, one for mouse location and one for the center of the window.
    mouse = Py5Vector2D(mouse_x, mouse_y)
    center = Py5Vector2D(width / 2, height / 2)
    mouse -= center

    translate(width / 2, height / 2)
    stroke_weight(2)
    stroke(175)
    line(0, 0, mouse.x, mouse.y)

    # Multiplying a vector! Now half its original size (multiplied by 0.5).
    mouse *= 0.5

    stroke(0)
    stroke_weight(4)
    line(0, 0, mouse.x, mouse.y)
