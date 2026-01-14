# https://natureofcode.com/genetic-algorithms/#coding-the-genetic-algorithm

from dna import DNA

MUTATION_RATE = 0.01           # Per-gene mutation probability.
POPULATION_SIZE = 150          # Number of individuals in the population.
TARGET = 'to be or not to be'  # Target phrase to evolve toward.


def setup():
    global monospace, population
    size(640, 360)
    monospace = create_font('DejaVu Sans Mono', 32)

    # Step 1: Initialization.
    population = [DNA(len(TARGET)) for _ in range(POPULATION_SIZE)]


def draw():
    global population

    # Step 2a: Calculate fitness.
    for phrase in population:
        phrase.calculate_fitness(TARGET)

    display_progress()

    # Step 2b: Build the mating pool.
    mating_pool = []

    for phrase in population:
        # Add each member n times according to its fitness score.
        n = floor(phrase.fitness * 100)
        # Always include at least one entry so selection never fails.
        mating_pool.extend([phrase] * (n + 1))

    # Step 3: Reproduction.
    for i, _ in enumerate(population):
        parent_a = random_choice(mating_pool)
        parent_b = random_choice(mating_pool)

        child = parent_a.crossover(parent_b)  # Step 3a: Crossover.
        child.mutate(MUTATION_RATE)  # Step 3b: Mutation.

        """You overwrite the population with the new children. On the next call
        to draw(), the same steps run again on this new generation."""
        population[i] = child

        # Step 4: Repetition. Go back to the beginning of draw()!


def display_progress():
    """Display the current best phrase and summary statistics."""
    background(255)
    fill(0)
    text_font(monospace)

    best = ''.join(max(population, key=lambda phrase: phrase.fitness).genes)
    text_size(12)
    text('Best phrase:', 10, 32)
    text_size(24)
    text(best, 10, 64)

    avgfitness = sum(phrase.fitness for phrase in population) / len(population)
    statstext = (
      f'total generations:     {frame_count}\n'
      f'average fitness:       {avgfitness:.2f}\n'
      f'total population:      {POPULATION_SIZE}\n'
      f'mutation rate:         {floor(MUTATION_RATE * 100)}%'
    )
    text_size(12)
    text(statstext, 10, 96)

    phrasestext = '| ' + '| '.join(
      ''.join(population[i].genes) + ('\n' if i % 3 == 2 else ' ')
      for i in range(min(len(population), 99))
    )
    text_size(8)
    text(phrasestext, width / 2, 24)

    text_size(10)
    text('(C) pause\n(Z) advance frame\n(X) run continuous\n(Q) quit', 10, 300)

    if best == TARGET:  # Stop when the target phrase is reached.
        no_loop()


def key_pressed():
    """Handle keyboard controls for stepping, looping, pausing, and quitting."""
    if key == 'c': no_loop()
    if key == 'z': redraw()
    if key == 'x': loop()
    if key == 'q': exit_sketch()
