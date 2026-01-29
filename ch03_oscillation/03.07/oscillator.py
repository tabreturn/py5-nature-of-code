# PY5 IMPORTED MODE CODE


class Oscillator:

    def __init__(self):
        # Use a p5.Vector to track two angles!
        self.angle = Py5Vector2D()
        # Random velocities and amplitudes.
        self.angle_velocity = Py5Vector2D(
          random(-0.05, 0.05), random(-0.05, 0.05)
        )
        self.amplitude = Py5Vector2D(
          random(20, width / 2), random(20, height / 2)
        )

    def update(self) -> None:
        self.angle += self.angle_velocity

    def show(self) -> None:
        x = sin(self.angle.x) * self.amplitude.x  # Oscillating on the x-axis.
        y = sin(self.angle.y) * self.amplitude.y  # Oscillating on the y-axis.

        push()
        translate(width / 2, height / 2)
        stroke(0)
        stroke_weight(2)
        fill(127)
        # Draw the oscillator as a line connecting a circle.
        line(0, 0, x, y)
        circle(x, y, 32)
        pop()
