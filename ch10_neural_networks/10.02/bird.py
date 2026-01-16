from py5 import get_current_sketch


class Bird:
    def __init__(self):
        self.x = 50  # The bird's position (x will be constant).
        self.y = 120
        # Velocity and forces are scalar since bird moves only along the y-axis.
        self.velocity = 0
        self.gravity = 0.5
        self.flap_force = -10

    def flap(self):
        """The bird flaps its wings."""
        self.velocity += self.flap_force

    def update(self):
        self.velocity += self.gravity  # Add gravity.
        self.y += self.velocity
        # Dampen velocity.
        self.velocity *= 0.95
        # Handle the floor.
        if self.y > get_current_sketch().height:
            self.y = get_current_sketch().height
            self.velocity = 0