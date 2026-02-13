# PY5 IMPORTED MODE CODE


class DNA:
    # Needs "lifespan" parameter because Python modules have isolated namespaces.
    # (p5.js sketches share a single global scope)
    def __init__(self, lifespan: int):
        """The genetic sequence is a list of vectors."""

        self.max_force = 0.1  # How strong can the thrusters be?
        # Notice that the length of genes is equal to global LIFESPAN variable.
        self.genes = [
          # Scale the vectors randomly, but not stronger than the maximum force.
          Py5Vector2D().random() * random(0, self.max_force)
          # Notice that the length of genes is equal to a lifespan variable.
          for _ in range(lifespan)
        ]

    def crossover(self, partner: 'DNA') -> 'DNA':
        """Crossover."""

        child = DNA(len(self.genes))
        midpoint = floor(random(len(self.genes)))
        child.genes[:midpoint] = self.genes[:midpoint]
        child.genes[midpoint:] = partner.genes[midpoint:]
        return child

    def mutate(self, mutation_rate: float) -> None:
        """Mutation."""

        for i, gene in enumerate(self.genes):
            if random(1) < mutation_rate:
                angle = random(TAU)
                self.genes[i] = Py5Vector2D.from_heading(angle).set_mag(
                  random(self.max_force)
                )

