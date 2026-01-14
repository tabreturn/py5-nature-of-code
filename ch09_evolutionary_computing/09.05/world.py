from py5 import get_current_sketch, Py5Vector2D, random
from bloop import Bloop
from dna import DNA
from food import Food


class World:
    """The World class manages the population of bloops and all the food."""
    def __init__(self, population_size: int):
        # Create the population.
        self.bloops = [
          # Create each bloop with a starting position.
          Bloop(
            Py5Vector2D(
              random(get_current_sketch().width),
              random(get_current_sketch().height)
            ),
            DNA()
          )
          for _ in range(population_size)
        ]
        # Create the food.
        self.food = Food(population_size)

    def run(self) -> None:
        """Run the world."""
        # This method draws the food and adds new food when necessary.
        self.food.run()

        # Manage bloops (cycle through array backward since bloops are deleted).
        for i in range(len(self.bloops) - 1, -1, -1):
            # All bloops run and eat.
            bloop = self.bloops[i]
            bloop.run()
            bloop.eat(self.food)
            # If the bloop is dead, remove it and create food.
            if bloop.dead():
                self.bloops.pop(i)
                self.food.add(bloop.position)
                continue
            # Here is where each living bloop has a chance to reproduce.
            child = bloop.reproduce()
            # If it does, the child is added to the population.
            # The value of the child is undefined if parent does not reproduce.
            if child is not None:
                self.bloops.append(child)

    def born(self, x: int, y: int) -> None:
        """We can add a creature manually if we so desire."""
        position = Py5Vector2D(x, y)
        self.bloops.append(Bloop(position, DNA()))