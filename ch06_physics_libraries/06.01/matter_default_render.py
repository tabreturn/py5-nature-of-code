# https://natureofcode.com/physics-libraries/#importing-the-matterjs-library

# Note Matter.js uses 'aliases'; for py5 just import Pymunk symbols directly.
from pymunk import Body, moment_for_box, Poly, Space
# (Matter.js example imports Bodies, Body, Engine, Composite, Render, Vector)

import sys, os; sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from pymunk_constants import *  # Matter.js <-> Pymunk calibration constants.


def setup():
    global engine  # A reference to the Pymunk physics engine.
    global box_body, box_shape, ground_body, ground_shape, render_params
    size(640, 240)

    # Create the Pymunk world.
    engine = Space()  # Pymunk's "world/engine" is a Space.
    # Change the engine's gravity to point downward.
    engine.gravity = (0, 1.0 * SCALE_GRAVITY)

    # Configure the renderer.
    render_params = {
      'fill': (0, 0),      # Transparent fills (black shows through).
      'stroke': 255,       # White outlines.
      'stroke_weight': 1,
    }

    """
    NOTE:
    Pymunk separates Body (physics) from Shape (collision geometry). 
    Multiple Shapes can attach to one Body. 
    Think: Body = physics; Shape = collision skin.
    """

    # Create a box with custom friction and restitution.
    options = {  # Specify the properties of this body in a dictionary.
      'friction': 0.01 * SCALE_FRICTION,
      'restitution': 0.75,
      'mass': 1.0,  # In Pymunk, use mass/moment instead of density.
    }
    w, h = 50, 50
    box_body = Body(
      options['mass'],
      moment_for_box(options['mass'], (w, h)),
    )
    box_body.position = (100, 100)
    box_shape = Poly.create_box(box_body, (w, h))
    box_shape.friction = options['friction']
    box_shape.elasticity = options['restitution']
    # Set the initial velocity of the box.
    box_body.velocity = (5.0 * SCALE_VELOCITY, 0.0 * SCALE_VELOCITY)
    box_body.angular_velocity = 0.1 * SCALE_ANG_VELOCITY
    # Add the box object to the world.
    engine.add(box_body, box_shape)

    # Create a static body+shape for the ground.
    ground_body = Body(body_type=Body.STATIC)
    ground_body.position = (width / 2, height - 5)
    ground_shape = Poly.create_box(ground_body, (width * 2, 10))
    ground_shape.friction = 2.0
    ground_shape.elasticity = 0.2
    engine.add(ground_body, ground_shape)


def draw():
    background(0)

    # Run the engine!
    engine.step(DT)
    # Run the renderer!
    render_run(ground_shape, box_shape)


def render_run(*polygons: Poly) -> None:
    """Simulate Matter.js debug-drawing-style wireframe renderer."""

    fill(*render_params['fill'])
    stroke(render_params['stroke'])
    stroke_weight(render_params['stroke_weight'])

    for polygon in polygons:
        body = polygon.body
        begin_shape()
        for vertex_ in polygon.get_vertices():
            vertex(*body.local_to_world(vertex_))
        end_shape(CLOSE)
