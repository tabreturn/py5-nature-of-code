# https://natureofcode.com/forces/#example-24-including-friction

from mover import Mover


def setup():
    global mover
    size(640, 240)
    mover = Mover(width / 2, 30, 5)


def draw():
    background(255)

    # Make up a gravity force and apply it.
    gravity = Py5Vector2D(0, 1)
    # Should scale by mass for accuracy, but this example has only one circle.
    mover.apply_force(gravity)

    # Make up a wind force and apply it when the mouse is clicked.
    if is_mouse_pressed:
        wind = Py5Vector2D(0.1, 0)
        mover.apply_force(wind)

    if mover.contact_edge:
        c = 0.1
        friction = mover.velocity * -1
        friction.set_mag(c)
        # Apply the friction force vector to the object.
        mover.apply_force(friction)

    # Call methods on the Mover object(s).
    mover.update()
    mover.check_edges()  # Call the revised check_edges() method.
    mover.show()
