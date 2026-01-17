import os
import pickle

import neat
import random


WIDTH = 640
HEIGHT = 240


class BirdSim:
    def __init__(self):
        self.x = 50
        self.y = 120.0
        self.velocity = 0.0
        self.gravity = 0.5
        self.flap_force = -10.0
        self.fitness = 0.0
        self.alive = True

    def flap(self) -> None:
        self.velocity += self.flap_force

    def update(self) -> None:
        if self.alive:
            self.velocity += self.gravity
            self.y += self.velocity
            self.velocity *= 0.95

            if self.y > HEIGHT or self.y < 0:
                self.alive = False

            self.fitness += 1.0


class PipeSim:
    def __init__(self):
        self.spacing = 100
        self.height = HEIGHT

        self.top = random.uniform(0.0, self.height - self.spacing)
        self.bottom = self.top + self.spacing

        self.x = WIDTH
        self.w = 20
        self.velocity = 2

    def update(self) -> None:
        self.x -= self.velocity

    def collides(self, bird: BirdSim) -> bool:
        vertical_collision = bird.y < self.top or bird.y > self.bottom
        horizontal_collision = bird.x > self.x and bird.x < self.x + self.w
        return vertical_collision and horizontal_collision

    def offscreen(self) -> bool:
        return self.x < -self.w


def eval_genomes(genomes, config):
    for genome_id, genome in genomes:
        net = neat.nn.FeedForwardNetwork.create(genome, config)

        bird = BirdSim()
        pipes = [PipeSim()]
        frame = 0

        while bird.alive and frame < 3000:
            next_pipe = None
            for pipe in pipes:
                if pipe.x + pipe.w > bird.x:
                    next_pipe = pipe
                    break

            if next_pipe is None:
                next_pipe = pipes[0]

            inputs = [
                bird.y / HEIGHT,
                bird.velocity / HEIGHT,
                next_pipe.top / HEIGHT,
                (next_pipe.x - bird.x) / WIDTH,
            ]

            out = net.activate(inputs)

            if len(out) == 1:
                if out[0] > 0.5:
                    bird.flap()
            else:
                if out[0] > out[1]:
                    bird.flap()

            bird.update()

            for i in range(len(pipes) - 1, -1, -1):
                pipes[i].update()
                if pipes[i].collides(bird):
                    bird.alive = False
                if pipes[i].offscreen():
                    pipes.pop(i)

            if frame % 100 == 0:
                pipes.append(PipeSim())

            frame += 1

        genome.fitness = bird.fitness


def run():
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')

    config = neat.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_path,
    )

    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    p.add_reporter(neat.StatisticsReporter())

    winner = p.run(eval_genomes, 50)

    winner_path = os.path.join(local_dir, 'winner.pkl')
    with open(winner_path, 'wb') as f:
        pickle.dump(winner, f)

    print('Saved winner to', winner_path)


if __name__ == '__main__':
    run()
