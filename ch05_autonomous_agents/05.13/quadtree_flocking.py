# https://natureofcode.com/autonomous-agents/#example-513-quadtree

"""
NOTE:
Although this simulation runs much slower than the p5.js version, it *may*
demonstrate an improvement over 05.12 (flocking_bin_lattice) when boids are
highly clustered, large regions are empty, and overall occupancy is sparse.
"""

from boid import Boid
from flock import Flock
from quadtree_noc import QuadTree, Rectangle, Point

QT_CAPACITY = 4  # Bucket size: points per node before split (4-8 is common).


def setup():
    global flock, monospace
    size(640, 240)
    monospace = create_font('../../DejaVuSansMono.ttf', 32)

    flock = Flock()
    # The flock starts out with 120 (÷3) boids.
    for _ in range(120 // 3):
        boid = Boid(random(width), random(height), 3, 0.05)
        boid.r = 3.0
        boid.velocity = random(-1, 1), random(-1, 1)
        flock.add_boid(boid)


def draw():
    background(255)

    # Build a quadtree from the current boid positions.
    boundary = Rectangle(width / 2, height / 2, width / 2, height / 2)
    qtree = QuadTree(boundary, QT_CAPACITY)
    # Insert each boid into the quadtree (store position + Boid reference).
    for b in flock.boids:
        qtree.insert(Point(b.position.x, b.position.y, b))

    # Draw the grid.
    qtree.show()

    # Create a 100×100 query box centered on the mouse.
    rect_mode(CENTER)
    range_ = Rectangle(mouse_x, mouse_y, 50, 50)

    # This check mirrors the Coding Train fix (avoid weirdness outside canvas).
    if mouse_x < width and mouse_y < height:
        stroke_weight(2)
        stroke(255, 50, 50)
        fill(255, 50, 50, 50)
        rect(range_.x, range_.y, range_.w * 2, range_.h * 2)

    flock.run_qtree(qtree)

    # Display some info.
    text_align(LEFT); text_font(monospace); text_size(11); fill(0)
    text(f'FPS: {int(get_frame_rate())}', 10, 226)
