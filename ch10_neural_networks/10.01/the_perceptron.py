# https://natureofcode.com/neural-networks/#the-perceptron

from perceptron import Perceptron

count = 0  # A counter to track training data points one by one


def f(x: float) -> float:
    """The formula for a line"""
    return 0.5 * x + 1


def setup():
    global count, perceptron, training
    size(640, 240)

    # The perceptron has three inputs (including bias) and learning rate 0.0001.
    perceptron = Perceptron(3, 0.0001)  # Create the perceptron.

    # Make 2,000 training data points.
    training = [
      [
        random(-width / 2, width / 2),
        random(-height / 2, height / 2),
        1,  # Don't forget to include the bias!
      ]
      for _ in range(2000)
    ]


def draw():
    global count
    background(255)

    # Reorient the canvas to match a traditional Cartesian plane.
    translate(width / 2, height / 2)
    scale(1, -1)

    # Draw the line.
    stroke(0)
    stroke_weight(2)
    line(-width / 2, f(-width / 2), width / 2, f(width / 2))

    # Get the current (x, y) of the training data.
    x, y, _ = training[count]

    # What is the desired output?
    desired = 1 if y > f(x) else -1  # The answer is +1 if y is above the line.

    # Train the perceptron.
    perceptron.train(training[count], desired)

    # For animation, train one point at a time.
    count = (count + 1) % len(training)

    # Draw all the points and color according to the output of the perceptron.
    for data_point in training:
        guess = perceptron.feed_forward(data_point)
        fill(127 if guess > 0 else 255)
        stroke_weight(1)
        stroke(0)
        circle(data_point[0], data_point[1], 8)