# https://natureofcode.com/vectors/#vector-magnitude


def setup():
    size(640, 240)


def draw():
    background(255)

    # Two vectors, one for mouse location and one for the center of the window.
    mouse = Py5Vector2D(mouse_x, mouse_y)
    center = Py5Vector2D(width / 2, height / 2)
    mouse -= center

    # The magnitude ('length') of a vector is accessed via the mag attribute.
    # Here it's used as the width of a rectangle drawn at the top of the window.
    m = mouse.mag
    fill(0)
    rect(0, 0, m, 10)

    translate(width / 2, height / 2)
    line(0, 0, mouse.x, mouse.y)
