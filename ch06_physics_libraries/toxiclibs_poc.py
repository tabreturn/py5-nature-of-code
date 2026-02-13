# https://natureofcode.com/physics-libraries/#verlet-physics-with-toxiclibsjs

"""
NOTE:
Examples 6.11 through 6.15 (end of chapter) use the Toxiclibs Java libraries.
For details on py5's integration with Processing (Java) libraries, see:
https://py5coding.org/how_tos/use_processing_libraries.html
"""

# The necessary geometry classes: vectors, rectangles.
from toxi.geom import Vec2D, Rect
# Import the important classes from toxi.physics2d.
from toxi.physics2d import VerletPhysics2D, VerletSpring2D, VerletParticle2D
# For the world's gravity.
from toxi.physics2d.behaviors import GravityBehavior2D


def setup():
    global particle, physics
    size(640, 240)

    physics = VerletPhysics2D()  # Create a Toxiclibs world.
    physics.setWorldBounds(Rect(0, 0, width, height))
    physics.addBehavior(GravityBehavior2D(Vec2D(0, 0.5)))

    particle = Particle(width / 2, height / 2, 8)
    physics.addParticle(particle.particle)


def draw():
    background(255)
    physics.update()  # This is the same as the Matter.js Engine.update().
    particle.show()


class Particle:
    """For py5, wrap Java VerletParticle2D rather than subclassing it."""

    def __init__(self, x: float, y: float, r: float) -> None:
        # A VerletParticle needs initial (x, y) position, but has no geometry ...
        self.particle = VerletParticle2D(x, y)
        # so the r is used only for drawing.
        self.r = r

    def show(self) -> None:
        fill(127)
        stroke(0)
        # When it comes time to draw particle, (x, y) is stored in self.particle.
        circle(self.particle.x(), self.particle.y(), self.r * 2)
