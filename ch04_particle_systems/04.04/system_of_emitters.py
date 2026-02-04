# https://natureofcode.com/particles/#a-system-of-emitters

from emitter import Emitter

emitters = []  # This time, what you're putting in the list is an emitter itself!


def setup():
    global monospace
    size(640, 240)
    monospace = create_font('../../DejaVuSansMono.ttf', 32)


def draw():
    background(255)

    # No emitters are removed, so a for...in loop can work here!
    for emitter in emitters:
        emitter.add_particle()
        emitter.run()

    # Display some info.
    fill(0); text_font(monospace); text_size(11)
    text('click to add particle systems', 10, 226)


def mouse_pressed():
    global emitters
    emitters.append(Emitter(mouse_x, mouse_y))
