# PY5 IMPORTED MODE CODE

import sys, os; sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from brain_ne import Brain

from sensor import Sensor
from food import Food


class Creature:

    def __init__(self, x: float, y: float, brain: Brain | None = None):
        # The creature has a position and radius.
        self.position = Py5Vector2D(x, y)

        self.full_size = 12
        self.r = 12

        # The creature has a list of sensors.
        self.total_sensors = 15  # How about 15 sensors?
        # Create the sensors for the creature.
        self.sensors = [
          Sensor(
            Py5Vector2D
              # First, calculate a direction for the sensor.
              .from_heading(remap(i, 0, self.total_sensors, 0, TAU))
              # Create a vector a little bit longer than radius as the sensor.
              .set_mag(self.full_size * 1.5)
          )
          for i in range(self.total_sensors)
        ]

        self.brain = (
          brain
          if brain is not None
          else Brain(
            inputs = len(self.sensors),
            outputs = 2,  # Angle and magnitude.
          )
        )
        self.health = 100  # The health starts at 100.
        self.acceleration = Py5Vector2D()
        self.velocity = Py5Vector2D()
        self.max_speed = 2

#    def sense(self, food: 'Food') -> None:
#        """Call the sense() method for each sensor."""
#
#        for sensor in self.sensors:
#            sensor.sense(self.position, food)

    def show(self) -> None:
        """Draw the creature and all the sensors."""

        push()
        translate(*self.position)

        for sensor in self.sensors:
            stroke(0, self.health * 2)
            line(0, 0, sensor.v.x, sensor.v.y)
            if sensor.value > 0:
                fill(255, sensor.value * 255)
                stroke(0, 100)
                circle(sensor.v.x, sensor.v.y, 8)

        no_stroke()
        fill(0, self.health * 2)
        self.r = remap(self.health, 0, 100, 2, self.full_size)
        self.r = constrain(self.r, 2, self.full_size)
        circle(0, 0, self.r * 2)
        pop()

    def think(self, food_list: list[Food]) -> None:
        # Build an input array from the sensor values.
        for sensor in self.sensors:
            sensor.value = 0.0
            for food in food_list:
                sensor.sense(self.position, food)
        inputs = [s.value for s in self.sensors]

        # Predict a steering force from the sensors.
        outputs = self.brain.predict_continuous_01(inputs)
        angle = outputs[0] * TAU
        magnitude = outputs[1]
        force = Py5Vector2D.from_heading(angle)
        force.set_mag(magnitude)
        self.apply_force(force)

    def update(self) -> None:
        """A simple physics engine (Euler integration)."""

        # Velocity changes according to acceleration.
        self.velocity.set_limit(self.max_speed)
        self.velocity += self.acceleration
        # Position changes according to velocity.
        self.position += self.velocity
        self.acceleration *= 0

        self.health -= 0.25  # Lose some health!

    def apply_force(self, force: Py5Vector2D) -> None:
        """Accumulate forces into acceleration (Newton's second law)."""

        self.acceleration += force

    def reproduce(self) -> 'Creature':
        # Copy and mutate rather than use crossover and mutate.
        brain = self.brain.copy()
        brain.mutate(0.1)

        return Creature(self.position.x, self.position.y, brain)

    def eat(self, food_list: list[Food]) -> None:
        """If the bloop is close to the food, increase its health!"""

        for i in range(len(food_list)):
            d = self.position.dist(food_list[i].position)

            if d < self.r + food_list[i].r:
                self.health += 0.5
                food_list[i].r -= 0.05

                if food_list[i].r < 20:
                    food_list[i] = Food()

    def borders(self) -> None:
        """Wraparound."""

        if self.position.x < -self.r: self.position.x = width + self.r
        elif self.position.x > width + self.r: self.position.x = -self.r
        if self.position.y < -self.r: self.position.y = height + self.r
        elif self.position.y > height + self.r: self.position.y = -self.r
