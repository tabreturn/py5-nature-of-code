from py5 import floor, Py5Vector2D, random, TWO_PI


class DNA:
    # Needs "life_span" because Python modules have isolated namespaces.
    # (p5.js sketches share a single global scope)
    def __init__(self, life_span: int):
        """The genetic sequence is an array of vectors."""
        self.max_force = 0.1  # How strong can the thrusters be?
        # Notice that the length of genes is equal to global LIFE_SPAN variable.
        self.genes = [
          # Scale the vectors randomly, but not stronger than the maximum force.
          Py5Vector2D().random() * random(0, self.max_force)
          # Notice that the length of genes is equal to a life_span variable.
          for _ in range(life_span)
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
                angle = random(TWO_PI)
                self.genes[i] = Py5Vector2D.from_heading(angle).set_mag(
                  random(self.max_force)
                )
