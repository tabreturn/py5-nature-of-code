# https://natureofcode.com/particles/#example-48-an-image-texture-particle-system

from emitter import Emitter


def setup():
    global emitter, img
    size(640, 240)
    img = load_image('texture.png')  # Load the PNG.
    emitter = Emitter(width / 2, height - 75)


def draw():
    background(0)

    # The wind force direction is based on mouse_x.
    dx = remap(mouse_x, 0, width, -0.2, 0.2)
    wind = Py5Vector2D(dx, 0)

    emitter.apply_force(wind)
    emitter.run()
    emitter.add_particle(img)

    # Draw an arrow representing the wind force.
    draw_vector(wind, Py5Vector2D(width / 2, 50), 500)


def draw_vector(v: Py5Vector2D, pos: Py5Vector2D, scayl: int) -> None:
    arrow_size = 4
    stroke(255)
    length = v.x * scayl
    sign = 1 if length >= 0 else -1
    arrow_x = pos.x + length
    line(pos.x, pos.y, arrow_x, pos.y)
    line(arrow_x, pos.y, arrow_x - arrow_size * sign, pos.y + arrow_size / 2)
    line(arrow_x, pos.y, arrow_x - arrow_size * sign, pos.y - arrow_size / 2)
