# https://natureofcode.com/oscillation/#polar-vs-cartesian-coordinates


def setup():
    global r, theta
    size(640, 240)
    
    # Initialize all values.
    r = height * 0.45
    theta = 0


def draw():
    global r, theta
    background(255)

    # Translate the origin point to the center of the screen.
    translate(width / 2, height / 2)

#    #  Polar coordinates (r, theta) are converted to Cartesian (x, y).
#    x = r * cos(theta)
#    y = r * sin(theta)

    # Create a unit vector pointing in the direction of an angle.
    position = Py5Vector.from_heading(theta)
    # To complete polar-to-Cartesian conversion, scale position by r.
    position *= r
    x, y = position.x, position.y
    
    # Draw the circle by using the x- and y-components of the vector.
    fill(127)
    stroke(0)
    stroke_weight(2)
    line(0, 0, x, y)
    circle(x, y, 48)

    theta += 0.02  # Increase the angle over time.
