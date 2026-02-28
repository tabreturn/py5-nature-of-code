# PY5 IMPORTED MODE CODE

from toxi.geom import *
from toxi.physics2d import *

from toxi.physics2d.behaviors import AttractionBehavior2D


# How cute is this simple Particle class?!
class Particle:
    """For py5, wrap Java VerletParticle2D as **py5 cannot subclass it**."""

    # Needs "physics" parameter because Python modules have isolated namespaces.
    # (p5.js sketches share a single global scope)
    def __init__(self, physics: VerletPhysics2D, x: float, y: float, r: float):
        # A VerletParticle needs initial (x, y) position, but has no geometry ...
        self.p = VerletParticle2D(x, y)  # (Python wrapper forwards to this)
        # ... so the r is used only for drawing.
        self.r = r

        # Every time a Particle is made, an AttractionBehavior is generated. 
        physics.addBehavior(AttractionBehavior2D(self.p, r * 2, -2))
        # (Note that when the strength is negative, it's a repulsive force!)

        # Add the object to the global physics world.
        physics.addParticle(self.p)  # Inside class, reference is self.p.

    def show(self) -> None:
        fill(127)
        stroke(0)
        circle(self.x, self.y, self.r * 2)


# The code below is necessary to provide a more p5.js-like Toxiclibs workflow.

    # Provide JS-style fields and forward the relevant physics verbs;
    # else Python would just create wrapper attributes and nothing would move.
    @property
    def x(self) -> float: return float(self.p.x())
    @x.setter
    def x(self, v: float): self.p.set(float(v), self.y)
    @property
    def y(self) -> float: return float(self.p.y())
    @y.setter
    def y(self, v: float): self.p.set(self.x, float(v))
    lock   = lambda self: self.p.lock()
    unlock = lambda self: self.p.unlock()
