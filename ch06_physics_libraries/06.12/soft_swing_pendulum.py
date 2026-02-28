# https://natureofcode.com/physics-libraries/#a-string

# The necessary geometry classes: vectors, rectangles.
from toxi.geom import Vec2D, Rect
# Import the important classes from toxi.physics2d.
from toxi.physics2d import VerletPhysics2D, VerletParticle2D, VerletSpring2D
# For the world's gravity.
from toxi.physics2d.behaviors import GravityBehavior2D

particles: list['Particle'] = []
SPACING = 10
TOTAL = 20


def setup():
    global physics, particles
    size(640, 240)

    # Create a Toxiclibs.js Verlet physics world.
    physics = VerletPhysics2D()
    physics.setWorldBounds(Rect(0, 0, width, height))
    physics.addBehavior(GravityBehavior2D(Vec2D(0, 0.5)))

    for i in range(TOTAL):
        # Space them out along the x-axis.
        particle = Particle(width / 2 + i * SPACING, 0, 16)
        # Add the particle to the physics world.
        physics.addParticle(particle._p)  # (Underlying Java object via ._p)
        # Add the particle to the array.
        particles.append(particle)

    for i in range(TOTAL - 1):  # Loop stops before last element (TOTAL – 1).
        # The spring connects particle i to i + 1.
        spring = VerletSpring2D(
          particles[i]._p,
          particles[i + 1]._p,
          SPACING, 0.2
        )
        physics.addSpring(spring)  # The spring must also be added to the world.

    particles[0].lock()


def draw():
    # Must update the physics.
    physics.update()

    background(255)

    stroke(0)
    no_fill()

    begin_shape()
    for particle in particles:
        # Each particle represents one vertex in the string.
        vertex(particle.x, particle.y)
    end_shape()

    # This draws the last particle as a circle.
    particles[-1].show()

    # Move the particle according to the mouse.
    if is_mouse_pressed:
        # First lock the particle, then set the x and y, then unlock() it.
        particles[-1].lock()
        particles[-1].x = mouse_x
        particles[-1].y = mouse_y
        particles[-1].unlock()


# How cute is this simple Particle class?!
class Particle:
    """For py5, wrap Java VerletParticle2D as **py5 cannot subclass it**."""

    def __init__(self, x: float, y: float, r: float):
        # A VerletParticle needs initial (x, y) position, but has no geometry ...
        self._p = VerletParticle2D(x, y)  # (Python wrapper forwards to this)
        # ... so the r is used only for drawing.
        self.r = r

    def show(self) -> None:
        fill(127)
        stroke(0)
        circle(self.x, self.y, self.r * 2)


# The code below is necessary to provide a more p5.js-like Toxiclibs workflow.

    # Provide JS-style fields and forward the relevant physics verbs;
    # else Python would just create wrapper attributes and nothing would move.
    @property
    def x(self) -> float: return float(self._p.x())
    @x.setter
    def x(self, v: float): self._p.set(float(v), self.y)
    @property
    def y(self) -> float: return float(self._p.y())
    @y.setter
    def y(self, v: float): self._p.set(self.x, float(v))
    lock   = lambda self: self._p.lock()
    unlock = lambda self: self._p.unlock()
