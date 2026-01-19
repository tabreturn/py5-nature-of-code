# https://natureofcode.com/neuroevolution/#reinforcement-learning

from bird import Bird
from pipe import Pipe

# ml5.js-style neuro-evolution functionality implemented with bespoke class.
from brain_ne import Brain

POPULATION_SIZE = 200  # Population size.


def setup():
    global birds, pipes
    size(640, 240)
    # Create the bird population.
    birds = [Bird() for _ in range(POPULATION_SIZE)]  # Array of birds.
    pipes = [Pipe()]
    
    # brain_pe.py runs on NumPy (i.e. on CPU by default)
    # ml5.setBackend('cpu');


def draw():
    global birds, pipes

    background(255)

    # Handle all the pipes.
    for pipe in reversed(pipes):
        pipe.show()
        pipe.update()

#        if pipe.collides(bird):
#           text('OOPS!', pipe.x, pipe.top + 20)

        if pipe.offscreen():
            pipes.remove(pipe)

    for bird in birds:  # There's now an array of birds!
        # Operate only on the birds that are still alive.
        if bird.alive:
            # This is the new method for the bird to decide to flap or not.
            bird.think(pipes)  # Make a decision based on the pipes.
            # Update and show the bird.
            bird.update()
            bird.show()
            # Has the bird hit a pipe? If so, it's no longer alive.
            for pipe in pipes:
                if pipe.collides(bird):
                    bird.alive = False

    # Add a new pipe every 100 frames.
    if frame_count % 100 == 0:
        pipes.append(Pipe())

    # Create the next generation when all the birds have died.
    if all_birds_dead():
        normalize_fitness()
        reproduction()
        reset_pipes()


def weighted_selection() -> Brain:
    """See Chapter 9 for a detailed explanation of this algorithm."""
    index = 0
    start = random()

    while start > 0:
        start -= birds[index].fitness
        index += 1

    index -= 1
    # Instead of returning the entire Bird object, just the brain is returned.
    return birds[index].brain


def normalize_fitness() -> None:
    # Sum the total fitness of all birds.
    fitness_sum = sum(bird.fitness for bird in birds)
    # Divide each bird's fitness by the sum.
    for bird in birds:
        bird.fitness /= fitness_sum


def reproduction() -> list[Bird]:
    global birds
    next_birds = []  # Start with a new empty array.

    for _ in range(POPULATION_SIZE):
        # Pick two parents.
        parent_a = weighted_selection()
        parent_b = weighted_selection()
        # Create a child with crossover.
        child = parent_a.crossover(parent_b)
        # Apply mutation.
        child.mutate(0.01)
        # Create the new bird object.
        next_birds.append(Bird(child))

    # The next generation is now the current one!
    birds = next_birds


def all_birds_dead() -> bool:
    for bird in birds:
        # If a single bird is alive, they are not all dead!
        if bird.alive:
            return False
    # If the loop completes without finding a living bird, all birds are dead.
    return True


def reset_pipes() -> None:
    """Remove all the pipes but the very latest one."""
    del pipes[:-1]