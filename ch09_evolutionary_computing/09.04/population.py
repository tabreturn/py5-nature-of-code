from dna import DNA
from py5 import random
from flower import Flower


class Population:
    def __init__(self, mutation: float, length: int):
        self.mutation_rate = mutation  # Mutation rate.
        self.generations = 0  # Number of generations
        # Array to hold the current population.
        self.population = [Flower(DNA(), 40 + _ * 80, 120) for _ in range(length)]

    def show(self) -> None:
        """Display all faces."""
        for flower in self.population:
            flower.show()

    def rollover(self, mx: int, my: int) -> None:
        """Are we rolling over any of the faces?"""
        for flower in self.population:
            flower.rollover(mx, my)

    def weighted_selection(self) -> DNA:
        # Start with the first element.
        index = 0
        # Pick a starting point.
        start = random(1)
        # At the finish line?
        while start > 0:
            # Move a distance according to fitness.
            start -= self.population[index].fitness
            # Pass the baton to the next element.
            index += 1
        # Undo moving to the next element since the finish has been reached.
        index -= 1
        return self.population[index].dna

    def selection(self) -> None:
        """The selection method normalizes all the fitness values."""
        # Sum all the fitness values.
        total_fitness = sum(flower.fitness for flower in self.population)
        # Divide by the total to normalize the fitness values.
        for flower in self.population:
            flower.fitness /= total_fitness

    def reproduction(self) -> None:
        new_population = []  # Separate the array for the next generation.

        for _ in range(len(self.population)):
            # Now use the weighted selection algorithm.
            parent_a = self.weighted_selection()
            parent_b = self.weighted_selection()
            child = parent_a.crossover(parent_b)
            child.mutate(self.mutation_rate)
            # Flower goes in the new population.
            new_population.append(Flower(child, 40 + _ * 80, 120))

        # Now the new population is the current one.
        self.population = new_population
        self.generations += 1
