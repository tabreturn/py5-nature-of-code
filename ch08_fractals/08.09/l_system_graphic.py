# https://natureofcode.com/fractals/#example-89-an-l-system

from l_system import LSystem
from turtle import Turtle


def setup():
    global l_system, turtle
    size(640, 240)

    rules = {  # Rules can be defined as a Python dictionary.
      'F': 'FF+[+F-F-F]-[-F+F+F]'
    }
    l_system = LSystem('F', rules)   # L-system created with axiom and ruleset.
    turtle = Turtle(4, radians(25))  # The Turtle object has a length and angle.

# Some other rules:

#    rules = {
#      'F': 'F[F]-F+F[--F]+F-F'
#    }
#    l_system = LSystem('F-F-F-F', rules)
#    turtle = Turtle(4, PI / 2)

#    rules = {
#      'F': 'F--F--F--G',
#      'G': 'GG'
#    }
#    l_system = LSystem('F--F--F', rules)
#    turtle = Turtle(8, PI / 3)

    # Run the L-system through four generations.
    for _ in range(4):
        l_system.generate()


def draw():
    background(255);
    translate(width / 2, height)       # Start at the bottom of the canvas.
    turtle.render_(l_system.sentence)  # Ask turtle engine to render sentence.
    no_loop()
