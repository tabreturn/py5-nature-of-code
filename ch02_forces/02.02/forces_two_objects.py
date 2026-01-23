# https://natureofcode.com/forces/#creating-forces

from mover import Mover


def setup():
    global mover_a, mover_b
    size(640, 240)
    mover_a = Mover(200, 30, 10)  # A large mover on left side of the canvas.
    mover_b = Mover(440, 30, 2)   # A smaller mover on right side of the canvas.


def draw():
    background(255)
    
    # Make up a gravity force and apply it.
    gravity = Py5Vector2D(0, 0.1)
    mover_a.apply_force(gravity)
    mover_b.apply_force(gravity)

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
