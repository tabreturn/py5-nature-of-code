# https://natureofcode.com/forces/#example-23-gravity-scaled-by-mass

from mover import Mover


def setup():
    global mover_a, mover_b
    size(640, 240)
    # A large mover on left side of the canvas.
    mover_a = Mover(200, 30 - (10 * 8), 10)
    # A smaller mover on right side of the canvas.
    mover_b = Mover(440, 30 - (2 * 8), 2)


def draw():
    background(255)

    # Make up a gravity force and apply it.
    gravity = Py5Vector2D(0, 0.1)

    gravity_a = gravity * mover_a.mass  # Scale by mover A's mass.
    mover_a.apply_force(gravity_a)

    gravity_b = gravity * mover_b.mass  # Scale by mover B's mass.
    mover_b.apply_force(gravity_b)

    # Make up a wind force and apply it when the mouse is clicked.
    if is_mouse_pressed:
        wind = Py5Vector2D(0.1, 0)
        mover_a.apply_force(wind)
        mover_b.apply_force(wind)

    # Call methods on the Mover object(s).
    mover_a.update()
    mover_a.check_edges()
    mover_a.show()
    mover_b.update()
    mover_b.check_edges()
    mover_b.show()
