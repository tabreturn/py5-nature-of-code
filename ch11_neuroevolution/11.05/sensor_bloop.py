# https://natureofcode.com/neuroevolution/#sensing-the-environment

from creature import Creature
from food import Food


def setup():
    global bloop, food
    size(640, 240)

    # One bloop, one piece of food.
    bloop = Creature()
    food = Food()

    # Overwrite food attributes to match p5.js example.
    food.position = Py5Vector2D(width / 2, height / 2)
    food.r = 32


def draw():
    background(255)

    # Temporarily control the bloop with the mouse.
    bloop.position.x, bloop.position.y = mouse_x, mouse_y

    # Draw the food and the bloop.
    food.show()
    bloop.show()

    # The bloop senses the food.
    bloop.sense(food)
