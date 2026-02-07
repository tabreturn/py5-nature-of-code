# https://natureofcode.com/oscillation/#spring-forces

from bob import Bob
from spring import Spring


def setup():
    global bob, spring
    size(640, 240)

    # Pick values for the positions and rest length.
    spring = Spring(width / 2, 10, 100)  # third arg is for "rest_length".
    bob = Bob(width / 2, 100)


def draw():
    background(255)

    # Apply a gravity force to the bob.
    gravity = Py5Vector2D(0, 2)
    bob.apply_force(gravity)

    # Update bob
    bob.update()
    bob.handle_drag(mouse_x, mouse_y)

    # connect() method takes care of computing the spring's force on the bob.
    spring.connect(bob)
    spring.constrain_length(bob, 30, 200)

    # Draw everything.
    spring.show_line(bob)
    spring.show()
    bob.show()


# The function(s) below are for mouse interaction

def mouse_pressed():
    bob.handle_press(mouse_x, mouse_y)

def mouse_released():
    bob.stop_dragging()
