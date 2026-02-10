from boid import Boid


class Flock:

    def __init__(self):
        self.boids = []

    def run(self):
        for boid in self.boids:
            # Each Boid object must know about all the other boids.
            boid.run(self.boids)

    def add_boid(self, boid):
        self.boids.append(boid)
