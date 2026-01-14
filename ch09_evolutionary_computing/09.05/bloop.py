from py5 import (
  circle, fill, get_current_sketch, noise, Py5Vector2D, stroke, remap, random
)
from dna import DNA
from food import Food


class Bloop:

    def __init__(self, position: Py5Vector2D, dna: DNA):
        self.dna = dna
        self.max_speed = remap(self.dna.genes[0], 0, 1, 15, 0)
        self.r = remap(self.dna.genes[0], 0, 1, 0, 25)
        # DNA will determine size and max speed. Bigger bloop = slower it is.
        self.health = 200.0  # A variable to track the bloop's health.
        self.position = position
        # Each bloop will use a different part of the 1D noise space.
        self.xoff = random(1000)
        self.yoff = random(1000)

    def eat(self, food: Food) -> None:
        food_positions = food.food_positions
        # Check all the food vectors.
        for i in reversed(range(len(food_positions))):
            position = food_positions[i]
            # How far away is the bloop?
            distance = Py5Vector2D.dist(self.position, position)
            # If it is within its radius ...
            if distance < self.r * 2:
                # ... increase health and remove the food!
                self.health += 100
                food_positions.pop(i)

    def reproduce(self) -> 'Bloop':
        """This method will return a new child bloop."""
        # A 0.5% chance of executing the code inside the if statement.
        if random(1) < 0.0005:
            # A child is an exact copy of a single parent.
            child_dna = self.dna.copy()
            # 1% mutation rate
            child_dna.mutate(0.01)
            # The new bloop starts at this bloop's position.
            return Bloop(self.position.copy, child_dna)

    def dead(self) -> bool:
        """A method to test whether the bloop is alive or dead."""
        return self.health < 0.0

    def run(self) -> None:
        self.update()
        self.borders()
        self.show()

    def update(self) -> None:
        self.health -= 0.2  # Death is always looming.
        # Assign simple movement and velocity with Perlin noise.
        vx = remap(noise(self.xoff), 0, 1, -self.max_speed, self.max_speed)
        vy = remap(noise(self.yoff), 0, 1, -self.max_speed, self.max_speed)
        self.xoff += 0.01
        self.yoff += 0.01
        velocity = Py5Vector2D(vx, vy)
        self.position += velocity

    def borders(self) -> None:
        """Wraparound."""
        sketch = get_current_sketch()
        if self.position.x < -self.r: self.position.x = sketch.width + self.r
        elif self.position.x > sketch.width + self.r: self.position.x = -self.r
        if self.position.y < -self.r: self.position.y = sketch.height + self.r
        elif self.position.y > sketch.height + self.r: self.position.y = -self.r

    def show(self) -> None:
        """A bloop is a circle."""
        stroke(0, self.health)
        fill(0, self.health)
        circle(self.position.x, self.position.y, self.r * 2)