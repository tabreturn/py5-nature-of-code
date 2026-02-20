# https://natureofcode.com/cellular-automata/#the-game-of-life

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
            board[i][j] = random_int()  # Calculate the state for each cell.
            # With no arguments, random_int() return zero or one.


def draw():
    global board

    next_ = create_2d_array(columns, rows)  # The next board

    # Loop but skip the edge cells.
    for i in range(1, columns - 1):
        for j in range(1, rows - 1):

            # Add up all neighbor states to calculate number of live neighbors.
            neighbor_sum = sum(
              board[i + k][j + l]  # Use k/l as counters since i/j used!
              for k in range(-1, 2)
              for l in range(-1, 2)
            )
            neighbor_sum -= board[i][j]  # Correct by subtracting the cell state.

            # The rules of life!

            # If cell alive with < 2 live neighbors, it dies from loneliness.
            if board[i][j] == 1 and neighbor_sum < 2:
                next_[i][j] = 0
            # If cell alive with > 3 live neighbors, it dies from overpopulation.
            elif board[i][j] == 1 and neighbor_sum > 3:
                next_[i][j] = 0
            # If cell dead with 3 live neighbors (exactly), it is born!
            elif board[i][j] == 0 and neighbor_sum == 3:
                next_[i][j] = 1
            # In all other cases, the cell's state remains the same.
            else:
                next_[i][j] = board[i][j]

    for i in range(columns):
        for j in range(rows):
            # Evaluate to 255 when the state is 0, and 0 when the state is 1.
            fill(255 - board[i][j] * 255)

            stroke(0)
            square(i * W, j * W, W)

    board = next_


def create_2d_array(columns: int, rows: int) -> list[list[int]]:
    return [[0 for _ in range(rows)] for _ in range(columns)]
