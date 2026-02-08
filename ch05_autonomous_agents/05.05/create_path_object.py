# https://natureofcode.com/autonomous-agents/#simple-path-following

from path_noc import PathNoc  # Class is named PathNoc (not Path).
from vehicle import Vehicle


debug = True  # Variable to decide whether to draw all the stuff.


def setup():
    global monospace, path, vehicle_1, vehicle_2
    size(640, 240)
    monospace = create_font('../../DejaVuSansMono.ttf', 32)

    path = PathNoc()  # A path object (series of connected points).

    # Each vehicle has different max_speed and max_force for demo purposes.
    vehicle_1 = Vehicle(0, height / 2, 2, 0.02)
    vehicle_1.velocity = Py5Vector2D(2, 0)
    vehicle_2 = Vehicle(0, height / 2, 3, 0.05)
    vehicle_2.velocity = Py5Vector2D(2, 0)


def draw():
    background(255)
    path.show()  # Display the path.

    # The boids follow the path.
    vehicle_1.follow_path(path, debug)
    vehicle_2.follow_path(path, debug)
    # Call the generic run method (update, borders, display, etc.)
    vehicle_1.run()
    vehicle_2.run()    
    # Check if it gets to the end of the path since it's not a loop.
    vehicle_1.borders_path(path)
    vehicle_2.borders_path(path)

    # Display some info.
    fill(0); text_font(monospace); text_size(11)
    text('Hit space bar to toggle debugging lines.', 10, 226)


# The function(s) below are for mouse/key interaction

def key_pressed():
    global debug
    if key == ' ': debug = not debug
