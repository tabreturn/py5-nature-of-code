# PY5 IMPORTED MODE CODE


class Liquid:

    def __init__(self, x: float, y: float, w: int, h: int, c: float):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        # The Liquid object includes a variable defining its drag coefficient.
        self.c = c

    def show(self) -> None:
        no_stroke()
        fill(127, 127)
        rect(self.x, self.y, self.w, self.h)

    def contains(self, mover: 'Mover') -> bool:
        # Store position in a separate variable to make the code more readable.
        pos = mover.position

        # This Boolean expression determines whether the position vector is
        # contained within the rectangle defined by the Liquid class.
        return (
          pos.x > self.x and pos.x < self.x + self.w and
          pos.y > self.y and pos.y < self.y + self.h
        )

    def calculate_drag(self, mover: 'Mover') -> float:
        speed = mover.velocity.mag
        # Calculate the force's magnitude.
        drag_magnitude = self.c * speed * speed
        # Calculate the force's direction.
        drag_force = mover.velocity * -1
        # Finalize the force: set the magnitude and direction together.
        drag_force.set_mag(drag_magnitude)
        # Return the force.
        return drag_force
