# https://natureofcode.com/forces/#creating-forces

from mover import Mover


def setup():
    global mover
    size(640, 240)
    mover = Mover()  # Create the Mover object.


def draw():
    background(255)

    gravity = Py5Vector2D(0, 0.1)
    mover.apply_force(gravity)

    if is_mouse_pressed:
        wind = Py5Vector2D(0.1, 0)
        mover.apply_force(wind)

    # Call methods on the Mover object.
    mover.update()
    mover.check_edges()
    mover.show()
