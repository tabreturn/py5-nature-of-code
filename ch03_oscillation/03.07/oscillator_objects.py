# https://natureofcode.com/oscillation/#example-37-oscillator-objects

from oscillator import Oscillator


def setup():
    global oscillators
    size(640, 240)

    # Initialize all objects.
    oscillators = [Oscillator() for _ in range(10)]


def draw():
    background(255)

    # Run all objects.
    for oscillator in oscillators:
        oscillator.update()
        oscillator.show()
