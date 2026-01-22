# https://natureofcode.com/vectors/#the-point-of-vectors


def setup():
    global x, y, x_speed, y_speed
    size(640, 240)

    # Variables for position and speed of ball.
    x = 100
    y = 100
    x_speed = 2.5
    y_speed = 2


def draw():
    global x, y, x_speed, y_speed
    background(255)

    # Move the ball according to its speed.
    x += x_speed
    y += y_speed

    # Check for bouncing.
    if x > width or x < 0:
        x_speed *= -1
    if y > height or y < 0:
        y_speed *= -1

    # Draw the ball at the position (x, y).
    stroke(0)
    fill(127)
    circle(x, y, 48)
