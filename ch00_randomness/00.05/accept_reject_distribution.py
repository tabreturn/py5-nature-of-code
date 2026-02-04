# https://natureofcode.com/random/#a-custom-distribution-of-random-numbers

TOTAL = 20  # The total number of counts.


def setup():
    global random_counts
    size(640, 240)

    # A list to keep track of how often random numbers are picked.
    random_counts = [0] * TOTAL


def draw():
    global random_counts
    background(255)

    # Pick a random number and increase the count.
#    index = floor(random(len(random_counts)))
    index = int(accept_reject() * len(random_counts))
    random_counts[index] += 1

    stroke(0)
    stroke_weight(2)
    fill(127)
    w = width / len(random_counts)

    # Graph the results.
    for x, count in enumerate(random_counts):
        rect(x * w, height - count, w - 1, count)


def accept_reject() -> float:
    # Do this "forever" until you find a qualifying random value.
    while True:
        r1 = random()     # Pick a random value.
        probability = r1  # Assign a probability.
        r2 = random()     # Pick a second random value.
        # Does it qualify? If so, you're done!
        if r2 < probability:
            return r1

