# PY5 IMPORTED MODE CODE


class Bob:

    def __init__(self, x: float, y: float):
        self.position = Py5Vector2D(x, y)
        self.velocity = Py5Vector2D()
        self.acceleration = Py5Vector2D()
        self.mass = 24.0
        # Arbitrary damping to simulate friction / drag.
        self.damping = 0.98
        # For user interaction.
        self.drag_offset = Py5Vector2D()
        self.dragging = False

    def update(self) -> None:
        """Standard Euler integration."""

        self.velocity += self.acceleration
        self.velocity *= self.damping
        self.position += self.velocity
        self.acceleration *= 0

    def apply_force(self, force: Py5Vector2D) -> None:
        """Newton's law: F = M * A"""

        f = force / self.mass
        self.acceleration += f

    def show(self) -> None:
        """Draw the bob."""

        stroke(0)
        stroke_weight(2)
        fill(127)
        if self.dragging: fill(200)
        circle(self.position.x, self.position.y, self.mass * 2)


    # The methods below are for mouse interaction

    def handle_press(self, mx: int, my: int) -> None:
        if dist(mx, my, *self.position) < self.mass:
            self.dragging = True
            self.drag_offset = self.position - Py5Vector2D(mx, my)

    def stop_dragging(self) -> None:
        self.dragging = False

    def handle_drag(self, mx: int, my: int) -> None:
        if self.dragging:
            self.position = Py5Vector2D(mx, my) + self.drag_offset
