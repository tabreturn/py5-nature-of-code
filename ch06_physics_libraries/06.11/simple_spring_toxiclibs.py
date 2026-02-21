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
    global physics, particle_1, particle_2
    size(640, 240)

    physics = VerletPhysics2D()  # Create a Toxiclibs world.
    physics.setWorldBounds(Rect(0, 0, width, height))
    physics.addBehavior(GravityBehavior2D(Vec2D(0, 0.5)))

    length = 120  # What is the rest length of the spring?

    # Create two particles.
    particle_1 = Particle(width / 2, 0, 8)
    particle_2 = Particle(width / 2 + length, 0, 8)
    particle_1.lock()  # Lock particle 1 in place.

    # Must add particles to the world.
    physics.addParticle(particle_1.p)
    physics.addParticle(particle_2.p)
    # (Particle is a Python wrapper, so pass its underlying Java object via .p)

    # Create one spring.
    spring = VerletSpring2D(particle_1.p, particle_2.p, length, 0.01)
    physics.addSpring(spring)


def draw():
    # Must update the physics.
    physics.update()  # This is the same as the Matter.js Engine.update().

    background(255)

    # Draw everything.
    stroke(0)
    line(particle_1.x, particle_1.y, particle_2.x, particle_2.y)
    particle_1.show()
    particle_2.show()

    # Move the particle according to the mouse.
    if is_mouse_pressed:
        particle_2.lock()
        particle_2.x = mouse_x
        particle_2.y = mouse_y
        particle_2.unlock()


# How cute is this simple Particle class?!
class Particle():
    """For py5, wrap Java VerletParticle2D as py5 cannot subclass it."""

    def __init__(self, x: float, y: float, r: float) -> None:
        # A VerletParticle needs initial (x, y) position, but has no geometry ...
        self.p = VerletParticle2D(x, y)  # Python wrapper forwards to this.
        # so the r is used only for drawing.
        self.r = r

    def show(self) -> None:
        fill(127)
        stroke(0)
        # When it comes time to draw particle, (x, y) is stored in self.particle.
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
