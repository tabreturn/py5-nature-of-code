"""
Since the Matter.js and Pymunk engines use different units and solvers,
these values provide an approximate conversion for matching visual behavior.
"""

# Scale factors to approximate Matter.js units in Pymunk.
SCALE_GRAVITY = 900.0
SCALE_VELOCITY = 60.0
SCALE_ANG_VELOCITY = 60.0
SCALE_FRICTION = 50.0

# Fixed timestep (equivalent to Matter.Runner internal delta time).
DT = 1 / 60
