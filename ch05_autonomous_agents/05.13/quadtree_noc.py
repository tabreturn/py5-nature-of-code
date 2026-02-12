# PY5 IMPORTED MODE CODE

from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float
    data: object = None  # Required for flocking using quadtree (stores Boid).


@dataclass
class Rectangle:
    x: float
    y: float
    w: float
    h: float

    def contains(self, point: 'Point') -> bool:
        return (
          point.x >= self.x - self.w
          and point.x <  self.x + self.w
          and point.y >= self.y - self.h
          and point.y <  self.y + self.h
        )

    def intersects(self, range_: 'Rectangle') -> bool:
        return not (
          range_.x - range_.w > self.x + self.w
          or range_.x + range_.w < self.x - self.w
          or range_.y - range_.h > self.y + self.h
          or range_.y + range_.h < self.y - self.h
        )


class QuadTree:

    def __init__(self, boundary: Rectangle, n: int):
        self.boundary = boundary
        self.capacity = n
        self.points: list[Point] = []
        self.divided = False
        # JS permits attributes dynamically; Python prefers explicit init.
        self.northeast: QuadTree | None = None
        self.northwest: QuadTree | None = None
        self.southeast: QuadTree | None = None
        self.southwest: QuadTree | None = None

    def subdivide(self) -> None:
        x = self.boundary.x
        y = self.boundary.y
        w = self.boundary.w
        h = self.boundary.h
        ne = Rectangle(x + w / 2, y - h / 2, w / 2, h / 2)
        self.northeast = QuadTree(ne, self.capacity)
        nw = Rectangle(x - w / 2, y - h / 2, w / 2, h / 2)
        self.northwest = QuadTree(nw, self.capacity)
        se = Rectangle(x + w / 2, y + h / 2, w / 2, h / 2)
        self.southeast = QuadTree(se, self.capacity)
        sw = Rectangle(x - w / 2, y + h / 2, w / 2, h / 2)
        self.southwest = QuadTree(sw, self.capacity)
        self.divided = True

    def insert(self, point: Point) -> bool:
        if not self.boundary.contains(point):
            return False

        if len(self.points) < self.capacity:
            self.points.append(point)
            return True
        else:
            if not self.divided:
                self.subdivide()

            if self.northeast.insert(point):
                return True
            elif self.northwest.insert(point):
                return True
            elif self.southeast.insert(point):
                return True
            elif self.southwest.insert(point):
                return True

        return False

    def query(
      self, range_: Rectangle, found: list[Point] | None = None
    ) -> list[Point]:
        if found is None:
            found = []

        if not self.boundary.intersects(range_):
            return found

        for p in self.points:
            if range_.contains(p):
                found.append(p)

        if self.divided:
            self.northwest.query(range_, found)
            self.northeast.query(range_, found)
            self.southwest.query(range_, found)
            self.southeast.query(range_, found)

        return found

    def show(self) -> None:
        stroke(175)
        no_fill()
        stroke_weight(1)
        rect_mode(CENTER)
        rect(
          self.boundary.x, self.boundary.y,
          self.boundary.w * 2, self.boundary.h * 2
        )
        for p in self.points:
            stroke(0)
            point(p.x, p.y)

        if self.divided:
            self.northeast.show()
            self.northwest.show()
            self.southeast.show()
            self.southwest.show()
