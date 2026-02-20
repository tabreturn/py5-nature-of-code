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


def branch(len_: float) -> None:  # Each branch receives its length as argument.
    line(0, 0, 0, -len_)  # Draw the branch.
    translate(0, -len_)   # Translate to the end.
    len_ *= 0.67          # Each branch's length shrinks by one-third.

    if len_ > 2:  # Exit condition for the recursion!
        push()
        # Rotate to the right and branch again.
        rotate(angle)
        branch(len_)  # Subsequent calls to branch() include length argument.
        pop()

        push()
        # Rotate to the left and branch again.
        rotate(-angle)
        branch(len_)
        pop()
