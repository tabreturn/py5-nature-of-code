# https://natureofcode.com/genetic-algorithms/#interactive-selection

from population import Population
from rectangle import Rectangle

POPULATION_SIZE = 8  # This is a very small population!
# Pretty high mutation. Our population is small; we need to enforce variety.
MUTATION_RATE = 0.05


def setup():
    global button, monospace, population
    size(640, 240)
    monospace = create_font('DejaVu Sans Mono', 32)
    color_mode(RGB, 1)
    # Create the population.
    population = Population(MUTATION_RATE, POPULATION_SIZE)
    # Define a p5.js-'like' button.
    button = Rectangle(10, 10, 150, 20)


def mouse_pressed():
    # Listen for the p5.js-'like' button.
    if button.contains(mouse_x, mouse_y):
        next_generation()


def draw():
    background(1)
    # Render the p5.js-'like' button.
    text_font(monospace); text_align(CENTER, CENTER); text_size(11); fill(0)
    text('evolve new generation', *button.center)
    no_fill(); rect(button.x, button.y, button.width, button.height)

    # Draw the flowers.
    population.show()
    # Check for increasing fitness.
    population.rollover(mouse_x, mouse_y)
    text_align(LEFT)
    text(f'Generation {population.generations}', 12, height - 10)


def next_generation():
    """If the button is pressed, evolve the next generation."""
    population.selection()
    population.reproduction()
