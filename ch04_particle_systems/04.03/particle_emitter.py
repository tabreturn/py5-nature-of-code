# https://natureofcode.com/particles/#a-particle-emitter

from emitter import Emitter


def setup():
    global emitter
    size(640, 240)
    emitter = Emitter(width / 2, 50)  # Just one particle emitter!


def draw():
    background(255)
    emitter.add_particle()
    emitter.run()
