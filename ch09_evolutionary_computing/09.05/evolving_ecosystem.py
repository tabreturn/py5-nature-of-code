# https://natureofcode.com/genetic-algorithms/#ecosystem-simulation

from world import World


def setup():
    global world
    size(640, 240)
    # The world starts with 20 bloops and 20 pieces of food.
    world = World(20)


def draw():
    background(255)
    world.run()

# We can add a creature manually if we so desire.

def mouse_pressed():
    world.born(mouse_x, mouse_y)


def mouse_dragged():
    world.born(mouse_x, mouse_y)