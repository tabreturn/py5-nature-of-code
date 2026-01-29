# https://natureofcode.com/oscillation/#spring-forces

from spring import Spring
from bob import Bob

# Pick arbitrary values for the positions and rest length.
anchor = Py5Vector2D(0, 0)
bob = Py5Vector2D(0, 120)
rest_length = 100


force = bob - anchor
# A vector pointing from the anchor to bob gives current length of the spring.
current_length = force.mag
x = current_length - rest_length


def setup():
    global bob, spring
    size(640, 240)

    bob = Bob(width / 2, 100)
    spring = Spring(width / 2, 10, 100)


def draw():
    background(255)

    # Apply a gravity force to the bob.
    gravity = Py5Vector2D(0, 2)
    bob.apply_force(gravity)

    


    # physics / interaction
    bob.update()
    bob.handle_drag(mouse_x, mouse_y)
    # This Spring method takes care of computing the spring's force on the bob.
    spring.connect(bob)
    spring.constrain_length(bob, 30, 200)

    # draw (after positions are final for the frame)
    spring.show_line(bob)
    spring.show()
    bob.show()


# The methods below are for mouse interaction

def mouse_pressed():
    bob.handle_press(mouse_x, mouse_y)

def mouse_released():
    bob.stop_dragging()
