# https://natureofcode.com/genetic-algorithms/#evolving-forces-smart-rockets

from dna import DNA
from population import Population
from rocket import Rocket

MUTATION_RATE = 0.01  # Per-gene mutation probability.
POPULATION_SIZE = 50  # Number of individuals in the population.
LIFE_SPAN = 250       # How many frames does a generation live for?
life_counter = 0      # Keep track of the life span.


def setup():
    global monospace, population, target
    size(640, 240)
    monospace = create_font('DejaVu Sans Mono', 32)
    target = Py5Vector2D(width / 2, 24)
    # Step 1: Create the population.
    # Try different values for the mutation rate and population size.
    xy = (width / 2, height + 20)
    # The population.
    population = Population(MUTATION_RATE, POPULATION_SIZE, LIFE_SPAN, xy)


def draw():
    global life_counter, target
    background(255)
    # The revised GA
    if life_counter < LIFE_SPAN:
        # Step 2: The rockets live lives until life_counter reaches LIFE_SPAN.
        population.live()
        life_counter += 1
    else:
        # When LIFE_SPAN is reached, reset life_counter and evolve the next gen.
        # (steps 3 and 4, selection and reproduction).
        life_counter = 0
        population.fitness(target)
        population.selection()
        population.reproduction()

    # Draw the target position.
    fill(127)
    stroke(0)
    stroke_weight(2)
    circle(target.x, target.y, 24)
    # Display some info.
    fill(0)
    text_font(monospace)
    text_size(11)
    text(
      f'Generation #: {population.generations}\n'
      f'Cycles left: {LIFE_SPAN - life_counter}',
      10,
      20,
    )
    text('(C) pause\n(Z) advance frame\n(X) run continuous\n(Q) quit', 10, 187)


def mouse_pressed():
    """Move the target if the mouse is clicked. Rockets adapt to new target."""
    global target
    target.x = mouse_x
    target.y = mouse_y


def key_pressed():
    """Handle keyboard controls for stepping, looping, pausing, and quitting."""
    if key == "c": no_loop()
    if key == "z": redraw()
    if key == "x": loop()
    if key == "q": exit_sketch()
