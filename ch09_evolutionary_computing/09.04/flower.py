from dna import DNA
from py5 import (
  CENTER, color, cos, ellipse, fill, floor, line, no_fill, no_stroke, pop, push,
  remap, sin, stroke, stroke_weight, rect, rect_mode, text, text_align,
  translate, TWO_PI
)
from rectangle import Rectangle


class Flower:
    """Flower phenotype."""

    def __init__(self, dna: DNA, x: float, y: float):
        self.dna = dna  # Flower DNA.
        self.fitness = 1  # How fit is the flower?
        self.rollover_on = False  # Are we rolling over this flower?
        self.x, self.y = x, y  # Position on screen.
        self.w, self.h = 70, 140  # Size of square enclosing flower.
        self.bounding_box = Rectangle(
            self.x - self.w / 2, self.y - self.h / 2, self.w, self.h
        )

    def show(self):
        """Display the flower."""
        # DNA values such as petal color, petal size, and number of petals.
        genes = self.dna.genes
        # Set RGB range from 0 to 1 with color_mode() and use map() as needed.
        petal_color = color(genes[0], genes[1], genes[2], genes[3])
        petal_size = remap(genes[4], 0, 1, 4, 24)
        petal_count = floor(remap(genes[5], 0, 1, 2, 16))
        center_color = color(genes[6], genes[7], genes[8])
        center_size = remap(genes[9], 0, 1, 24, 48)
        stem_color = color(genes[10], genes[11], genes[12])
        stem_length = remap(genes[13], 0, 1, 50, 100)

        push()
        translate(self.x, self.y)
        # Draw the bounding box.
        fill(0, 0.25) if self.rollover_on else no_fill()
        stroke(0)
        stroke_weight(0.5)
        rect_mode(CENTER)
        rect(0, 0, self.w, self.h)
        # Draw the stem.
        translate(0, self.h / 2 - stem_length)
        stroke(stem_color)
        stroke_weight(4)
        line(0, 0, 0, stem_length)
        no_stroke()
        # Draw the petals.
        fill(petal_color)
        for i in range(petal_count):
            angle = remap(i, 0, petal_count, 0, TWO_PI)
            x = petal_size * cos(angle)
            y = petal_size * sin(angle)
            ellipse(x, y, petal_size, petal_size)
        # Draw the center.
        fill(center_color)
        ellipse(0, 0, center_size, center_size)
        pop()

        # Display fitness value.
        text_align(CENTER)
        fill(0) if self.rollover_on else fill(0.25)
        text(str(floor(self.fitness)), self.x, self.y + 90)

    def rollover(self, mx: float, my: float) -> None:
        """Increment fitness if mouse is rolling over flower."""
        if self.bounding_box.contains(mx, my):
            self.rollover_on = True
            self.fitness += 0.25
        else:
            self.rollover_on = False
