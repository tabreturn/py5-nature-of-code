# https://natureofcode.com/vectors/#algorithm-3-interactive-motion


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
