# https://natureofcode.com/autonomous-agents/#example-512-bin-lattice-spatial-subdivision

"""
NOTE:
Although this simulation runs much slower than the p5.js version, it still
demonstrates a major improvement over 05.11 (flocking), with the FPS counter
here showing roughly double the frame rate for the same flock size.
"""

from boid import Boid
from flock import Flock

RESOLUTION = 40  # Each cell is 40×40 pixels.


def setup():
    global cols, rows, flock, grid, monospace
    size(640, 240)
    monospace = create_font('../../DejaVuSansMono.ttf', 32)

    # How many columns and rows are in the grid, based on the width and height?
    cols = floor(width / RESOLUTION)
    rows = floor(height / RESOLUTION)

    # Create the 2D list.
    grid = [[[] for _ in range(rows)] for _ in range(cols)]

    flock = Flock()
    # The flock starts out with 120 (÷3) boids.
    for _ in range(120 // 3):
        boid = Boid(random(width), random(height), 3, 0.05)
        boid.r = 3.0
        boid.velocity = random(-1, 1), random(-1, 1)
        flock.add_boid(boid)
    

def draw():
    global grid
    background(255)

    # Each frame, the grid is reset to empty arrays.
    [cell.clear() for col in grid for cell in col]

    # Place each boid into appropriate cell in grid.
    for boid in flock.boids:
        # Find the right column and row.
        column = floor(boid.position.x / RESOLUTION)
        row = floor(boid.position.y / RESOLUTION)
        # Constrain to the limits of the array.
        column = constrain(column, 0, cols - 1)
        row = constrain(row, 0, rows - 1)
        # Add the boid.
        grid[column][row].append(boid)

    # Draw the grid.
    stroke(175)
    stroke_weight(1)

    # Draw vertical lines.
    for i in range(cols + 1):
        line(i * RESOLUTION, 0, i * RESOLUTION, height)

    # Draw horizontal lines.
    for j in range(rows + 1):
        line(0, j * RESOLUTION, width, j * RESOLUTION)

    # Highlight the 3x3 neighborhood the mouse is over.
    mouse_col = floor(mouse_x / RESOLUTION)
    mouse_row = floor(mouse_y / RESOLUTION)
    no_stroke()
    fill(255, 50, 50, 100)  # Semi-transparent red.
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            col = mouse_col + i
            row = mouse_row + j
            # Check if the cell is within the grid.
            if 0 <= col < cols and 0 <= row < rows:
                square(col * RESOLUTION, row * RESOLUTION, RESOLUTION)

    flock.run(grid, RESOLUTION)

    # Display some info.
    text_align(LEFT); text_font(monospace); text_size(11); fill(0)
    text(f'FPS: {int(get_frame_rate())}', 10, 226)
