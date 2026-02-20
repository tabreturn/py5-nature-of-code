# https://natureofcode.com/fractals/#example-81-recursive-circles-once


def setup():
    size(640, 240)


def draw():
    background(255)
    draw_circles(width / 2, height / 2, width / 2)
    no_loop()


def draw_circles(x: float, y: float, r: float) -> None:
    stroke(0)
    stroke_weight(2)
    circle(x, y, r * 2)

    if r > 4:  # Exit condition: stop when the radius is too small.
        r *= 0.75
        # Call the function inside the function (aka recursion!).
        draw_circles(x, y, r)  # Is this a paradox?


def factorial(n: int) -> int:
    """Unused function to cover the chapter's preceeding content:
    https://natureofcode.com/fractals/#implementing-recursive-functions"""

    # Instead of a regular loop to compute the factorial.
    if n <= 1:
        return 1
    return n * factorial(n - 1)

    """
    NOTE:
    On my system, py5 (Jython-based) crashes at a bit over 1700 recursive calls.
    JVM ThreadStackSize = 1024 KB (~1 MB).
    """
