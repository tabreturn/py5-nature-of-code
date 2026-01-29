# https://natureofcode.com/oscillation/#waves

size(640, 240)

DELTA_ANGLE = 0.2
AMPLITUDE = 100

background(255)

angle = 0

for x in range(0, width + 1, 24):
    # Step 1: Calculate the y-position according to amplitude and sine of angle.
    y = AMPLITUDE * sin(angle)
    # Step 2: Draw a circle at the (x, y) position.
    stroke(0)
    stroke_weight(2)
    fill(127, 127)
    circle(x, y + height / 2, 48)
    # Step 3: Increment the angle according to the delta angle.
    angle += DELTA_ANGLE
