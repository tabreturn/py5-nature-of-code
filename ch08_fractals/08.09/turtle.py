# PY5 IMPORTED MODE CODE


class Turtle:

    def __init__(self, length: int, angle: float):
        self.length = length
        self.angle = angle

    def render_(self, sentence: str) -> None:
        stroke(0)

        for c in sentence:  # Look at each character one at a time.
            # This could also be written with if...else statements.
            match c:  # Python equivalent of a JS switch statement.
                case 'F':
                    line(0, 0, 0, -self.length)
                    translate(0, -self.length)
                case 'G':
                    translate(0, -self.length)
                case '+':
                    rotate(self.angle)
                case '-':
                    rotate(-self.angle)
                case '[':
                    push()
                case ']':
                    pop()
