# PY5 IMPORTED MODE CODE


class Particle:

    def __init__(self, x: float, y: float):
        """A Particle object is just another name for a mover.
        It has position, velocity, and acceleration."""

        self.position = Py5Vector2D(x, y)
        self.acceleration = Py5Vector2D()
        # For demonstration purposes, the particle has a random velocity.
        self.velocity = Py5Vector2D(random(-1, 1), random(-2, 0))

        # A new variable to keep track of how long the particle has been "alive."
        # It starts at 255 and counts down to 0.
        self.lifespan = 255.0

    def update(self) -> None:
        self.velocity += self.acceleration
        self.position += self.velocity
        self.acceleration *= 0

        # Life span decreases.
        self.lifespan -= 2.0

    def show(self) -> None:
        # Since the life ranges from 255 to 0, it can also be used for alpha.
        stroke(0, self.lifespan)
        stroke_weight(2)
        fill(127, self.lifespan)

        circle(self.position.x, self.position.y, 8)

    def apply_force(self, force: Py5Vector2D) -> None:
        """Keep the same physics model as in previous chapters."""
        self.acceleration += force

    # Computed property -- accessed as particle.dead (no parentheses).
    @property
    def dead(self):
        """Is the particle still alive?"""

        return self.lifespan < 0.0
