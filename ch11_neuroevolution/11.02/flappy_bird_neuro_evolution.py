# https://natureofcode.com/neuroevolution/#reinforcement-learning

from bird import Bird
from pipe import Pipe

# ml5.js-style neural network functionality implemented with bespoke class.
from brain_ga import Brain






POP_SIZE = 200
PIPE_INTERVAL = 100



def setup():
    global birds, pipes
    size(640, 240)
    # Create a bird and start with one pipe.
    birds = [Bird() for _ in range(POP_SIZE)]
    pipes = [Pipe()]


def mouse_pressed():
    # The bird flaps its wings when the mouse is clicked.
    bird.flap()


def draw():
    global birds, pipes

    background(255)

    '''
    # Handle all the pipes.
    for pipe in reversed(pipes):
        pipe.show()
        pipe.update()

        if pipe.collides(bird):
            text('OOPS!', pipe.x, pipe.top + 20)

        if pipe.offscreen():
            pipes.remove(pipe)
    '''
    # Handle all the pipes.
    for i in range(len(pipes) - 1, -1, -1):
        pipes[i].update()
        pipes[i].show()
        if pipes[i].offscreen():
            pipes.pop(i)





    for bird in birds:
        if not bird.alive:
            continue

        # collisions (Pipe.collides uses bird.x/bird.y etc.) :contentReference[oaicite:3]{index=3}
        for pipe in pipes:
            if pipe.collides(bird):
                bird.alive = False
                break

        if bird.alive:
            bird.think(pipes)
            bird.update()
            bird.show()

        '''
        # Update and show the bird.
        bird.update()
        bird.show()'''


        '''
    # Add a new pipe every 100 frames.
    if frame_count % 100 == 0:
        pipes.append(Pipe())'''





    sketch = get_current_sketch()
    if sketch.frame_count % PIPE_INTERVAL == 0:
        pipes.append(Pipe())


    if all_birds_dead(birds):
        next_gen = reproduction(birds)
        birds[:] = next_gen
        reset_pipes(pipes)


def all_birds_dead(birds_list) -> bool:
    return all(not b.alive for b in birds_list)


def reset_pipes(pipes_list):
    if len(pipes_list) > 1:
        del pipes_list[:-1]


def normalize_fitness(birds_list):
    total = 0.0
    for b in birds_list:
        b.fitness = b.fitness * b.fitness
        total += b.fitness

    if total == 0.0:
        p = 1.0 / len(birds_list)
        for b in birds_list:
            b.fitness = p
        return

    for b in birds_list:
        b.fitness = b.fitness / total


def weighted_selection(birds_list) -> Brain:
    r = random()
    idx = 0
    while r > 0.0:
        r -= birds_list[idx].fitness
        idx += 1
        if idx >= len(birds_list):
            idx = len(birds_list) - 1
            break
    idx -= 1
    if idx < 0:
        idx = 0
    return birds_list[idx].brain


def reproduction(birds_list):
    normalize_fitness(birds_list)

    next_birds = []

    elite = sorted(birds_list, key=lambda b: b.fitness, reverse=True)[:2]
    for e in elite:
        next_birds.append(Bird(e.brain.copy()))

    while len(next_birds) < len(birds_list):
        parentA = weighted_selection(birds_list)
        parentB = weighted_selection(birds_list)

        child = Brain.crossover(parentA, parentB)
        child.mutate(rate=0.01, sigma=0.5)  # JS-like mutate(0.01)

        next_birds.append(Bird(child))

    return next_birds
