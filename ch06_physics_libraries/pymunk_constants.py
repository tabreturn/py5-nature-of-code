"""
Since the Matter.js and Pymunk engines use different units and solvers,
these values provide an *approximate* conversion for matching visual behavior.
"""

SCALE_GRAVITY = 900.0

FPS = 60.0
DT = 1.0 / FPS
SCALE_TIME = FPS

SCALE_VELOCITY = SCALE_TIME
SCALE_ANG_VELOCITY = SCALE_TIME
SCALE_FRICTION = SCALE_TIME
