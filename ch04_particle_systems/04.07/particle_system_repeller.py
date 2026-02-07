# https://natureofcode.com/particles/#particle-systems-with-repellers

from emitter import Emitter
from repeller import Repeller


def setup():
    global emitter, repeller
    size(640, 240)
    emitter = Emitter(width / 2, 60)
    repeller = Repeller(width / 2, 250)  # One repeller.


def draw():
    background(255)

    # Create a hardcoded vector and apply it as a force.
    GRAVITY = Py5Vector2D(0, 0.1)
    # Apply a force to the emitter.
    emitter.apply_force(GRAVITY)

    emitter.apply_repeller(repeller)  # Apply the repeller.
    repeller.show()

    emitter.add_particle()
    emitter.run()


# The function(s) below are for mouse interaction

def mouse_moved():
    global repeller
    repeller.position = Py5Vector2D(mouse_x, mouse_y)
