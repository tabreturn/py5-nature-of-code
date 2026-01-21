from py5 import random


class Perceptron:
    def __init__(self, n: int, learning_constant: float):
        """The argument n determines number of inputs (including the bias)."""

        self.learning_constant = learning_constant
        self.weights = [
          # The weights are picked randomly to start.
          random(-1, 1)
          for _ in range(n)
        ]

    def feed_forward(self, inputs: tuple[float]) -> int:
        """Return an output based on inputs."""

        weighted_sum = sum(
          inputs[i] * self.weights[i]
          for i in range(len(self.weights))
        )
        # The perceptron is guessing: Is it on one side of the line or other?
        return self.activate(weighted_sum)

    def activate(self, weighted_sum: float) -> int:
        """The output is a +1 or –1."""

        return 1 if weighted_sum > 0 else -1

    def train(self, inputs: list[float], desired: float) -> None:
        """
        Step 1: Provide the inputs (as arguments) and known answer.
        Step 2: Guess according to those inputs.
        Step 3: Compute the error (the difference between desired and guess).
        Step 4: Adjust all the weights according to error and learning constant.
        """

        guess = self.feed_forward(inputs)
        error = desired - guess
        for i in range(len(self.weights)):
            self.weights[i] += error * inputs[i] * self.learning_constant

