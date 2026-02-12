# https://natureofcode.com/autonomous-agents/#more-optimization-tricks

SC_PRECISION = 0.5                  # Set table precision to 0.5 degrees.
SC_INV_PREC = 1 / SC_PRECISION      # Caculate reciprocal for conversions.
SC_PERIOD = int(360 * SC_INV_PREC)  # Compute required table length.



def init_sin_cos() -> None:
    """Init sin/cos tables with values. Should be called from setup()."""

    global sin_lut, cos_lut

    sin_cos_luts = [
      [sin(i * DEG_TO_RAD * SC_PRECISION), cos(i * DEG_TO_RAD * SC_PRECISION)]
      for i in range(SC_PERIOD)
    ]

    sin_lut, cos_lut = map(list, zip(*sin_cos_luts))


def setup():
    size(640, 240)
    init_sin_cos()  # Important call to initialize lookup tables.


def draw():
    background(255)

    # Modulate the current radius.
    radius = 50 + 50 * sin_lut[frame_count % SC_PERIOD]

    # Draw a circle made of points (every 5 degrees).
    for i in range(0, 360, 5):
        # Convert degrees into array index.
        theta = int((i * SC_INV_PREC) % SC_PERIOD) # Modulo ensures periodicity.
        stroke_weight(4)
        # Draw the circle around mouse position.
        point(
          width / 2 + radius * cos_lut[theta],
          height / 2 + radius * sin_lut[theta]
        )
