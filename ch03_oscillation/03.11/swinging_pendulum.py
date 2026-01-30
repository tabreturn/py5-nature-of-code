# https://natureofcode.com/oscillation/#the-pendulum

from pendulum import Pendulum


def setup():
    global pendulum
    size(640, 240)
    # Make a new Pendulum object with an origin position and arm length.
    pendulum = Pendulum(width / 2, 0, 175)


def draw():
    background(255)
    pendulum.update()
    pendulum.show()

    pendulum.handle_drag(mouse_x, mouse_y)  # For mouse interaction.


# The methods below are for mouse interaction

def mouse_pressed():
    pendulum.handle_press(mouse_x, mouse_y)

def mouse_released():
    pendulum.stop_dragging()
