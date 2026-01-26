# https://natureofcode.com/forces/#example-28-two-body-attraction

from body import Body

G = 1.0  # A gravitational constant (for global scaling)


def setup():
    global body_a, body_b
    size(640, 240)

    # Create two Body objects, A and B.
    body_a = Body(320, 40, 8)
    body_b = Body(320, 200, 8)


def draw():
    background(255)

    # A attracts B, and B attracts A.
    body_a.attract(body_b, G)
    body_b.attract(body_a, G)

    body_a.update()
    body_a.show()
    body_b.update()
    body_b.show()
