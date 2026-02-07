# PY5 IMPORTED MODE CODE


class Vehicle:

    def __init__(self, x: float, y: float):
        self.position = Py5Vector2D(x, y)
        self.velocity = Py5Vector2D()
        self.acceleration = Py5Vector2D()
        self.r = 6.0  # Additional variable for size.
        # Arbitrary values for max speed and force; try varying these!
        self.max_speed = 8.0  # Maximum speed.
        self.max_force = 0.2  # Also, a maximum force.

    def update(self) -> None:
        """Standard update function."""

        self.velocity += self.acceleration
        self.velocity.set_limit(self.max_speed)
        self.position += self.velocity
        self.acceleration *= 0

    def apply_force(self, force: Py5Vector2D) -> None:
        """Newton's second law (skipping the math)."""

        self.acceleration += force

    def seek(self, target: Py5Vector2D) -> None:
        """The seek steering force algorithm."""

        # Calculate the desired velocity to target at max speed.
        desired = target - self.position
        desired.set_mag(self.max_speed)
        # Reynolds' formula for steering force.
        steer = desired - self.velocity
        # Limit the magnitude of the steering force.
        steer.set_limit(self.max_force)
        # Use the physics model and apply the force to the object's acceleration.
        self.apply_force(steer)

    def show(self) -> None:
        """The vehicle is a triangle pointing in the direction of velocity."""

        angle = self.velocity.heading
        fill(127)
        stroke(0)
        push()
        translate(*self.position)
        rotate(angle)
        begin_shape()
        vertex(self.r * 2, 0)
        vertex(-self.r * 2, -self.r)
        vertex(-self.r * 2, self.r)
        end_shape(CLOSE)
        pop()
