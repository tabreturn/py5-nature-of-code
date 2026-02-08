# https://natureofcode.com/autonomous-agents/#example-55-creating-a-path-object

from path_noc import PathNoc  # Class is named PathNoc (not Path).


def setup():
    global path
    size(640, 240)

    path = PathNoc()  # A path object (series of connected points).


def draw():
    background(255)
    path.show()  # Display the path.
