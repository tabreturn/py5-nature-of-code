# PY5 IMPORTED MODE CODE

"""
NOTE:
Imported py5 mode injects pathlib.Path into the module namespace. Therefore,
the class is named PathNoc (not Path), avoiding name clash that breaks imports.
"""


class PathNoc:

    def __init__(self):
        # A path has a radius, indicating its width.
        self.radius = 20

        # A path has only two points, start and end.
        self.start = Py5Vector2D(0, height / 3)
        self.end = Py5Vector2D(width, (2 * height) / 3)

    def show(self):
        """Display the path."""
        stroke_weight(self.radius * 2)
        stroke(0, 50)
        line(self.start.x, self.start.y, self.end.x, self.end.y)
        stroke_weight(1)
        stroke(0)
        line(self.start.x, self.start.y, self.end.x, self.end.y)
