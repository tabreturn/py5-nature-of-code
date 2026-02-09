# PY5 IMPORTED MODE CODE


class Attractor:

    def __init__(self):
        # Attractor object doesn't move; it needs just a mass and position.
        self.position = Py5Vector2D(width / 2, height / 2)
        self.mass = 20

        # The attribute(s) below are for mouse interaction
        self.drag_offset = Py5Vector2D()
        self.dragging = self.rollover = False

    # Needs "G" parameter because Python modules have isolated namespaces.
    # (p5.js sketches share a single global scope)
    def attract(self, mover: 'Mover', G: float) -> Py5Vector2D:
        # What's the force's direction?
        force = self.position - mover.position
        # The length (magnitude) is the distance between the two objects.
        distance = force.mag
        # Constrain the distance so the circle doesn't spin out of control.
        distance = constrain(distance, 5, 25)
        # The constrain() function limits distance value -- min (5), max (25).

        # Calculate the strength of the attraction force.
        strength = (G * self.mass * mover.mass) / (distance ** 2)
        force.set_mag(strength)

        return force  # Return the force so it can be applied!

    def show(self) -> None:
        stroke_weight(4)
        stroke(0)
        if self.dragging or self.rollover: fill(175)
        else: fill(175, 175)
        circle(self.position.x, self.position.y, self.mass * 2)

    # The method(s) below are for mouse interaction

    def handle_press(self, mx: int, my: int) -> None:
        if dist(mx, my, *self.position) < self.mass:
            self.dragging = True
            self.drag_offset = self.position - Py5Vector2D(mx, my)

    def handle_hover(self, mx, my) -> None:
        self.rollover = dist(mx, my, *self.position) < self.mass

    def stop_dragging(self) -> None:
        self.dragging = False

    def handle_drag(self, mx, my) -> None:
        if self.dragging:
            self.position = Py5Vector2D(mx, my) + self.drag_offset
