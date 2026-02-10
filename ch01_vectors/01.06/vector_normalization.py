# https://natureofcode.com/vectors/#normalizing-vectors


def setup():
    size(640, 240)


def draw():
    background(255)

    # Two vectors, one for mouse location and one for the center of the window.
    mouse = Py5Vector2D(mouse_x, mouse_y)
    center = Py5Vector2D(width / 2, height / 2)
    mouse -= center

    translate(width / 2, height / 2)
    stroke(175)
    stroke_weight(2)
    line(0, 0, mouse.x, mouse.y)

    # In this example, after the vector is normalized, it's multiplied by 50.
    # Note that no matter where the mouse is, the vector has the same length (50)
    # because of the normalization process.
    mouse.normalize()
    mouse *= 50

    stroke(0)
    stroke_weight(8)
    line(0, 0, mouse.x, mouse.y)
