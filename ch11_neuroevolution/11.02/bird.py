from py5 import fill, circle, get_current_sketch, stroke, stroke_weight
import sys, os; sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from brain_ne import Brain


class Bird:
    def __init__(self, brain: Brain | None = None):
        # A bird's brain receives four inputs classifying into one of two labels.
        self.brain = (
          brain
          if brain is not None  # Check whether a brain was passed in.
          else Brain(           # If not, make a new one.
            inputs = 4,
            outputs = 1,  # single logit for binary action (flap vs no flap)
          )
        )
        self.x = 50  # The bird's position (x will be constant).
        self.y = 120.0
        # Velocity and forces are scalar since bird moves only along the y-axis.
        self.velocity = 0.0
        self.gravity = 0.5
        self.flap_force = -10.0
        self.fitness = 0.0  # The bird's fitness
        self.alive = True  # Is the bird alive or not?

    def flap(self) -> None:
        """The bird flaps its wings."""

        self.velocity += self.flap_force

    def update(self) -> None:
        self.velocity += self.gravity  # Add gravity.
        self.y += self.velocity
        # Dampen velocity.
        self.velocity *= 0.95
        # Handle the floor.
#        if self.y > get_current_sketch().height:
#            self.y = get_current_sketch().height
#            self.velocity = 0
        if self.y > get_current_sketch().height or self.y < 0:
            self.alive = False
        # Increment the fitness each time through update().
        self.fitness += 1

    def show(self) -> None:
        stroke_weight(2)
        stroke(0)
        fill(127, 200)
        circle(self.x, self.y, 16)

    def think(self, pipes: list['Pipe']) -> None:
        next_pipe = None
        # The next pipe is the one that hasn't passed the bird yet.
        for pipe in pipes:
            if pipe.x + pipe.w > self.x:
                next_pipe = pipe
                break

        # All the inputs are now normalized by width and height.
        width, height = get_current_sketch().width, get_current_sketch().height
        inputs = [
          self.y / height,                 # y-position of the bird.
          self.velocity / height,          # y-velocity of the bird.
          next_pipe.top / height,          # Top opening of the next pipe.
          (next_pipe.x - self.x) / width,  # Distance to the next pipe.
        ]

        result = self.brain.classify_binary(inputs)
        # classify_binary() returns True (flap) or False (no flap)
        if result:
            self.flap()

