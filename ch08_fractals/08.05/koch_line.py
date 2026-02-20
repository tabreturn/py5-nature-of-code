# PY5 IMPORTED MODE CODE


class KochLine:

    def __init__(self, a: Py5Vector2D, b: Py5Vector2D):
        """A line between two points: a and b."""

        # a and b are p5.Vector objects.
        self.start = a.copy
        self.end = b.copy

    def show(self) -> None:
        stroke_weight(2)
        line(*self.start, *self.end)  # Draw the line from a to b.

    def koch_points(self) -> list[Py5Vector2D]:
        # It's best to avoid making copies whenever possible,
        # but we need a new object so segments can move independently.
        a = self.start.copy
        e = self.end.copy

        v = self.end - self.start  # Create a vector from start to end.
        v /= 3  # Shorten the length to one-third.
        b = a + v  # Add that vector to beginning of line to find new point.
        d = b + v  # d is just another one-third of the way past b!
        v.rotate(-PI / 3)  # Rotate –π/3 radians (negative angle rotates 'up').
        c = b + v  # Move along from b by v to get to point c.

        return [a, b, c, d, e]  # Return all five points in an array.
        