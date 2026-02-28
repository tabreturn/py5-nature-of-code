# PY5 IMPORTED MODE CODE

from toxi.geom import *
from toxi.physics2d import *

from toxi.physics2d.behaviors import AttractionBehavior2D


class Attractor:
    """Wrapper for Java VerletSpring2D (py5 can't subclass Java classes)."""

    # Needs "physics" parameter because Python modules have isolated namespaces.
    # (p5.js sketches share a single global scope)
    def __init__(self, physics: VerletPhysics2D, x: float, y: float, r: float):
        self.p = VerletParticle2D(x, y)
        self.r = r

        # Attract all particles always.
        distance = width
        strength = 0.1
        behavior = AttractionBehavior2D(self.p, distance, strength)
        physics.addBehavior(behavior)
        # Repel particles that come within its radius.
        physics.addBehavior(AttractionBehavior2D(self.p, self.r + 4, -5))
        # A nice improvement where the attractor adds itself to the physics.
        physics.addParticle(self.p)

    def show(self) -> None:
        fill(0)
        circle(self.p.x(), self.p.y(), self.r * 2)
