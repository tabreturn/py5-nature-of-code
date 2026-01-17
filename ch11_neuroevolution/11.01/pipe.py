from py5 import get_current_sketch, random


class Pipe:
    def __init__(self):
        # The size of the opening between the two parts of the pipe.
         self.spacing = 100
         # A random height for the top of the pipe.
         self.height = get_current_sketch().height
         self.top = random(height - self.spacing)
         # The starting position of the bottom pipe (based on the top).
         self.x = get_current_sketch().width
         # The width of the pipe.
         self.w = 20
         # The horizontal speed of the pipe.
         self.velocity = 2

    def show(self) -> None:
        """Draw the two pipes."""
        fill(0)
        no_stroke()
        rect(self.x, 0, self.w, self.top)
        rect(self.x, self.bottom, self.w, height - self.bottom)

    def update(self) -> None:
        """Update the horizontal position."""
        self.x -= self.velocity

    def collides(self, bird: Bird) -> bool:
        # Is the bird within the vertical range of the top or bottom pipe?
        vertical_collision = bird.y < self.top or bird.y > self.bottom
        # Is the bird within the horizontal range of the pipes?
        horizontal_collision = bird.x > self.x and bird.x < self.x + self.w
        # If it's both a vertical and horizontal hit, it’s a hit!
        return vertical_collision and horizontal_collision