# PY5 IMPORTED MODE CODE


class Mover:

    def __init__(self, x: float, y: float, mass: float):
        # Set these variables with arguments.
        self.mass = mass
        self.position = Py5Vector2D(x, y)

        self.radius = mass * 8

        self.velocity = Py5Vector2D()
        self.acceleration = Py5Vector2D()

    def apply_force(self, force: Py5Vector2D) -> None:
        """Newton's second law."""

        # Receive a force, divide by mass, and add to acceleration.
        f = force / self.mass
        self.acceleration += f

    def update(self) -> None:
        # Motion 101 from Chapter 1.
        self.velocity += self.acceleration
        self.position += self.velocity
        # Now add clearing the acceleration each time!
        self.acceleration *= 0

    def show(self) -> None:
        stroke(0)
        stroke_weight(2)
        fill(127, 127)
        # Scale the size according to mass.
        circle(self.position.x, self.position.y, self.mass * 16)
        # Stay tuned for an improvement on this to come later in the chapter!

    def check_edges(self) -> None:
        """An object bounces when it hits the edges of the canvas."""

        if self.position.x > width - self.radius:
            self.position.x = width - self.radius
            self.velocity.x *= -1
        elif self.position.x < 0 + self.radius:
            self.velocity.x *= -1
            self.position.x = 0 + self.radius

        if self.position.y > height - self.radius:
            # Quick way to reverse the object's direction when it reaches edge.
            self.velocity.y *= -1
            self.position.y = height - self.radius
