# https://natureofcode.com/autonomous-agents/#example-59-separation

from vehicle import Vehicle


def setup():
    global vehicles  # Declare a list of Vehicle objects.
    size(640, 240)

    # Initialize and fill the list with a bunch of vehicles.
    vehicles = [
      Vehicle(random(width), random(height), 3, 0.2)
      for _ in range(25)
    ]


def draw():
    background(255)

    for vehicle in vehicles:
        # Vehicle examines all other vehicles to calculate a separation force.
        vehicle.separate(vehicles)
        vehicle.update()
        vehicle.borders_flow()
        vehicle.show()


# The function(s) below are for mouse/key interaction

def mouse_dragged():
    global vehicles
    if frame_count % 5 == 0:
        vehicles.append(Vehicle(mouse_x, mouse_y, 3, 0.2))
