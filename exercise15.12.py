class Line:
    def __init__(self, slope, yIntercept):
        self.slope = slope
        self.y = yIntercept

    def findIntercept(self, other):
        x = (self.slope - other.slope) / (other.yIntercept - self.yIntercept)
        y = self.slope * x + self.yIntercept
        return Point(x, y)

    def findPerpendicularBisector(self, point1, point2):
        slope = -1 / self.slope
        midpoint, anotherPoint = Point((point1.x + point2.x) / 2, (point1.y + point2.y) / 2), Point(
            (point1.x + point2.x) / 2, (point1.y + point2.y) / 2)
        dx = 1
        dy = slope
        anotherPoint.move(dx, dy)
        return midpoint.getLineTo(anotherPoint)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def getCoordinates(self):
        return self.x, self.y

    def distanceFromPoint(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def reflectX(self):
        return Point(-self.x, self.y)

    def slopeFromPoint(self, other):
        return (self.y - other.y) / (self.x - other.x)

    def slopeFromOrigin(self):
        return self.slopeFromPoint(Point(0, 0))

    def getLineTo(self, other):
        slope = self.slopeFromPoint(other)
        yIntercept = self.y - slope * self.x
        return Line(slope, yIntercept)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def getCircle(self, point1, point2):
        line1 = self.getLineTo(point1)
        line2 = self.getLineTo(point2)
        perpendicularBisector1 = line1.findPerpendicularBisector(self, point1)
        perpendicularBisector2 = line2.findPerpendicularBisector(self, point2)
        center = perpendicularBisector1.findIntercept(perpendicularBisector2)
        radius = self.distanceFromPoint(center)
        return center, radius


class SMS_Store:
    # each message is a list in the form [hasBeenViewed, fromNumber, timeArrived, textOfSMS]
    def __init__(self):
        self.messageList = []

    def addNewArrival(self, fromNumber, timeArrived, textOfSMS):
        self.messageList.append([False, fromNumber, timeArrived, textOfSMS])

    def messageCount(self):
        return len(self.messageList)

    def getUnreadIndexes(self):
        unreadList = []
        for message in range(len(self.messageList)):
            if not self.messageList[message][0]:
                unreadList.append(message)
        return unreadList

    def getMessage(self, index):
        try:
            self.messageList[index][0] = True
            return self.messageList[index][1:]
        except:
            return None

    def delete(self, index):
        self.messageList.pop(index)

    def clear(self):
        self.messageList = []
