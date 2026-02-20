# https://natureofcode.com/cellular-automata/#object-oriented-cells

from cell import Cell

W = 8


def setup():
    global board, columns, rows
    size(640, 240)

    columns = width // W
    rows = height // W

    board = create_2d_array(columns, rows)

    for i in range(1, columns - 1):
        for j in range(1, rows - 1):
            # Start each cell with a 0 or 1.
            board[i][j] = Cell(random_int(), i * W, j * W, W)
            # With no arguments, random_int() return zero or one.


def draw():
    # Loop but skip the edge cells.
    for i in range(1, columns - 1):
        for j in range(1, rows - 1):

            # Add up all neighbor states to calculate number of live neighbors.
            neighbor_sum = sum(
              board[i + k][j + l].previous  # Use k/l as counters since i/j used!
              for k in range(-1, 2)
              for l in range(-1, 2)
            )
            # Use the previous state when counting neighbors.
            neighbor_sum -= board[i][j].previous

            # The rules of life!

            # If cell alive with < 2 live neighbors, it dies from loneliness.
            if board[i][j].state == 1 and neighbor_sum < 2:
                board[i][j].state = 0
            # If cell alive with > 3 live neighbors, it dies from overpopulation.
            elif board[i][j].state == 1 and neighbor_sum > 3:
                board[i][j].state = 0
            # If cell dead with 3 live neighbors (exactly), it is born!
            elif board[i][j].state == 0 and neighbor_sum == 3:
                board[i][j].state = 1
            # Else do nothing!

    for i in range(columns):
        for j in range(rows):
            board[i][j].show()
            board[i][j].previous = board[i][j].state


def create_2d_array(columns: int, rows: int) -> list[list[Cell]]:
    return [
      [Cell(0, i * W, j * W, W) for j in range(rows)]
      for i in range(columns)
    ]
