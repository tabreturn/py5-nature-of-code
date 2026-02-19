# PY5 IMPORTED MODE CODE


class DNA:
    def __init__(self, length: int):
        """Constructor (makes a random DNA)."""

        self.genes = [self.random_character() for _ in range(length)]
        self.fitness = 0.0

    def get_phrase(self) -> str:
        """Convert the list to a string of the phenotype."""

        return "".join(self.genes)

    def calculate_fitness(self, target: str) -> None:
        """Compute fitness as a percentage of correct characters."""

        assert len(target) == len(self.genes)
        score = sum(g == t for g, t in zip(self.genes, target))
        self.fitness = score / len(target)

    def crossover(self, partner: 'DNA') -> 'DNA':
        """Crossover."""

        child = DNA(len(self.genes))
        midpoint = random_int(len(self.genes)-1)
        child.genes[:midpoint] = self.genes[:midpoint]
        child.genes[midpoint:] = partner.genes[midpoint:]
        return child

    def mutate(self, mutationrate: float) -> None:
        """Mutation."""

        for i in range(len(self.genes)):
            if random() < mutationrate:
                self.genes[i] = self.random_character()

    def random_character(self) -> str:
        """Return a random character (letter, number, symbol, and so forth)."""

        c = random_int(32, 127-1)
        return chr(c)

