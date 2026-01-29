# https://natureofcode.com/oscillation/#example-39-the-wave

DELTA_ANGLE = 0.2
start_angle = 0


def setup():
    size(640, 240)


def draw():
    global start_angle
    background(255)

    # Each time through draw(), the angle that increments is set to start_angle.
    angle = start_angle

    for x in range(0, width + 1, 24):

        y = remap(sin(angle), -1, 1, 0, height)

        stroke(0)
        stroke_weight(2)
        fill(127, 127)
        circle(x, y, 48)

        angle += DELTA_ANGLE

    start_angle += 0.02  # Increment the starting angle.
