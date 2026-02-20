# https://natureofcode.com/fractals/#the-stochastic-version


def setup():
    size(640, 240)
    frame_rate(1)


def draw():
    global angle
    background(255)

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
        # A random number of branches.
        for _ in range(random_int(1, 4 - 1)):
            angle = random(-PI / 2, PI / 2)  # A random angle.
            push()
            rotate(angle)
            branch(length)  # Subsequent calls to branch() include a length arg.
            pop()
