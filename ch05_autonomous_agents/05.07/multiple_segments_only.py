# https://natureofcode.com/autonomous-agents/#example-58-path-following

from path_noc import PathNoc  # Class is named PathNoc (not Path).


def setup():
    global path
    size(640, 240)

    path = PathNoc()  # A path object (series of connected points).
    path.add_point(-20, height / 2)
    path.add_point(random(width / 2), random(height))
    path.add_point(random(width / 2, width), random(height))
    path.add_point(width + 20, height / 2)


def draw():
    background(255)
    path.show()  # Display the path.
