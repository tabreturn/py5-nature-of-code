# PY5 IMPORTED MODE CODE


#class Mover:
class Body:  # The mover is now called a body.

    def __init__(self, x: float, y: float, mass: float):
        # Set these variables with arguments.
        self.mass = mass
        self.position = Py5Vector2D(x, y)

        self.radius = mass * 8
#        self.radius = sqrt(self.mass) * 4

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
        circle(self.position.x, self.position.y, self.radius * 2)
        # Stay tuned for an improvement on this to come later in the chapter!

    def check_edges(self) -> None:
        """An object bounces when it hits the edges of the canvas."""

        # A new variable to simulate an inelastic collision:
        # 10% of the velocity's x- or y-component is lost.
        bounce = -0.9

        if self.position.x > width - self.radius:
            self.position.x = width - self.radius
            self.velocity.x *= bounce
        elif self.position.x < 0 + self.radius:
            self.velocity.x *= bounce
            self.position.x = 0 + self.radius

        if self.position.y > height - self.radius:
            # Quick way to reverse the object's direction when it reaches edge.
            self.velocity.y *= bounce
            self.position.y = height - self.radius

    # Computed property -- accessed as body.contact_edge (no parentheses).
    def contact_edge(self) -> bool:
        """The mover is touching the edge when it's within 1 pixel."""

        return self.position.y > height - self.radius - 1

    # The attract() method is now part of the Body class.

    # Needs "G" because Python modules have isolated namespaces.
    # (p5.js sketches share a single global scope)
    def attract(self, body: 'Body', G: float) -> Py5Vector2D:
        # What's the force's direction?
        force = self.position - body.position
        # The length (magnitude) is the distance between the two objects.
        distance = force.mag
        # Constrain the distance so your circle doesn't spin out of control.
        distance = constrain(distance, 5, 25)
        # The constrain() function limits distance value -- min (5), max (25).

        # Calculate the strength of the attraction force.
        strength = (G * self.mass * body.mass) / (distance ** 2)
        force.set_mag(strength)

        return force  # Return the force so it can be applied!
