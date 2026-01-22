# https://natureofcode.com/vectors/#example-17-motion-101-velocity

from mover import Mover


def setup():
    global mover
    size(640, 240)
    mover = Mover()  # Create the Mover object.


def draw():
    background(255)

    # Call methods on the Mover object.
    mover.update()
    mover.check_edges()
    mover.show()
