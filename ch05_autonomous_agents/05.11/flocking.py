# https://natureofcode.com/autonomous-agents/#flocking

from boid import Boid
from flock import Flock


def setup():
    global flock
    size(640, 240)

    flock = Flock()
    # The flock starts out with 120 boids.
    for _ in range(120):
        boid = Boid(width / 2, height / 2, 3.0, 0.05)
        flock.add_boid(boid)


def draw():
    background(255)
    flock.run()
