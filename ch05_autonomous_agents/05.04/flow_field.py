# PY5 IMPORTED MODE CODE


class FlowField:

    def __init__(self, r: int):
        # Resolution of grid relative to canvas width and height in pixels.
        self.resolution = r

        # Determine the number of columns and rows.
        self.cols = floor(width / self.resolution)
        self.rows = floor(height / self.resolution)

        # A flow field is a 2D list of vectors.
        self.field = [
          [None for _ in range(self.rows)]
          for _ in range(self.cols)
        ]

        self.init()  # ... a separate function to create that 2D list.

    def init(self) -> None:
        """The init() method fills the 2D list with vectors."""

        noise_seed(int(random(10000)))  # Reseed noise for new field each time.

        x_off = 0.0
        # Use a nested loop to hit every column and every row of flow field.
        for i in range(self.cols):
            y_off = 0.0

            for j in range(self.rows):
                # Use Perlin noise to create the vectors.
                angle = remap(noise(x_off, y_off), 0, 1, 0, TWO_PI)  # 2D noise.
                self.field[i][j] = Py5Vector2D.from_heading(angle)
                y_off += 0.1

            x_off += 0.1

    def lookup(self, position: Py5Vector2D) -> Py5Vector2D:
        """A method to return a vector based on a position."""

        # Use constrain().
        column = constrain(floor(position.x / self.resolution), 0, self.cols - 1)
        row = constrain(floor(position.y / self.resolution), 0, self.rows - 1)

        # Use .copy to ensure that a copy of the vector is returned.
        return self.field[column][row].copy

    def show(self) -> None:
        """Draw every vector."""

        w = width / self.cols
        h = height / self.rows
        stroke_weight(1)

        for i in range(self.cols):
            for j in range(self.rows):
                v = self.field[i][j].copy
                v.set_mag(w * 0.5)
                x = i * w + w / 2
                y = j * h + h / 2
                line(x, y, x + v.x, y + v.y)
