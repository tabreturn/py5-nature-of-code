# PY5 IMPORTED MODE CODE


class Spring:

    def __init__(self, x: float, y: float, length: float):
        """The constructor initializes the anchor point and rest length."""

        self.anchor = Py5Vector2D(x, y)  # The spring's anchor position.
        # Rest length and spring constant variables
        self.rest_length = length
        self.k = 0.2

    def connect(self, bob: 'Bob') -> None:
        """Calculate the spring force as an implementation of Hooke's law."""

        # Get a vector pointing from the anchor to the bob position.
        force = bob.position - self.anchor

        # Calculate the displacement between the distance and rest length.
        # Use the variable name "stretch" instead of x to be descriptive.
        current_length = force.mag
        stretch = current_length - self.rest_length

        # Put it together: direction and magnitude!
        force.set_mag(-1 * self.k * stretch)

        # The connect() method takes care of calling apply_force().
        # Therefore, it doesn't have to return a vector to the calling area.
        bob.apply_force(force)

    def constrain_length(self, bob: 'Bob', min_len: float, max_len: float) -> None:
        # A vector pointing from the bob to the anchor.
        direction = bob.position - self.anchor
        length = direction.mag

        # Is it too short? Is it too long?
        if min_len <= length <= max_len:
            return

        # Keep the position within the constraint.
        target_len = min_len if length < min_len else max_len
        direction.set_mag(target_len)

        bob.position = self.anchor + direction
        bob.velocity *= 0

    def show(self) -> None:
        """Draw the anchor."""

        fill(127)
        circle(self.anchor.x, self.anchor.y, 10)

    def show_line(self, bob: 'Bob') -> None:
        """Draw the spring connection between the bob position and anchor."""

        stroke(0)
        line(bob.position.x, bob.position.y, self.anchor.x, self.anchor.y)
