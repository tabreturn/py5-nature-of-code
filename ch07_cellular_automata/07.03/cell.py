# PY5 IMPORTED MODE CODE


class Cell:

    def __init__(self, state: int, x: int, y: int, w: int):
        self.state = state  # What is the cell's state?
        self.previous = self.state  # What was its previous state?

        # Position and size.
        self.x = x
        self.y = y
        self.w = w

    def show(self) -> None:
        stroke(0)

        if self.previous == 0 and self.state == 1:  # If cell born, color blue!
            fill(0, 0, 255)
        elif self.state == 1:
            fill(0)
        elif self.previous == 1 and self.state == 0:  # If cell dies, color red!
            fill(255, 0, 0)
        else:
            fill(255)

        square(self.x, self.y, self.w)
