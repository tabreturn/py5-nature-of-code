# PY5 IMPORTED MODE CODE


class DNA:
    """Flower genotype."""

    def __init__(self):
        # The genetic sequence (14 properties for each flower).
        # Each gene is a random value from 0 to 1.
        self.genes = [random() for _ in range(14)]

    def crossover(self, partner: 'DNA') -> 'DNA':
        """Crossover."""

        child = DNA()
        midpoint = random_int(len(self.genes)-1)
        child.genes[:midpoint] = self.genes[:midpoint]
        child.genes[midpoint:] = partner.genes[midpoint:]
        return child

    def mutate(self, mutation_rate: float) -> None:
        """Mutation."""

        for i, _ in enumerate(self.genes):
            if random() < mutation_rate:
                self.genes[i] = random()

