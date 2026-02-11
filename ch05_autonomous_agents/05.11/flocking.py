# https://natureofcode.com/autonomous-agents/#flocking

from boid import Boid
from flock import Flock


def setup():
    global monospace, flock  # A Flock object manages the entire group.
    size(640, 240)
    monospace = create_font('../../DejaVuSansMono.ttf', 32)

    flock = Flock()
    # The flock starts out with 120 (÷3) boids.
    for _ in range(120 // 3):
        boid = Boid(width / 2, height / 2, 3.0, 0.05)
        flock.add_boid(boid)
        boid.velocity = Py5Vector2D(random(-1, 1), random(-1, 1))
        boid.r = 3.0


def draw():
    background(255)
    flock.run()

    # Display some info.
    text_align(LEFT); text_font(monospace); text_size(11); fill(0)
    text(f'FPS: {int(get_frame_rate())}', 10, 226)
