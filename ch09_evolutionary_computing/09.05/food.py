# PY5 IMPORTED MODE CODE


class Food:

    def __init__(self, num: int):
        """Start with some food."""

        self.food_positions = [
          Py5Vector2D(random(width), random(height))
          for _ in range(num)
        ]

    def add(self, position: Py5Vector2D) -> None:
        """Add some food at a location."""

        self.food_positions.append(position.copy)

    def run(self) -> None:
        """Display the food."""

        rect_mode(CENTER)
        stroke(0)
        stroke_weight(1)
        fill(175)

        for position in self.food_positions:
            square(position.x, position.y, 8)

        # There's a small chance food will appear randomly.
        if random() < 0.001:
            self.food_positions.append(Py5Vector2D(
              random(width), random(height)
            ))

