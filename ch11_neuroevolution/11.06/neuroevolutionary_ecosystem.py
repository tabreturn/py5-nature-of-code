# https://natureofcode.com/neuroevolution/#learning-from-the-sensors

from creature import Creature
from food import Food

time_slider_value = 10  # A variable to hold the slider value.


def setup():
    global bloops, food
    size(640, 240)

    # Many bloops, many pieces of food.
    bloops = [Creature(random(width), random(height)) for _ in range(20)]
    food = [Food() for _ in range(8)]


def draw():
    background(255)

    for _ in range(time_slider_value):
        # Draw the food and the bloop(s).
        for i in range(len(bloops) - 1, -1, -1):
            bloops[i].think(food)
            bloops[i].eat(food)
            bloops[i].update()
            bloops[i].borders()

            if bloops[i].health < 0:
                bloops.pop(i)
            elif random() < 0.001:
                child = bloops[i].reproduce()
                bloops.append(child)

    for treat in food:
        treat.show()

    # Bloop(s) sensing the food.
    for bloop in bloops:
        bloop.show()

    # Display a slider with a min and max range, and a starting value.
    display_slider(1, 20, 1)


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
