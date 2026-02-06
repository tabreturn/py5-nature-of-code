# https://natureofcode.com/particles/#example-49-additive-blending


def setup():
    global img
    img = load_image('texture.png')  # Load the PNG.


def show():
    image_mode(CENTER)
    # Note that tint() is the image equivalent of a shape's fill().
    tint(255, self.lifespan)
    image(img, self.position.x, self.position.y)


def draw():
    # Use additive blending.
    blend_mode(ADD)
    # Clear the previous frame since background() doesn't overwrite
    clear()
    # Additive glow needs a dark background.
    background(0)

    # The wind force direction is based on mouse_x.
    dx = remap(mouse_x, 0, width, -0.2, 0.2);
    wind = Py5Vector2D(dx, 0)

    emitter.apply_force(wind)
    emitter.run()

    # Add three particles per frame to layer the effect.
    for i in range(3):
        emitter.add_particle()

