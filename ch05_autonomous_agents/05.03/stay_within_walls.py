# https://natureofcode.com/autonomous-agents/#example-53-stay-within-walls-steering-behavior

from vehicle import Vehicle

OFFSET = 25
debug = True


def setup():
    global vehicle
    size(640, 240)
    vehicle = Vehicle(width / 2, height / 2)

    vehicle.velocity = Py5Vector2D(3, 4)
    vehicle.max_speed = 3.0   # Maximum speed.
    vehicle.max_force = 0.15  # Also, a maximum force.

def draw():
    background(255)

    if debug:
        stroke(0)
        no_fill()
        rect_mode(CENTER)
        rect(width / 2, height / 2, width - OFFSET * 2, height - OFFSET * 2)

    # Call the appropriate steering behaviors for agents.
    vehicle.boundaries(OFFSET)
    vehicle.update()
    vehicle.show()


# The function(s) below are for mouse interaction

def mouse_pressed():
    global debug
    debug = not debug
