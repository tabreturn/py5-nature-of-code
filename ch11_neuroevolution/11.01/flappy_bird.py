# https://natureofcode.com/neuroevolution/#reinforcement-learning

from bird import Bird
from pipe import Pipe


def setup():
    global bird, pipes
    size(640, 240)
    # Create a bird and start with one pipe.
    bird = Bird()
    pipes = [Pipe()]


def mouse_pressed():
    # The bird flaps its wings when the mouse is clicked.
    bird.flap()


def draw():
    background(255)

    # Handle all the pipes.
    for pipe in reversed(pipes):
        pipe.show()
        pipe.update()

        if pipe.collides(bird):
            text('OOPS!', pipe.x, pipe.top + 20)

        if pipe.off_screen:
            pipes.remove(pipe)

    # Update and show the bird.
    bird.update()
    bird.show()

    # Add a new pipe every 100 frames.
    if frame_count % 100 == 0:
        pipes.append(Pipe())

