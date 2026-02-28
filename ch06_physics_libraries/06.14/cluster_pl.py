# PY5 IMPORTED MODE CODE

from toxi.geom import *
from toxi.physics2d import *

from particle_pl import Particle


class Cluster:

    # Needs "physics" parameter because Python modules have isolated namespaces.
    # (p5.js sketches share a single global scope)
    def __init__(self, physics: VerletPhysics2D, n: int, length: float):
        # Physics will misbehave if all particles created in exact same position.
        self.particles = [
          Particle(
            physics, width / 2 + random(-1, 1), height / 2 + random(-1, 1), 4
          )
          for _ in range(n)
        ]

        # Use the variable particle_i to store the particle reference.
        for i, particle_i in enumerate(self.particles[:-1]):
            # Look at how j starts at i + 1.
            for particle_j in self.particles[i + 1:]:
                physics.addSpring(
                  # The spring connects particles i and j.
                  VerletSpring2D(particle_i._p, particle_j._p, length, 0.01)
                )

    def show(self) -> None:
        """Show all the nodes."""

        for n in self.particles:
            n.show()

    def show_connections(self) -> None:
        """Draw all the internal connections."""

        stroke(0, 127)
        stroke_weight(2)

        for i, pi in enumerate(self.particles[:-1]):
            for pj in self.particles[i + 1:]:
                line(pi.x, pi.y, pj.x, pj.y)
