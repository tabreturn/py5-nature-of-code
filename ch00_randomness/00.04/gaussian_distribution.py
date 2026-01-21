# https://natureofcode.com/random/#a-normal-distribution-of-random-numbers


def setup():
    size(640, 240)
    background(255)


def draw():
    # A normal distribution with mean 320 and standard deviation 60.
    x = random_gaussian(320, 60)  # same as: 60 * randomGaussian() + 320
    no_stroke()
    fill(0, 10)
    circle(x, 120, 16)
