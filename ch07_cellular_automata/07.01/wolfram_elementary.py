# https://natureofcode.com/cellular-automata/#elementary-cellular-automata

W = 10  # Cell size.
ruleset = [0, 1, 0, 1, 1, 0, 1, 0]  # Rule 90.


def setup():
    global cells, generation
    size(640, 240)

    generation = 0  # Start at generation 0.
    background(255)

    # A list of 0s and 1s.
    cells = [0] * (width // W)  # All cells start with state 0 ...
    cells[len(cells) // 2] = 1  # ... except the center cell is set to state 1.


def draw():
    global cells, generation

    for i in range(1, len(cells) - 1):
        # Create a fill based on its state (0 or 1).
        if cells[i] == 1:  # Draw only the cells with a state of 1.
            fill(0)
            # Set the y-position according to the generation.
            square(i * W, generation * W, W)  # X-position = index × cell width.

    # Compute the next generation.
    next_gen = cells[:]  # Create new list to store states for next generation.
    for i in range(1, len(cells) - 1):  # Loop that ignores first & last cells.
        # Look at the states (neighborhood) in the current list.
        left   = cells[i - 1]
        me     = cells[i]
        right  = cells[i + 1]
        # Look up the new value according to the rules.
        next_gen[i] = rules(left, me, right)  # Save new state in the new list.

    cells = next_gen  # The new generation becomes the current generation.
    generation += 1  # The next generation.

    # Stopping when it gets to the bottom of the canvas.
    if generation * W > height:
        no_loop()


# Look up a new state from the ruleset.
def rules(a: int, b: int, c: int) -> int:
    """Function signature: receives 3 values and returns 1."""

    s = f'{a}{b}{c}'  # A quick way to concatenate three numbers into a string.
    index = int(s, 2)  # Second argument (2) indicates parse as binary (base 2).
    return ruleset[7 - index]  # Invert index so 0 becomes 7, 1 becomes 6, ...
