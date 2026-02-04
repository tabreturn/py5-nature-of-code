# PY5 IMPORTED MODE CODE

from particle import Particle


class Emitter:

    def __init__(self, x: float, y: float):
        # Origin point where each particle begins.
        self.origin = Py5Vector2D(x, y)

        self.particles = []

    def add_particle(self) -> None:
        # The origin is passed to each particle when it's added to the array.
        self.particles.append(Particle(*self.origin))

    def run(self) -> None:
        particles = self.particles

        # Loop through the list backward for deletion.
        for i in range(len(particles) - 1, -1, -1):
            # Improve readability by assigning the array element to a variable.
            particle = particles[i]
            particle.run()

            if particle.dead:
                del particles[i]  # Remove particle at index i.
