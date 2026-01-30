# PY5 IMPORTED MODE CODE


class Pendulum():

    def __init__(self, x: float, y: float, r: float):
        """Many variables keep track of the pendulum's various properties."""
        self.r = r                      # Length of arm.
        self.angle = PI / 4             # Pendulum arm angle.
        self.angle_velocity = 0         # Angular velocity.
        self.angle_acceleration = 0     # Angular acceleration.
        self.pivot = Py5Vector2D(x, y)  # Position of pivot.
        self.bob = Py5Vector2D()        # Position of bob.
        self.damping = 0.99             # Arbitrary damping.
        self.ballr = 24                 # Arbitrary bob radius.
        self.dragging = False

    def update(self) -> None:
        GRAVITY = 0.4  # An arbitrary constant.
        
        # As long as we aren't dragging the pendulum, let it swing!
        if not self.dragging:
            # Formula for angular acceleration.
            self.angle_acceleration = -1 * GRAVITY * sin(self.angle) / self.r
            # Standard angular motion algorithm.
            self.angle_velocity +=  self.angle_acceleration  # Increment velocity.
            self.angle += self.angle_velocity  # Increment angle.
            # Apply some damping.
            self.angle_velocity *= self.damping

    def show(self) -> None:
        # Apply polar-to-Cartesian conversion. Instead of creating a new vector each time,
        # use set() to update the bob’s position.
        self.bob.x = self.r * sin(self.angle) + self.pivot.x
        self.bob.y = self.r * cos(self.angle) + self.pivot.y
        # The arm.
        stroke(0)
        stroke_weight(2)
        line(self.pivot.x, self.pivot.y, self.bob.x, self.bob.y)
        # The bob.
        fill(127)
        circle(self.bob.x, self.bob.y, self.ballr * 2)

    # The methods below are for mouse interaction

    def handle_press(self, mx: int, my: int) -> None:
        if dist(mx, my, *self.bob) < self.ballr:
            self.dragging = True

    def stop_dragging(self) -> None:
        self.dragging = False
        self.angle_velocity = 0

    def handle_drag(self, mx: int, my: int) -> None:
        if self.dragging:
            diff = Py5Vector2D(mx, my) - self.pivot
            self.angle = atan2(diff.x, diff.y)
