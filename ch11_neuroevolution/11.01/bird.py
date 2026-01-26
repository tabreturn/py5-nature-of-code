# PY5 IMPORTED MODE CODE


class Bird:
    def __init__(self):
        self.x = 50  # The bird's position (x will be constant).
        self.y = 120
        # Velocity and forces are scalar since bird moves only along the y-axis.
        self.velocity = 0.0
        self.gravity = 0.5
        self.flap_force = -10

    def flap(self) -> None:
        """The bird flaps its wings."""

        self.velocity += self.flap_force

    def update(self) -> None:
        self.velocity += self.gravity  # Add gravity.
        self.y += self.velocity
        # Dampen velocity.
        self.velocity *= 0.95
        # Handle the floor.
        if self.y > height:
            self.y = height
            self.velocity = 0

    def show(self) -> None:
        stroke_weight(2)
        stroke(0)
        fill(127)
        circle(self.x, self.y, 16)

