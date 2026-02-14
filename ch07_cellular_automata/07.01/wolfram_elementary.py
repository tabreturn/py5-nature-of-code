# https://natureofcode.com/cellular-automata/#drawing-an-elementary-ca

W = 10  # Cell size
ruleset = [0, 1, 0, 1, 1, 0, 1, 0]  # Rule 90


def setup():
    global cells, generation
    size(640, 240)
    generation = 0  # Start at generation 0.
    background(255)

    # A list of 0s and 1s.
    cells = [0] * (width // W)
    cells[floor(len(cells) / 2)] = 1


def draw():
    global cells, generation

    for i in range(1, len(cells) - 1):
        if cells[i] == 1:  # Draw only the cells with a state of 1.
            fill(0)
            # Set the y-position according to the generation.
            square(i * W, generation * W, W)

    # Compute the next generation.
    nextgen = cells[:]
    for i in range(1, len(cells) - 1):
        left = cells[i - 1]
        me = cells[i]
        right = cells[i + 1]
        nextgen[i] = rules(left, me, right)

    cells = nextgen
    generation += 1  # The next generation.

    # Stopping when it gets to the bottom of the canvas.
    if generation * W > height:
        no_loop()


def rules(a: int, b: int, c: int) -> int:
    """Look up a new state from the ruleset."""

    s = f"{a}{b}{c}"
    index = int(s, 2)
    return ruleset[7 - index]
