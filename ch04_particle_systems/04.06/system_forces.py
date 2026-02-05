# https://natureofcode.com/particles/#particle-systems-with-forces

from emitter import Emitter


def setup():
    global emitter
    size(640, 240)
    emitter = Emitter(width / 2, 20)


def draw():
    # Note that py5 does not support transparency alpha with background().
    fill(255, 30); rect(0, 0, width, height)

    # Apply a force to all particles.
    GRAVITY = Py5Vector2D(0, 0.1)
    # Apply a force to the emitter.
    emitter.apply_force(GRAVITY)

    emitter.add_particle()
    emitter.run()
    
