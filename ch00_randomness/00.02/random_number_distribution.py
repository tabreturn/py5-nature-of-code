# https://natureofcode.com/random/#example-02-a-random-number-distribution

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
    index = random_int(len(random_counts)-1)
    random_counts[index] += 1

    stroke(0)
    stroke_weight(2)
    fill(127)
    w = width / len(random_counts)

    # Graph the results.
    for x, count in enumerate(random_counts):
        rect(x * w, height - count, w - 1, count)

