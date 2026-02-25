# https://natureofcode.com/physics-libraries/#revolute-constraints


# Constraint connects body to fixed (x, y) with a length: 0 and stiffness: 1.
options = {
  'body_a': self.anchor_body,
  'body_b': self.bob_body,
  'length': self.len_,
}

# Create the constraint and add it to the world.
constraint = Matter.Constraint.create(options);
Composite.add(engine.world, constraint)

# Create a body at a given position with width and height.
body = Bodies.rectangle(x, y, w, h)
self.space.add(engine.world, body)