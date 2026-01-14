# https://natureofcode.com/genetic-algorithms/#making-improvements

from dna import DNA
from obstacle import Obstacle
from population import Population
from rocket import Rocket

MUTATION_RATE = 0.01     # Per-gene mutation probability.
POPULATION_SIZE = 50     # Number of individuals in the population.
LIFE_SPAN = 250          # How many frames does a generation live for?
life_counter = 0         # Keep track of the life span.
record_time = LIFE_SPAN  # Fastest time to target.


def setup():
    global monospace, obstacles, population, target
    size(640, 240)
    monospace = create_font('DejaVu Sans Mono', 32)
    target = Obstacle(width / 2 - 12, 24, 24, 24)
    # Step 1: Create the population.
    # Try different values for the mutation rate and population size.
    xy = (width / 2, height - 20)
    # The population.
    population = Population(MUTATION_RATE, POPULATION_SIZE, LIFE_SPAN, xy)
    # Create the obstacle course
    obstacles = [
      Obstacle(width / 2 - 75, height / 2, 150, 10)
    ]


def draw():
    global life_counter, target, record_time
    background(255)
    # The revised GA
    if life_counter < LIFE_SPAN:
        # Step 2: The rockets live lives until life_counter reaches LIFE_SPAN.
        population.live(obstacles, target)

        if population.target_reached() and life_counter < record_time:
            record_time = life_counter
        else:
            life_counter += 1
    else:
        # When LIFE_SPAN is reached, reset life_counter and evolve the next gen.
        # (steps 3 and 4, selection and reproduction).
        life_counter = 0
        population.fitness(target)
        population.selection()
        population.reproduction()

    # Draw the target position.
    target.show()

    # Draw the obstacles.
    for obstacle in obstacles:
        obstacle.show()

    # Display some info.
    fill(0)
    text_font(monospace)
    text_size(11)
    text(
      f'Generation #: {population.generations}\n'
      f'Cycles left: {LIFE_SPAN - life_counter}\n'
      f'Record cycles: {record_time}',
      10,
      20,
    )
    text('(C) pause\n(Z) advance frame\n(X) run continuous\n(Q) quit', 10, 187)


def mouse_pressed():
    """Move the target if the mouse is clicked. Rockets adapt to new target."""
    global target
    target.position.x = mouse_x
    target.position.y = mouse_y


def key_pressed():
    """Handle keyboard controls for stepping, looping, pausing, and quitting."""
    if key == "c": no_loop()
    if key == "z": redraw()
    if key == "x": loop()
    if key == "q": exit_sketch()
