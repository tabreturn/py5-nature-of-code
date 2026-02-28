# https://natureofcode.com/physics-libraries/#a-force-directed-graph

from toxi.physics2d import VerletPhysics2D, VerletParticle2D, VerletSpring2D

from cluster_pl import Cluster


def setup():
    global physics, monospace, cluster
    size(640, 240)
    monospace = create_font('../../DejaVuSansMono.ttf', 32)

    # Create a Toxiclibs.js Verlet physics world.
    physics = VerletPhysics2D()

    # Create a random cluster.
    cluster = Cluster(physics, random_int(2, 20-1), random(10, height / 2))


def draw():
    global cluster

    # Must update the physics.
    physics.update()
    physics.setDrag(0.2)  # Some drag to avoid fast-spinning clusters.

    background(255)

#    if frame_count % 120 == 0:
#        cluster = Cluster(physics, random_int(2, 20-1), random(10, height / 2))

    # Display all points.
    if show_particles:
        cluster.show()  # Draw the particles.

    # If we want to see the physics.
    if show_physics:
        cluster.show_connections()

    # Display some info.
    fill(0); text_font(monospace); text_size(11)
    text('(C) connection toggle\n(P) particle toggle\n(N) new cluster', 10, 200)


# The function(s) below are for mouse/key interaction

show_particles, show_physics = True, True

def key_pressed():
    global cluster, show_particles, show_physics

    if key == 'c':
        show_physics = not show_physics
        show_particles |= not show_physics
    elif key == 'p':
        show_particles = not show_particles
        show_physics |= not show_particles
    elif key == 'n':
        physics.clear()
        cluster = Cluster(physics, random_int(2, 20), random(10, height / 2))
