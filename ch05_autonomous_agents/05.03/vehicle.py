# PY5 IMPORTED MODE CODE


class Vehicle:

    def __init__(self, x: float, y: float):
        self.position = Py5Vector2D(x, y)
        self.velocity = Py5Vector2D()
        self.acceleration = Py5Vector2D()
        self.r = 6.0  # Additional variable for size.
        # Arbitrary values for max speed and force; try varying these!
        self.max_speed = random(8.0)
        self.max_force = random(0.3)

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

    def arrive(self, target: Py5Vector2D) -> None:
        desired = target - self.position
        # Distance is magnitude of vector pointing from position to the target.
        d = desired.mag

        # If we are closer than 100 pixels ...
        if d < 100:
            # ... set the magnitude according to how close we are.
            m = remap(d, 0, 100, 0, self.max_speed)
            desired.set_mag(m)
        else:
            # Otherwise, proceed at maximum speed.
            desired.set_mag(self.max_speed)

        steer = desired - self.velocity  # Usual steering = desired – velocity.
        steer.set_limit(self.max_force)
        self.apply_force(steer)

    def boundaries(self, offset: float) -> None:
        """This method receives an offset from the edges."""

        desired = None  # Start with a null desired velocity.

        # Make a desired velocity that retains the y-direction of the vehicle,
        # but points the x-direction directly away from the canvas edges.
        if self.position.x < offset:
            desired = Py5Vector2D(self.max_speed, self.velocity.y)
        elif self.position.x > width - offset:
            desired = Py5Vector2D(-self.max_speed, self.velocity.y)
        # Make a desired velocity that retains the x-direction of the vehicle,
        # but points the y-direction directly away from the canvas edges.
        if self.position.y < offset:
            desired = Py5Vector2D(self.velocity.x, self.max_speed)
        elif self.position.y > height - offset:
            desired = Py5Vector2D(self.velocity.x, -self.max_speed)

        # If the desired velocity is non-null, apply steering.
        if desired is not None:
            desired.normalize()
            desired *= self.max_speed
            steer = desired - self.velocity
            steer.set_limit(self.max_force)
            self.apply_force(steer)

    def show(self) -> None:
        """The vehicle is a triangle pointing in the direction of velocity."""

        angle = self.velocity.heading
        fill(127)
        stroke(0)
        stroke_weight(2)
        push()
        translate(*self.position)
        rotate(angle)
        begin_shape()
        vertex(self.r * 2, 0)
        vertex(-self.r * 2, -self.r)
        vertex(-self.r * 2, self.r)
        end_shape(CLOSE)
        pop()
