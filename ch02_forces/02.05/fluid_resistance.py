# https://natureofcode.com/forces/#air-and-fluid-resistance

from mover import Mover
from liquid import Liquid


def setup():
    global movers, liquid
    size(640, 240)

    # Initialize an array of Mover objects.
    movers = [
      Mover(
        40 + i * 70, 0,  # The x-values are spaced out evenly according to i.
        random(0.5, 3),  # Use a random mass for each one.
      )
      for i in range(9)
    ]

    # Initialize a Liquid object. Low coefficient (0.1) for a weaker effect.
    liquid = Liquid(0, height / 2, width, height / 2, 0.1)


def draw():
    background(255)

    liquid.show()  # Draw the liquid.

    for mover in movers:
        # Is the mover in the liquid?
        if liquid.contains(mover):
            # Calculate the drag force.
            drag_force = liquid.calculate_drag(mover)
            # Apply the drag force to mover.
            mover.apply_force(drag_force)

        # Gravity scaled by mass here!
        gravity = Py5Vector2D(0, 0.1 * mover.mass)
        # Apply gravity.
        mover.apply_force(gravity)
        # Update and display the mover.
        mover.update()
        mover.check_edges()
        mover.show()
