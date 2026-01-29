# https://natureofcode.com/oscillation/#oscillation-with-angular-velocity

# The amplitude is measured in pixels.
AMPLITUDE = 200
## The period is measured in frames (the unit of time for animation).
# PERIOD = 120
ANGLE_VELOCITY = 0.05


def setup():
    global angle
    size(640, 240)
    angle = 0


def draw():
    global angle
    background(255)

#    # Calculate the horizontal position according to simple harmonic motion.
#    x = AMPLITUDE * sin(TWO_PI * frame_count / PERIOD)
    angle += ANGLE_VELOCITY
    x = AMPLITUDE * sin(angle)

    stroke(0)
    stroke_weight(2)
    fill(127)
    translate(width / 2, height / 2)
    line(0, 0, x, 0)
    circle(x, 0, 48)
