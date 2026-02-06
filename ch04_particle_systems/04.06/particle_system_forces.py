# https://natureofcode.com/particles/#particle-systems-with-forces

from emitter import Emitter


def setup():
    global emitter
    size(640, 240)
    emitter = Emitter(width / 2, 50)


def draw():
    # Note that py5 does not support transparency alpha with background().
    fill(255, 25); rect(0, 0, width, height)

    # Create a hardcoded vector and apply it as a force.
    GRAVITY = Py5Vector2D(0, 0.1)
    # Apply a force to the emitter.
    emitter.apply_force(GRAVITY)

    emitter.add_particle()
    emitter.run()
