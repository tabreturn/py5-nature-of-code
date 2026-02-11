from boid import Boid


class Flock:

    def __init__(self):
        self.boids = []

    def run(self) -> None:
        for boid in self.boids:
            # Each Boid object must know about all the other boids.
            boid.run(self.boids)

    def add_boid(self, boid: Boid) -> None:
        self.boids.append(boid)
