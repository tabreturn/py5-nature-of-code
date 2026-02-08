# https://natureofcode.com/autonomous-agents/#flow-fields

from flow_field import FlowField
from vehicle import Vehicle

debug = True


def setup():
    global monospace, flow_field, vehicles
    size(640, 240)
    monospace = create_font('../../DejaVuSansMono.ttf', 32)

    flow_field = FlowField(20)  # Make new flow field with 'resolution' of 16.

    # Make a whole bunch of vehicles with random max_speed and max_force values.
    vehicles = [
      Vehicle(random(width), random(height), random(2, 5), random(0.1, 0.5))
      for _ in range(120)
    ]


def draw():
    background(255)

    # Display the flowfield in "debug" mode.
    if debug: flow_field.show()
    # Tell all the vehicles to follow the flow field.
    for vehicle in vehicles:
        vehicle.follow_flow(flow_field)
        vehicle.run()

    # Display some info.
    fill(0); text_font(monospace); text_size(11)
    text(
      f'Hit space bar to toggle debugging lines.\n'
      f'Click the mouse to generate a new flow field.',
      10, 216,
    )


# The function(s) below are for mouse/key interaction

def key_pressed():
    global debug
    if key == ' ': debug = not debug

def mouse_pressed():
    global flow_field
    flow_field.init()
