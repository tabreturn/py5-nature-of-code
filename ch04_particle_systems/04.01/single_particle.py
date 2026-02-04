# https://natureofcode.com/particles/#a-single-particle

from particle import Particle


def setup():
    global particle
    size(640, 240)
    particle = Particle(width / 2, 10)


def draw():
    global particle
    background(255)

    # Operate the single particle.
    particle.update()
    particle.show()

    # Apply a gravity force.
    gravity = Py5Vector2D(0, 0.1)
    particle.apply_force(gravity)

    # Check the particle's state and make a new particle.
    if particle.dead:
        particle = Particle(width / 2, 20)
        print("Particle dead!")
