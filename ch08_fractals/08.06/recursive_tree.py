# https://natureofcode.com/fractals/#the-deterministic-version


def setup():
    size(640, 240)


def draw():
    global angle
    background(255)

    # Map the angle to range from 0° to 90° (HALF_PI) according to mouse_x.
    angle = remap(mouse_x, 0, width, 0, HALF_PI)

    # Start the tree from the bottom of the canvas.
    translate(width / 2, height)
    stroke(0)
    stroke_weight(2)
    branch(80)


def branch(length: float) -> None:  # Each branch receives its length as an arg.
    line(0, 0, 0, -length)  # Draw the branch.
    translate(0, -length)   # Translate to the end.
    length *= 0.67          # Each branch's length shrinks by one-third.

    if length > 2:  # Exit condition for the recursion!
        push()
        # Rotate to the right and branch again.
        rotate(angle)
        branch(length)  # Subsequent calls to branch() include a length arg.
        pop()

        push()
        # Rotate to the left and branch again.
        rotate(-angle)
        branch(length)
        pop()
