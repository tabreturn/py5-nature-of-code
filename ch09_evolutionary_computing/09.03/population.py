from dna import DNA
from py5 import Py5Vector2D, random
from rocket import Rocket


class Population:
    # Needs "life_span", "xy" because Python modules have isolated namespaces.
    # (p5.js sketches share a single global scope)
    def __init__(self, mutation: float, length: int, life_span: int, xy: tuple):
        """Population has variables to keep track of the mutation rate, current
        population array, and number of generations."""
        self.mutation_rate = mutation  # Mutation rate.
        self.generations = 0  # Number of generations
        self.x, self.y = xy
        # Array to hold the current population.
        self.population = [
          Rocket(self.x, self.y, DNA(life_span)) for _ in range(length)
        ]

    def live(self, obstacles, target: Py5Vector2D) -> None:
        # Needs "target" because Python modules have isolated namespaces.
        """The run() method takes care of the simulation, updates the rocket's
        position, and draws it to the canvas."""
        for rocket in self.population:
            rocket.check_target(target)
            rocket.run(obstacles)

    def target_reached(self) -> bool:
        """Did anything finish?"""
        return any(rocket.hit_target for rocket in self.population)

    def fitness(self, target: Py5Vector2D) -> None:
        # Needs "target" because Python modules have isolated namespaces.
        """Calculate the fitness for each rocket."""
        for rocket in self.population:
            rocket.calculate_fitness(target)

    def selection(self) -> None:
        """The selection method normalizes all the fitness values."""
        # Sum all the fitness values.
        total_fitness = sum(rocket.fitness for rocket in self.population)
        # Divide by the total to normalize the fitness values.
        for rocket in self.population:
            rocket.fitness /= total_fitness

    def reproduction(self) -> None:
        new_population = []  # Separate the array for the next generation.

        for _ in range(len(self.population)):
            # Now use the weighted selection algorithm.
            parent_a = self.weighted_selection()
            parent_b = self.weighted_selection()
            child = parent_a.crossover(parent_b)
            child.mutate(self.mutation_rate)
            # Rocket goes in the new population.
            new_population.append(Rocket(self.x, self.y, child))

        # Now the new population is the current one.
        self.population = new_population
        self.generations += 1

    def weighted_selection(self) -> Rocket:
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
