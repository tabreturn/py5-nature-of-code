# PY5 IMPORTED MODE CODE


class Particle:

    def __init__(self, x: float, y: float, img: Py5Image):
        """A Particle object is just another name for a mover.
        It has position, velocity, and acceleration."""

        self.position = Py5Vector2D(x, y)
        self.acceleration = Py5Vector2D()
#        # For demonstration purposes, the particle has a random velocity.
#        self.velocity = Py5Vector2D(random(-1, 1), random(-2, 0))
        vx = random_gaussian(0, 0.3)
        vy = random_gaussian(-1, 0.3)
        self.velocity = Py5Vector2D(vx, vy)

        # A new variable to keep track of how long the particle has been "alive."
#        self.lifespan = 255.0  # It starts at 255 and counts down to 0.
        self.lifespan = 100.0

        # Add a mass property. Vary mass for different, interesting results!
        self.mass = 1

        self.img = img

    def update(self) -> None:
        self.velocity += self.acceleration
        self.position += self.velocity
        self.acceleration *= 0

        # Life span decreases.
        self.lifespan -= 2.0

    def show(self) -> None:
#        # Since the life ranges from 255 to 0, it can also be used for alpha.
#        stroke(0, self.lifespan)
#        stroke_weight(2)
#        fill(127, self.lifespan)
#        circle(self.position.x, self.position.y, 8)

        image_mode(CENTER)
        # Note that tint() is the image equivalent of a shape's fill().
#        tint(255, self.lifespan)
        tint(255, 100, 255, self.lifespan)
        image(self.img, self.position.x, self.position.y)

    def apply_force(self, force: Py5Vector2D) -> None:
        """Keep the same physics model as in previous chapters."""
        # Divide force by mass.
        f = Py5Vector2D(force.x, force.y)
        f /= self.mass

        self.acceleration += f

    def run(self) -> None:
#        gravity = Py5Vector2D(0, 0.05)
#        self.apply_force(gravity)
        self.update()
        self.show()

    # Computed property -- accessed as particle.dead (no parentheses).
    @property
    def dead(self) -> bool:
        """Is the particle still alive?"""

        return self.lifespan < 0.0
