"""
Since the Matter.js and Pymunk engines use different units and solvers,
these values provide an approximate conversion for matching visual behavior.
"""

# Fixed timestep (equivalent to Matter.Runner internal delta time).
FPS = 60.0
DT = 1.0 / FPS
SCALE_TIME = FPS

# Scale factors to approximate Matter.js units in Pymunk.
SCALE_VELOCITY = SCALE_TIME
SCALE_ANG_VELOCITY = SCALE_TIME
SCALE_GRAVITY = SCALE_TIME ** 2
SCALE_FRICTION = SCALE_TIME
