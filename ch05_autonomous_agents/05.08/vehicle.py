# PY5 IMPORTED MODE CODE


class Vehicle:

    def __init__(self, x: float, y: float, ms: float, mf: float):
        self.position = Py5Vector2D(x, y)
        self.velocity = Py5Vector2D()
        self.acceleration = Py5Vector2D()
        self.r = 4.0  # Additional variable for size.
        # Arbitrary values for max speed and force; try varying these!
        self.max_speed = ms
        self.max_force = mf

    def update(self) -> None:
        """Standard update function."""

        self.velocity += self.acceleration
        self.velocity.set_limit(self.max_speed)
        self.position += self.velocity
        self.acceleration *= 0

    def apply_force(self, force: Py5Vector2D) -> None:
        """Newton's second law (skipping the math)."""

        self.acceleration += force

    def seek(self, target: Py5Vector2D) -> None:
        """The seek steering force algorithm."""

        # Calculate the desired velocity to target at max speed.
        desired = target - self.position
        # If the magnitude of desired equals 0, skip out of here.
        if desired.mag == 0: return
        # Set desired velocity toward target at max_speed.
        desired.set_mag(self.max_speed)
        # Reynolds' formula for steering force.
        steer = desired - self.velocity
        # Limit the magnitude of the steering force.
        steer.set_limit(self.max_force)
        # Use the physics model and apply the force to the object's acceleration.
        self.apply_force(steer)

    def arrive(self, target: Py5Vector2D) -> None:
        desired = target - self.position
        # Distance is magnitude of vector pointing from position to the target.
        d = desired.mag

        # If closer than 100 pixels ...
        if d < 100:
            # ... set the magnitude according to how close it is.
            m = remap(d, 0, 100, 0, self.max_speed)
            desired.set_mag(m)
        else:
            # Otherwise, proceed at maximum speed.
            desired.set_mag(self.max_speed)

        steer = desired - self.velocity  # Usual steering = desired – velocity.
        steer.set_limit(self.max_force)
        self.apply_force(steer)

    def boundaries(self, offset: float) -> None:
        """This method receives an offset from the edges."""

        desired = None  # Start with a null desired velocity.

        # Make a desired velocity that retains the y-direction of the vehicle,
        # but points the x-direction directly away from the canvas edges.
        if self.position.x < offset:
            desired = Py5Vector2D(self.max_speed, self.velocity.y)
        elif self.position.x > width - offset:
            desired = Py5Vector2D(-self.max_speed, self.velocity.y)
        # Make a desired velocity that retains the x-direction of the vehicle,
        # but points the y-direction directly away from the canvas edges.
        if self.position.y < offset:
            desired = Py5Vector2D(self.velocity.x, self.max_speed)
        elif self.position.y > height - offset:
            desired = Py5Vector2D(self.velocity.x, -self.max_speed)

        # If the desired velocity is non-null, apply steering.
        if desired is not None:
            desired.normalize()
            desired *= self.max_speed
            steer = desired - self.velocity
            steer.set_limit(self.max_force)
            self.apply_force(steer)

    def follow_flow(self, flow: 'FlowField') -> None:
        # What is the vector at that spot in the flow field?
        desired = flow.lookup(self.position)
        desired.set_mag(self.max_speed)
        # Steering is desired minus velocity.
        steer = desired - self.velocity
        steer.set_limit(self.max_force)
        self.apply_force(steer)

    # Needs "debug" parameter because Python modules have isolated namespaces.
    # (p5.js sketches share a single global scope)
    def follow_path(self, path: 'PathNoc', debug: bool) -> None:

        # Step 1: Predict the vehicle's future position.
        future = self.velocity.copy  # Start by making a copy of the velocity.
        future.set_mag(50)  # Look ahead by setting the magnitude.
        future += self.position  # Add vector to position to find future position.

        target = None
        normal_noc = None  # "normal" is reverved for py5, hence "normal_noc".
        world_record = float('inf')  # Start with record that's easily beaten!

        distance = 0

        # Step 2: Find the normal point along the path.
#        normal_point = self.get_normal_point(future, path.start, path.end)
        for a, b in zip(path.points, path.points[1:]):
            # Find the normal for each line segment.
            normal_point = self.get_normal_point(future, a, b)

            if normal_point.x < a.x or normal_point.x > b.x:
                # Use endpoint of segment as normal point if one can't be found.
                normal_point = b.copy

            distance = future.dist(normal_point)

            # If it beats the record, this should be the target.
            if distance < world_record:
                world_record = distance
                normal_noc = normal_point
                target = normal_point.copy

                # Look at the direction of the line segment in order to
                # seek a little bit ahead of the normal.
                direction = b - a
                direction.set_mag(10)
                target += direction

#        # Step 3: Look a little farther along the path and set a target.
#        b = path.end - path.start
#        b.set_mag(25)  # Set the magnitude to 25 pixels (picked arbitrarily).
#        # Add b to normal_point to find the target 25 pixels ahead on the path.
#        target = normal_point + b
#
#        # Step 4: If off the path, seek target in order to stay on the path.
#        distance = normal_point.dist(future)
#        # If the vehicle is outside the path, seek the target.
#        if distance > path.radius:
#            # Seek target (using seek method created in Example 5.1).
#            self.seek(target)

        # Only if distance is greater than path's radius then bother to steer.
        if world_record > path.radius and target is not None:
            self.seek(target)

        # Draw the debugging stuff.
        if debug:
            fill(127)
            stroke(0)
            line(self.position.x, self.position.y, future.x, future.y)
            circle(future.x, future.y, 4)

            # Draw normal location.
            fill(127)
            stroke(0)
            line(future.x, future.y, normal_noc.x, normal_noc.y)
            circle(normal_noc.x, normal_noc.y, 4)
            stroke(0)
            if world_record > path.radius: fill(255, 0, 0)
            no_stroke()
#            circle(target.x + b.x, target.y + b.y, 8)
            circle(target.x, target.y, 8)

    def get_normal_point(
      self, position: Py5Vector2D, a: Py5Vector2D, b: Py5Vector2D
    ) -> Py5Vector2D:
        """Method to get normal point from position to a line segment (a-b)."""

        vector_a = position - a  # Vector that points from a to position.
        vector_b = b - a         # Vector that points from a to b.

        # Using the dot product for scalar projection.
        vector_b.normalize()  # Normalize b, and ...
        vector_b *= vector_a.dot(vector_b)  # use dot product to set b's length.

        # Finding the normal point along the line segment.
        return a + vector_b  # return normal_point

    def show(self) -> None:
        """The vehicle is a triangle pointing in the direction of velocity."""

        angle = self.velocity.heading
        fill(127)
        stroke(0)
        stroke_weight(2)
        push()
        translate(*self.position)
        rotate(angle)
        begin_shape()
        vertex(self.r * 2, 0)
        vertex(-self.r * 2, -self.r)
        vertex(-self.r * 2, self.r)
        end_shape(CLOSE)
        pop()

    def borders_flow(self) -> None:
        """Wraparound."""

        if self.position.x < -self.r: self.position.x = width + self.r
        if self.position.y < -self.r: self.position.y = height + self.r
        if self.position.x > width + self.r: self.position.x = -self.r
        if self.position.y > height + self.r: self.position.y = -self.r

    def borders_path(self, p: 'PathNoc') -> None:
        """Wraparound."""

        if self.position.x > p.end.x + self.r:
            self.position.x = p.start.x - self.r
            self.position.y = p.start.y + (self.position.y - p.end.y)

    def run(self) -> None:
        self.update()
#        self.borders_flow()
        self.show()
