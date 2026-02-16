# PY5 IMPORTED MODE CODE

from sensor import Sensor


class Creature:

    def __init__(self, x: float = 0.0, y: float = 0.0):
        # The creature has a position and radius.
        self.position = Py5Vector2D(x, y)
        self.r = 16

        self.total_sensors = 15  # How about 15 sensors?
        # Create the sensors for the creature.
        self.sensors = [
          Sensor(
            Py5Vector2D
              # First, calculate a direction for the sensor.
              .from_heading(remap(i, 0, self.total_sensors, 0, TAU))
              # Create a vector a little bit longer than radius as the sensor.
              .set_mag(self.r * 2)
          )
          for i in range(self.total_sensors)
        ]

    def sense(self, food: 'Food') -> None:
        """Call the sense() method for each sensor."""

        for sensor in self.sensors:
            sensor.sense(self.position, food)

    def show(self) -> None:
        """Draw the creature and all the sensors."""

        push()
        translate(*self.position)

        for sensor in self.sensors:
            stroke(0)
            line(0, 0, sensor.v.x, sensor.v.y)
            if sensor.value > 0:
                fill(255, sensor.value * 255)
                stroke(0, 100)
                circle(sensor.v.x, sensor.v.y, 8)

        no_stroke()
        fill(0)
        circle(0, 0, self.r * 2)
        pop()
