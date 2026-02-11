# PY5 IMPORTED MODE CODE

from particle import Particle
#from confetti import Confetti


class Emitter:

    def __init__(self, x: float, y: float):
        self.origin = Py5Vector2D(x, y)  # Point where each particle begins.
        self.particles: list[Particle] = []

    def add_particle(self) -> None:
#        # The origin is passed to each particle when it's added to the list.
#        self.particles.append(Particle(*self.origin))

#        # A 50% chance of adding each kind of particle.
#        if random() < 0.5:
#            self.particles.append(Particle(*self.origin))
#        else:
#            self.particles.append(Confetti(*self.origin))

        self.particles.append(Particle(*self.origin))

    def apply_force(self, force: Py5Vector2D) -> None:
        # Use a for in loop to apply the force to all particles.
        for particle in self.particles:
            particle.apply_force(force)

    def apply_repeller(self, repeller: 'Repeller') -> None:
        """Calculate a force for each particle based on a repeller."""

        for particle in self.particles:
            force = repeller.repel(particle)
            particle.apply_force(force)

    def run(self) -> None:
        particles = self.particles

        # Loop through the list backward for deletion.
        for i in range(len(particles) - 1, -1, -1):
            # Improve readability by assigning the list element to a variable.
            particle = particles[i]
            particle.run()

            if particle.dead:
                del particles[i]  # Remove particle at index i.
