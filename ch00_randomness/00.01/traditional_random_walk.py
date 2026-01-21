# https://natureofcode.com/random/#the-random-walker-class


class Walker:

    # Objects have a constructor where they are initialized.
    def __init__(self):
        # Objects have data.
        self.x = width / 2
        self.y = height / 2

    def show(self) -> None:  # Objects have methods.
        stroke(0)
        point(self.x, self.y)

    def step(self) -> None:
        # 0, 1, 2, or 3. The random choice determines the step.
        match floor(random(4)):
            # Four possible steps.
            case 0: self.x += 1
            case 1: self.x -= 1
            case 2: self.y += 1
            case 3: self.y -= 1

#        # Eight possible steps.
#        # Yields -1, 0, or 1
#        self.x += random_int(-1, 1)
#        self.y += random_int(-1, 1)
#        # Instead use random() for any floating-point number from -1 to 1.


# Remember how p5.js works? setup() is executed once when the sketch starts.
def setup():
    global walker  # A Walker object.
    size(640, 240)
    walker = Walker()  # Create the walker.
    background(255)


# Then draw() loops forever and ever (until you quit).
def draw():
    # Call functions on the walker.
    walker.step()
    walker.show()

