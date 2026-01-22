# https://natureofcode.com/vectors/#vectors-in-p5js


def setup():
#    global x, y, x_speed, y_speed
#    # Variables for position and speed of ball.
#    x = 100
#    y = 100
#    x_speed = 2.5
#    y_speed = 2

    size(640, 240)

    # Instead of a bunch of floats, you now have just two variables.
    global position, velocity
    # Note that py5 does not use createVector().
    # It provides Py5Vector, Py5Vector2D, Py5Vector3D for different dimensions.
    # https://py5coding.org/reference/py5vector.html
    position = Py5Vector2D(100, 100)
    velocity = Py5Vector2D(2.5, 2)


def draw():
#    global x, y, x_speed, y_speed
#    # Move the ball according to its speed.
#    x += x_speed
#    y += y_speed
#    # Check for bouncing.
#    if x > width or x < 0:
#        x_speed *= -1
#    if y > height or y < 0:
#        y_speed *= -1
#    # Draw the ball at the position (x, y).
#    stroke(0)
#    fill(127)
#    circle(x, y, 48)

    global position, velocity
    background(255)

    position += velocity

    # You sometimes need to refer to the individual components of a py5Vector, 
    # and can do so using the dot syntax: position.x, velocity.y, and so forth.
    if position.x > width or position.x < 0:
        velocity.x = velocity.x * -1
    if position.y > height or position.y < 0:
        velocity.y = velocity.y * -1

    stroke(0)
    fill(127)
    circle(position.x, position.y, 48)
