# PY5 IMPORTED MODE CODE


class Mover:

    def __init__(self, x: float, y: float, mass: float):
        # Set these variables with arguments.
        self.mass = mass
        self.position = Py5Vector2D(x, y)

        self.radius = mass * 8

        self.velocity = Py5Vector2D()
        self.acceleration = Py5Vector2D()

        # Variables for angular motion.
        self.angle = 0
        self.angle_velocity = 0
        self.angle_acceleration = 0

    def apply_force(self, force: Py5Vector2D) -> None:
        """Newton's second law."""

        # Receive a force, divide by mass, and add to acceleration.
        f = force / self.mass
        self.acceleration += f

    def update(self) -> None:
        mouse = Py5Vector2D(mouse_x, mouse_y)
        dir = mouse - self.position
        dir.normalize()
        dir *= 0.5
        self.acceleration = dir

        # Motion 101 from Chapter 1.
        self.velocity += self.acceleration
        self.velocity.set_limit(4)
        self.position += self.velocity

        # Newfangled angular motion

        # Calculate angular acceleration according to acceleration's x-component.
        self.angle_acceleration = self.acceleration.x / 10.0
        self.angle_velocity += self.angle_acceleration
        # Use constrain() to ensure angular velocity doesn't spin out of control.
        self.angle_velocity = constrain(self.angle_velocity, -0.1, 0.1)
        self.angle += self.angle_velocity

        # Now add clearing the acceleration each time!
        self.acceleration *= 0

    def show(self) -> None:
        # Once can use atan2() to account for all possible directions:
        # angle = atan2(self.velocity.y / self.velocity.x)
        angle = self.velocity.heading  # But this is the easiest way to do this!

        stroke(0)
        stroke_weight(2)
        fill(127, 127)

        # Use push() to save the current state so the rotation of this shape
        # doesn't affect the rest of the world.
        push()
        # Set the origin at the shape's position.
        translate(self.position.x, self.position.y)
        rotate(angle)  # Rotate according to that angle.
        rect_mode(CENTER)
        rect(0, 0, 30, 10)
#        rotate(self.angle)  # Rotate by the angle.
#        # Scale the size according to mass.
#        circle(self.position.x, self.position.y, self.radius * 2)
#        circle(0, 0, self.radius * 2)
#        line(0, 0, self.radius, 0)
        # Use pop() to restore the previous state after rotation is complete.
        pop()
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

    # Computed property -- accessed as mover.contact_edge (no parentheses)
    def contact_edge(self) -> bool:
        """The mover is touching the edge when it's within 1 pixel."""
        return self.position.y > height - self.radius - 1
