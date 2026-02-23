# PY5 IMPORTED MODE CODE

# Note Matter.js uses 'aliases'; for py5 just import Pymunk symbols directly.
from pymunk import Body, Poly


class Box:

    # Needs "space" parameter because Python modules have isolated namespaces.
    # (p5.js sketches share a single global scope)
    def __init__(self, space: 'Space', x: float, y: float):
#        # A box has an (x, y) position and a width.
#        self.x = x
#        self.y = y
        self.w = 16

        """
        NOTE:
        Pymunk separates Body (physics) from Shape (collision geometry). 
        Multiple Shapes can attach to one Body. 
        Think: Body = physics; Shape = collision skin.
        """

        # Instead of any of the usual variables, store a reference to a body.
        self.body = Body(1.0, 1.0)
        self.body.position = (x, y)
        self.shape = Poly.create_box(self.body, (self.w, self.w))

        self.space = space  # Store reference for removing/etc.
        self.space.add(self.body, self.shape)  # Don't forget to add it to world!

    def show(self) -> None:
        # Need the body's position and angle.
        position = self.body.position
        angle = self.body.angle

        # The box is drawn as a square().
        rect_mode(CENTER)
        fill(127)
        stroke(0)
        stroke_weight(2)

        push()
        # Use the position and angle to translate and rotate the square.
        translate(position.x, position.y)
        rotate(angle)
        rect(0, 0, self.w, self.w)
        pop()

    def remove_body(self) -> None:
        """This function removes a body from the Matter.js world."""

        self.space.remove(self.shape, self.body)

    def check_edge(self) -> bool:
        return self.body.position.y > height + self.w
