from boid import Boid


class Flock:

    def __init__(self):
        self.boids = []

    def run(self, grid: list[list[list['Boid']]], resolution: int) -> None:
        for boid in self.boids:
            # Each Boid object must know about all the other boids.
            boid.run(self.boids, grid, resolution)

    def add_boid(self, boid: Boid) -> None:
        self.boids.append(boid)
