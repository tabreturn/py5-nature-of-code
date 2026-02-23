# https://natureofcode.com/physics-libraries/#matterjs-with-p5js

# Note Matter.js uses 'aliases'; for py5 just import Pymunk symbols directly.
from pymunk import Space
from box_pymunk import Box

DT = 1 / 60  # Fixed timestep (equivalent to Matter.Runner internal delta time).
# Scale factors to approximate Matter.js units in Pymunk.
SCALE_GRAVITY = 900.0

boxes: list[Box] = []  # A list to store all Box objects.


def setup():
    global engine  # The engine is now a global variable!
    size(640, 240)
    engine = Space()  # Create the engine; Pymunk's "world/engine" is a Space.
    # Change the engine's gravity to point downward.
    engine.gravity = (0, SCALE_GRAVITY)

def draw():
    background(255)

    engine.step(DT)  # Step the engine forward in time!

    # When the mouse is clicked, add a new Box object.
    if is_mouse_pressed:
        box_ = Box(engine, mouse_x, mouse_y)
        boxes.append(box_)

    # Iterate over a copy to remove boxes safely (instead of backwards).
    for box_ in boxes[:]:
        # Display all the Box objects.
        box_.show()
        # Remove the Body(+shape) from the world and the list.
        if box_.check_edge():
            box_.remove_body()
            boxes.remove(box_)
