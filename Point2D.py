class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distance2Origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def distance2OtherPoint(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


if __name__ == "__main__":
    p1 = Point2D(0, 0)
    p2 = Point2D(3, 4)
    p3 = Point2D(4, 3)

    print(p2.distance2Origin())
    print(p3.distance2OtherPoint(p2))
