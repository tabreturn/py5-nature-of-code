from py5 import fill, circle, get_current_sketch, stroke, stroke_weight



from brain_ga import Brain


class Bird:
    def __init__(self, brain: Brain | None = None):
        self.brain = brain if brain is not None else Brain(
          inputs = 4,
          outputs = 1,  # flap / no flap
        )

        self.x = 50  # The bird's position (x will be constant).
        self.y = 120.0
        # Velocity and forces are scalar since bird moves only along the y-axis.
        self.velocity = 0.0
        self.gravity = 0.5
        self.flap_force = -10.0

        self.fitness = 0.0
        self.alive = True

    def flap(self) -> None:
        """The bird flaps its wings."""

        self.velocity += self.flap_force

    def think(self, pipes):
        # Find the next pipe in front of the bird
        next_pipe = None
        for pipe in pipes:
            if pipe.x + pipe.w > self.x:
                next_pipe = pipe
                break
        if next_pipe is None:
            return

        sketch = get_current_sketch()
        w, h = sketch.width, sketch.height

        # Same 4 inputs as your earlier NEAT sim used: y, vel, pipe.top, pipe dx
        inputs = [
            self.y / h,
            self.velocity / 10.0,          # better scaling than /height
            next_pipe.top / h,
            (next_pipe.x - self.x) / w,
        ]

        if self.brain.predict_flap(inputs):
            self.flap()

    def update(self) -> None:



        if not self.alive:
            return






        self.velocity += self.gravity  # Add gravity.
        self.y += self.velocity

        # Dampen velocity.
        self.velocity *= 0.95

        # Handle the floor.
        '''
        if self.y > get_current_sketch().height:
            self.y = get_current_sketch().height
            self.velocity = 0'''
        h = get_current_sketch().height
        if self.y > h or self.y < 0:
            self.alive = False

        # score = time alive (like JS)
        self.fitness += 1.0

    def show(self) -> None:
        stroke_weight(2)
        stroke(0)
        fill(127, 200)
        circle(self.x, self.y, 16)
