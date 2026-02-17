# https://natureofcode.com/neuroevolution/#responding-to-change

"""
NOTE:
This version often learns than the original p5.js/ml5 example.
That's mostly because the rocket 'brain' outputs are interpreted in a more
direct and stable way. No need to worry about the details -- it still feels
like working with ml5, just with 'creatures' that tend to act a bit smarter.
"""

#from dna import DNA
#from obstacle import Obstacle
from population import Population
from rocket import Rocket as Creature  # 'Creatures' are actually rockets.
from glow import Glow

MUTATION_RATE = 0.01    # Per-gene mutation probability.
POPULATION_SIZE = 50    # Number of individuals in the population.
LIFESPAN = 250          # How many frames does a generation live for?
life_counter = 0        # Keep track of the life span.
record_time = LIFESPAN  # Fastest time to target.

time_slider_value = 10  # A variable to hold the slider value.
life_counter = 0
generations = 0


def setup():
    global monospace, creatures, glow, population
    size(640, 240)
    monospace = create_font('../../DejaVuSansMono.ttf', 32)

    # Use Population to manage creatures.
    creatures = Population(
      MUTATION_RATE, POPULATION_SIZE, LIFESPAN, (width / 2, height / 2)
    )
    for r in creatures.population:
        r.position = Py5Vector2D(random(width), random(height))

    glow = Glow()


def draw():
    global life_counter

    # The drawing code happens just once!
    background(255)
    glow.show()
    for creature in creatures.population:
        creature.show()

    # Display a slider with a min and max range, and a starting value.
    display_slider(1, 20, 1)

    # The simulation code runs multiple times according to the slider.
    for i in range(time_slider_value):
        for creature in creatures.population:
            creature.seek(glow)
            creature.update(glow)
        glow.update()
        life_counter += 1

    if life_counter > LIFESPAN:
        # Use existing Population methods (instead of deigning new functions).
        creatures.selection()     # handles: normalizeFitness()
        creatures.reproduction()  # handles: reproduction() + generations++
        # Randomize positions here (so creatures don't spawn at center).
        for r in creatures.population:
            r.position = Py5Vector2D(random(width), random(height))
        life_counter = 0  # Restart 'timer'; prevents continuous reproduction.

    # Display some info.
    fill(0); text_font(monospace); text_size(11)
    text(
      f'Generation #: {creatures.generations}\n'
      f'Cycles left: {LIFESPAN - life_counter}\n',
      10, 20,
    )


# The function(s) below are for mouse/key interaction

_slider_inited = False

def display_slider(lo: int, hi: int, start: int) -> None:
    global time_slider_value, _slider_inited

    if not _slider_inited:
        time_slider_value = start; _slider_inited = True

    x, y, w, r = 10, 226, 160, 7
    stroke(0); stroke_weight(1)
    k = x + (time_slider_value - lo) / (hi - lo) * w
    line(x, y, x + w, y); fill(255); circle(k, y, r * 2)

    if is_mouse_pressed and abs(mouse_y - y) < 10:
        time_slider_value = int(
          lo + (constrain(mouse_x, x, x + w) - x) / w * (hi - lo)
        )

