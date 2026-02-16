# PY5 IMPORTED MODE CODE


class Sensor:

    def __init__(self, v: Py5Vector2D):
        self.v = v.copy
        # The sensor also stores a value for the proximity of what it's sensing.
        self.value = 0

    def sense(self, position: Py5Vector2D, food: 'Food') -> None:
        # Find tip (or endpoint) of sensor by adding the creature's position.
        end = position + self.v
        # How far is it from the food's center?
        d = end.dist(food.position)

        # If the sensor is within the radius, light up the sensor.
        if d < food.r:
            # The farther into the food's center, the more the sensor activates.
            self.value = remap(d, 0, food.r, 1, 0)
        else:
            self.value = 0
