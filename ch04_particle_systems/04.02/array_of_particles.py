# https://natureofcode.com/particles/#an-array-of-particles

from particle import Particle

particles = []  # Start with an empty list.
TOTAL = 10


def setup():
    size(640, 240)


def draw():
    global particles
    background(255)

    # A new Particle object is added to the list every cycle through draw().
    particles.append(Particle(width / 2, 20))

    # Loop through the list backward for deletion.
    for i in range(len(particles) - 1, -1, -1):
        # Improve readability by assigning the array element to a variable.
        particle = particles[i]
        particle.run()

        if particle.dead:
            del particles[i]  # Remove particle at index i.
