# https://natureofcode.com/autonomous-agents/#example-513-quadtree

from quadtree_noc import *

QT_CAPACITY = 8  # # Bucket size: points per node before split (4-8 is common).


def setup():
    global qtree
    size(640, 240)

    boundary = Rectangle(width / 2, height / 2, width, height)
    qtree = QuadTree(boundary, QT_CAPACITY)

    for _ in range(2000):
        x = random_gaussian(width / 2, width / 8)
        y = random_gaussian(height / 2, height / 8)
        qtree.insert(Point(x, y))


def draw():
    background(255)

    # draw quadtree + points
    qtree.show()

    # faint “all points” layer
    stroke(0, 40)
    stroke_weight(2)
    for p in qtree.query(qtree.boundary) or []:
        point(p.x, p.y)

    # Create a 100×100 query box centered on the mouse.
    rect_mode(CENTER)
    range_ = Rectangle(mouse_x, mouse_y, 50, 50)

    # This check mirrors the Coding Train fix (avoid weirdness outside canvas).
    if mouse_x < width and mouse_y < height:
        stroke_weight(2)
        stroke(255, 50, 50)
        fill(255, 50, 50, 50)
        rect(range_.x, range_.y, range_.w * 2, range_.h * 2)

        for p in qtree.query(range_):  # Iterate points.
            point(p.x, p.y)
