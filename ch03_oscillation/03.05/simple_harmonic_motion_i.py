# https://natureofcode.com/oscillation/#example-35-simple-harmonic-motion-i

# The amplitude is measured in pixels.
AMPLITUDE = 200
# The period is measured in frames (the unit of time for animation).
PERIOD = 120


def setup():
    size(640, 240)


def draw():
    background(255)

    # Calculate the horizontal position according to simple harmonic motion.
    x = AMPLITUDE * sin(TAU * frame_count / PERIOD)

    stroke(0)
    stroke_weight(2)
    fill(127)
    translate(width / 2, height / 2)
    line(0, 0, x, 0)
    circle(x, 0, 48)
