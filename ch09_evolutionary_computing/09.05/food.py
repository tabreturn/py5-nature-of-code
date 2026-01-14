from py5 import get_current_sketch, Py5Vector2D, random
from py5 import CENTER, fill, rect_mode, square, stroke, stroke_weight


class Food:

    def __init__(self, num: int):
        """Start with some food."""
        self.food_positions = [
          Py5Vector2D(
            random(get_current_sketch().width),
            random(get_current_sketch().height)
          )
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
        fill(200)

        for position in self.food_positions:
            square(position.x, position.y, 8)

        # There's a small chance food will appear randomly.
        if random(1) < 0.001:
            self.food_positions.append(Py5Vector2D(
              random(get_current_sketch().width),
              random(get_current_sketch().height)
            ))