# https://natureofcode.com/oscillation/#angular-motion

angle = 0                    # Position.
angle_velocity = 0           # Velocity.
ANGLE_ACCELERATION = 0.0001  # Acceleration.


def setup():
    size(640, 240)


def draw():
    global angle, angle_velocity

    background(255)
    translate(width / 2, height / 2)

    rotate(angle)  # Rotate according to that angle.

    stroke(0)
    stroke_weight(2)
    fill(127)
    line(-60, 0, 60, 0)
    circle(60, 0, 16)
    circle(-60, 0, 16)

    # Angular equivalent of JS velocity.add(acceleration).
    angle_velocity += ANGLE_ACCELERATION
    # Angular equivalent of JS position.add(velocity).
    angle += angle_velocity
