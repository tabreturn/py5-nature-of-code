from py5 import get_current_sketch, PI, Py5Vector2D, random

# py5 drawing methods for rendering rockets
from py5 import (
  begin_shape, CENTER, CLOSE, end_shape, fill, pop, push, rect, rect_mode,
  rotate, stroke, stroke_weight, translate, TRIANGLES, vertex,
  TWO_PI,
)
#from dna import DNA
from brain_ne import Brain
from obstacle import Obstacle


class Rocket:

#    def __init__(self, x: float, y: float, dna: DNA):
    def __init__(self, x: float, y: float, brain: Brain | None = None):
        """A rocket has three vectors: position, velocity, and acceleration."""

#        self.dna = dna  # A rocket has DNA.
        self.brain = (
          brain
          if brain is not None
          else Brain(
            inputs = 2,
            outputs = 2,  # angle and magnitude
          )
        )
        self.max_speed = 4
        self.max_force = 1

        self.fitness = 0  # A rocket has fitness.
        self.position = Py5Vector2D(x, y)
        self.velocity = Py5Vector2D()
        self.acceleration = Py5Vector2D()
        self.r = 4  # Size.
        self.gene_counter = 0  # A counter for the DNA genes array.
        self.hit_obstacle = False  # Am I stuck on an obstacle?
        self.record_distance = float('inf')  # High number to be beat instantly.
        self.hit_target = False  # Did I reach the target.
        self.finish_counter = 0  # Count how long it takes to reach target.

    def calculate_fitness(self, target: Py5Vector2D) -> None:
        """Reward finishing faster and getting close"""

        # Fitness is inversely proportional to distance.
#        distance = self.position.dist(target)
#        self.fitness = 1 / distance  # linear
#        self.fitness = 1 / (distance * distance)  # quadratic
        # Let's try to the power of 4 instead of squared!
        self.fitness = 1 / (self.finish_counter * self.record_distance)
        self.fitness **= 4
        # Lose 90% of fitness for hitting an obstacle.
        if self.hit_obstacle:
            self.fitness *= 0.1
        # Double the fitness for finishing!
        if self.hit_target:
            self.fitness *= 2

    def check_target(self, target: Obstacle) -> None:
        """How close did the rocket get?"""

        distance = self.position.dist(target.position)
        # Check whether the distance is closer than the record distance.
        if distance < self.record_distance:
            # If it is, set a new record.
            self.record_distance = distance
        # If the object reaches the target, set a Boolean flag to true.
        if target.contains(self.position):
            self.hit_target = True
        # Increase the finish counter if the rocket hasn't hit the target.
        if not self.hit_target:
            self.finish_counter += 1

    def run(self, obstacles: list[Obstacle]) -> None:
        """# Apply a force from the genes array."""

        # Stop the rocket if it has hit an obstacle.
        if not self.hit_obstacle and not self.hit_target:
#            self.apply_force(self.dna.genes[self.gene_counter])
#            # Go to the next force in the genes array.
#            self.gene_counter = (self.gene_counter + 1) % len(self.dna.genes)
            
            cs = get_current_sketch()
            inputs = [self.position.x / cs.width, self.position.y / cs.height]
            # Get the outputs from the neural network.
            outputs = self.brain.predict_continuous_01(inputs)
            # Use one output for an angle.
            angle = outputs[0] * TWO_PI
            # Use another output for the magnitude.
            magnitude = outputs[1] * self.max_force
            # Create and apply the force.
            force = Py5Vector2D.from_heading(angle).set_mag(magnitude) 
            self.apply_force(force)

            self.update()
            # Check whether the rocket has hit an obstacle.
            self.check_obstacles(obstacles)            

        self.show()

    def apply_force(self, force: Py5Vector2D) -> None:
        """Accumulate forces into acceleration (Newton's second law)."""

        self.acceleration += force

    def update(self) -> None:
        """A simple physics engine (Euler integration)."""

        self.velocity.set_limit(self.max_speed)
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

    def check_obstacles(self, obstacles: list[Obstacle]) -> None:
        """Checks whether a rocket has hit an obstacle."""

        self.hit_obstacle = any(
          obstacle.contains(self.position) for obstacle in obstacles
        )
