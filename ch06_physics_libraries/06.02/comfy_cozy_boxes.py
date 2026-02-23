# https://natureofcode.com/physics-libraries/#matterjs-with-p5js

from box_ import Box

boxes: list[Box] = []  # A list to store all Box objects.


def setup():
    size(640, 240)


def draw():
    background(255)

    # When the mouse is clicked, add a new Box object.
    if is_mouse_pressed:
        box_ = Box(mouse_x, mouse_y)
        boxes.append(box_)

    # Display all the Box objects.
    for box_ in boxes:
        box_.show()
