# https://natureofcode.com/autonomous-agents/#combining-behaviors

from vehicle import Vehicle


def setup():
    global vehicles  # Declare a list of Vehicle objects.
    size(640, 240)

    # Initialize and fill the list with a bunch of vehicles.
    vehicles = [
      Vehicle(random(width), random(height), 3, 0.2)
      for _ in range(50)
    ]


def draw():
    background(255)

    for vehicle in vehicles:
        # Vehicle examines all other vehicles to calculate separate AND seek forces.
        vehicle.apply_behaviors(vehicles)
        vehicle.update()
        vehicle.borders_flow()
        vehicle.show()
