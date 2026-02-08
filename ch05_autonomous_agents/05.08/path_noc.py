# PY5 IMPORTED MODE CODE

"""
NOTE:
Imported py5 mode injects pathlib.Path into the module namespace. Therefore,
the class is named PathNoc (not Path), avoiding a name clash that breaks import.
"""


class PathNoc:

    def __init__(self):
        self.radius = 20  # A path has a radius, indicating its width.
        self.points = []  # A path is now an list of points (vector objects).

#        # A path has only two points, start and end.
#        self.start = Py5Vector2D(0, height / 3)
#        self.end = Py5Vector2D(width, (2 * height) / 3)

    # Computed property -- accessed as path_noc.start (no parentheses).
    @property
    def start(self) -> Py5Vector2D:
        return self.points[0]

    # Computed property -- accessed as path_noc.end (no parentheses).
    @property
    def end(self) -> Py5Vector2D:
        return self.points[-1]

    def add_point(self, x: float, y: float) -> None:
        """This method allows you to add points to the path."""

        path_point = Py5Vector2D(x, y)
        self.points.append(path_point)

    def show(self):
        """Display the path."""

#         stroke_weight(self.radius * 2)
#         stroke(0, 50)
#         line(self.start.x, self.start.y, self.end.x, self.end.y)
#         stroke_weight(1)
#         stroke(0)
#         line(self.start.x, self.start.y, self.end.x, self.end.y)

        # Draw a thicker gray line for the path radius.
        stroke(175)
        stroke_weight(self.radius * 2)
        no_fill()
        begin_shape()
        for path_point in self.points:
            vertex(*path_point)
        end_shape()

        # Draw a thin line for the path center.
        stroke(0)
        stroke_weight(1)
        begin_shape()
        for path_point in self.points:
            vertex(*path_point)
        end_shape()
