# https://natureofcode.com/particles/#inheritance-and-polymorphism

from emitter import Emitter


def setup():
    global emitter
    size(640, 240)
    emitter = Emitter(width / 2, 50)


def draw():
    background(255)
    emitter.add_particle()
    emitter.run()
