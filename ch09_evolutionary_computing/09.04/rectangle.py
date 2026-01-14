class Rectangle:
    """Re-implementing java.awt.Rectangle (from Processing) for p5.js"""

    def __init__(self, x: float, y: float, w: float, h: float):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.center = (self.x + self.width / 2, self.y + self.height / 2)

    def contains(self, px: float, py: float) -> bool:
        return (
          px > self.x
          and px < self.x + self.width
          and py > self.y
          and py < self.y + self.height
        )