# https://natureofcode.com/oscillation/#pointing-in-the-direction-of-movement

from mover import Mover


def setup():
    global mover
    size(640, 240)
    mover = Mover(width / 2, height / 2, 1)


def draw():
    background(255)
    mover.update()
    mover.check_edges()
    mover.show()
