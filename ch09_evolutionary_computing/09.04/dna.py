from py5 import floor, random


class DNA:
    """Flower genotype."""

    def __init__(self):
        # The genetic sequence (14 properties for each flower).
        # Each gene is a random value from 0 to 1.
        self.genes = [random(1) for _ in range(14)]

    def crossover(self, partner: 'DNA') -> 'DNA':
        """Crossover."""
        child = DNA()
        midpoint = floor(random(len(self.genes)))
        child.genes[:midpoint] = self.genes[:midpoint]
        child.genes[midpoint:] = partner.genes[midpoint:]
        return child

    def mutate(self, mutation_rate: float) -> None:
        """Mutation."""
        for i, _ in enumerate(self.genes):
            if random(1) < mutation_rate:
                self.genes[i] = random(1)
