from boid import Boid


class Flock:

    def __init__(self):
        self.boids = []

    def run(self, grid: list[list[list['Boid']]], resolution: int) -> None:
        for boid in self.boids:
            # Each Boid object must know about all the other boids.
            boid.run(self.boids, grid, resolution)

    def run_qtree(self, qtree: 'QuadTree') -> None:
        for boid in self.boids:
            boid.run_qtree(qtree)

    def add_boid(self, boid: Boid) -> None:
        self.boids.append(boid)
