# https://natureofcode.com/fractals/#the-koch-curve

from koch_line import KochLine


def setup():
    global segments
    size(640, 240)

    start = Py5Vector2D(0, 200)        # Left side of the canvas.
    end = Py5Vector2D(width, 200)      # Right side of the canvas.
    segments = [KochLine(start, end)]  # The first KochLine object.

    # Apply the Koch rules five times.
    for _ in range(5):
        generate()


def draw():
    background(255)
    no_loop()

    for segment in segments:
        segment.show()


def generate() -> None:
    global segments
    next_ = []  # Create the next array.

    for segment in segments:  # For every segment ...
        a, b, c, d, e = segment.koch_points()  # 5 (Koch computed) points.
        # ... add four new lines.
        next_.append(KochLine(a, b))
        next_.append(KochLine(b, c))
        next_.append(KochLine(c, d))
        next_.append(KochLine(d, e))

    segments = next_  # The next segments!
