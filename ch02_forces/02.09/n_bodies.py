# https://natureofcode.com/forces/#example-29-n-bodies

from body import Body

G = 1.0  # A gravitational constant (for global scaling)


def setup():
    global bodies
    size(640, 240)

    # Fill the array with Body objects.
    bodies = [
      Body(random(width), random(height), random(0.1, 2))
      for _ in range(10)
    ]


def draw():
    background(255)

    # For every body, check every body!
    for i, body_i in enumerate(bodies):
        for j, body_j in enumerate(bodies):
            if i != j:  # Do not attract yourself!
                force = body_j.attract(body_i, G)
                body_i.apply_force(force)
        # Update and show all bodies.
        body_i.update()
        body_i.show()
