from py5 import PI, Py5Vector2D, random

# py5 drawing methods for rendering rockets
from py5 import (
  stroke, stroke_weight, push, translate, rotate,  rect_mode, fill, rect,
  begin_shape, vertex, end_shape, pop, CENTER, TRIANGLES, CLOSE
)
from dna import DNA


class Rocket:

    def __init__(self, x: float, y: float, dna: DNA):
        """A rocket has three vectors: position, velocity, and acceleration."""
        self.dna = dna  # A rocket has DNA.
        self.fitness = 0  # A rocket has fitness.
        self.position = Py5Vector2D(x, y)
        self.velocity = Py5Vector2D()
        self.acceleration = Py5Vector2D()
        self.r = 4  # Size.
        self.gene_counter = 0  # A counter for the DNA genes array.

    def calculate_fitness(self, target: Py5Vector2D) -> None:
        """How close did the rocket get?"""
        distance = self.position.dist(target)
        # Fitness is inversely proportional to distance.
        self.fitness = 1 / distance  # linear
#        self.fitness = 1 / (distance * distance)  # quadratic

    def run(self) -> None:
        """# Apply a force from the genes array."""
        self.apply_force(self.dna.genes[self.gene_counter])
        self.gene_counter += 1  # Go to the next force in the genes array.
        self.update()  # Update the rocket's physics.
        self.show()

    def apply_force(self, force: Py5Vector2D) -> None:
        """Accumulate forces into acceleration (Newton's second law)."""
        self.acceleration += force

    def update(self) -> None:
        """A simple physics engine (Euler integration)."""
        # Velocity changes according to acceleration.
        self.velocity += self.acceleration
        # Position changes according to velocity.
        self.position += self.velocity
        self.acceleration *= 0

    def show(self) -> None:
        angle = self.velocity.heading + PI / 2
        r = self.r
        stroke(0)
        stroke_weight(1)
        push()
        translate(self.position.x, self.position.y)
        rotate(angle)
        # Thrusters.
        rect_mode(CENTER)
        fill(0)
        rect(-r / 2, r * 2, r / 2, r)
        rect(r / 2, r * 2, r / 2, r)
        # Rocket body.
        fill(200)
        begin_shape(TRIANGLES)
        vertex(0, -r * 2)
        vertex(-r, r * 2)
        vertex(r, r * 2)
        end_shape(CLOSE)
        pop()
