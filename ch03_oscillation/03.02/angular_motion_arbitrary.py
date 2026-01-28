# https://natureofcode.com/forces/#example-29-n-bodies

"""
NOTE: This is an extension of 02.07 (attraction_many_movers)
"""

from mover import Mover
from attractor import Attractor

G = 1.0  # A gravitational constant (for global scaling)


def setup():
    global movers, attractor
    size(640, 240)

    # Now you have 20 movers!
    movers = [
      # Each mover is initialized randomly.
      Mover(random(width), random(height), random(0.5, 3))
      for _ in range(20)
    ]

    # JS version Mover class hardcodes this.velocity
    for m in movers:
        m.velocity = Py5Vector2D(random(-1, 1), random(-1, 1))

    attractor = Attractor()  # Initialize the Attractor object.


def draw():
    background(255)

    attractor.show()  # Draw the Attractor object.

    # Apply the attraction force from the attractor on the mover(s).
    for mover in movers:
        # Calculate an attraction force for each Mover object.
        force = attractor.attract(mover, G)
        mover.apply_force(force)
        mover.update()
        mover.show()


# The functions below are for mouse interaction

def mouse_moved():
    attractor.handle_hover(mouse_x, mouse_y)

def mouse_pressed():
    attractor.handle_press(mouse_x, mouse_y)

def mouse_dragged():
    attractor.handle_hover(mouse_x, mouse_y)
    attractor.handle_drag(mouse_x, mouse_y)

def mouse_released():
    attractor.stop_dragging()