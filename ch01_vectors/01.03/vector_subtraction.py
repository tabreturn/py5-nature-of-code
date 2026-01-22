# https://natureofcode.com/vectors/#example-13-vector-subtraction


def setup():
    size(640, 240)


def draw():
    background(255)

    # Two vectors, one for mouse location and one for the center of the window.
    mouse = Py5Vector2D(mouse_x, mouse_y)
    center = Py5Vector2D(width / 2, height / 2)

    # Draw the original two vectors.
    stroke(200)
    stroke_weight(4)
    line(0, 0, mouse.x, mouse.y)
    line(0, 0, center.x, center.y)

    # Vector subtraction!
    mouse -= center

    # Draw a line to represent the result of subtraction.
    # Notice that I move the origin with translate() to place the vector.
    stroke(0)
    translate(width / 2, height / 2)
    line(0, 0, mouse.x, mouse.y)
