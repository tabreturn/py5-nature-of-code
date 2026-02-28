# PY5 IMPORTED MODE CODE

from toxi.geom import *
from toxi.physics2d import *


class Spring:
    """Wrapper for Java VerletSpring2D (py5 can't subclass Java classes)."""

    # Needs "physics" parameter because Python modules have isolated namespaces.
    # (p5.js sketches share a single global scope)
    def __init__(self, physics: VerletPhysics2D, a: 'Particle', b: 'Particle'):
        # Calculate the rest length as the distance between the particles.
        length = dist(a.x, a.y, b.x, b.y)
        # Hardcode the spring strength.
        self._s = VerletSpring2D(a._p, b._p, length, 0.01)
        # Another enhancement to have object add itself to the physics world!
        physics.addSpring(self._s)  # Inside class, reference is self._s.

    def show(self) -> None:
        stroke(0)
        line(self._s.a.x(), self._s.a.y(), self._s.b.x(), self._s.b.y())
