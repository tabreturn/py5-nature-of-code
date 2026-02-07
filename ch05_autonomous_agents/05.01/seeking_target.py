# https://natureofcode.com/autonomous-agents/#the-steering-force

from vehicle import Vehicle


def setup():
    global vehicle
    size(640, 240)
    vehicle = Vehicle(width / 2, height / 2)

    vehicle.max_speed = 8.0  # Maximum speed.
    vehicle.max_force = 0.2  # Also, a maximum force.


def draw():
    background(255)

    mouse = Py5Vector2D(mouse_x, mouse_y)

    # Draw an ellipse at the mouse position.
    fill(127)
    stroke(0)
    stroke_weight(2)
    circle(mouse.x, mouse.y, 48)

    # Call the appropriate steering behaviors for agents.
    vehicle.seek(mouse)
    vehicle.update()
    vehicle.show()
