# https://natureofcode.com/forces/#example-26-attraction

from mover import Mover
from attractor import Attractor

G = 1.0  # A gravitational constant (for global scaling)


def setup():
    global mover, attractor  # A mover and an attractor
    size(640, 240)

    mover = Mover(300, 50, 2)
    mover.velocity = Py5Vector(1, 0)

    attractor = Attractor()  # Initialize the Attractor object.


def draw():
    background(255)

    # Apply the attraction force from the attractor on the mover(s).
    force = attractor.attract(mover, G)
    mover.apply_force(force)

    mover.update()
    attractor.show()  # Draw the Attractor object.
    mover.show()


# The function(s) below are for mouse/key interaction

def mouse_moved():
    attractor.handle_hover(mouse_x, mouse_y)

def mouse_pressed():
    attractor.handle_press(mouse_x, mouse_y)

def mouse_dragged():
    attractor.handle_hover(mouse_x, mouse_y)
    attractor.handle_drag(mouse_x, mouse_y)

def mouse_released():
    attractor.stop_dragging()
