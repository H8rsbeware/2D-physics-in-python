import sys, pygame
BLACK   = (0  ,0  ,0  )
RED     = (255,0  ,0  )


class point:
    def __init__(self, screen, x , y):
        self.screen = screen
        self.x = x
        self.y = y

    def update(self):
        pygame.draw.circle(self.screen, RED, (self.x,self.y), 5)


class line:
    def __init__(self, screen, firstPoint, secondPoint):
        self.screen = screen
        self.firstPoint = firstPoint
        self.secondPoint = secondPoint


    def update(self):
        pygame.draw.line(self.screen, BLACK , (self.firstPoint.x, self.firstPoint.y), (self.secondPoint.x, self.secondPoint.y), 3)



class pair:
    def __init__(self, screen, firstPoint, secondPoint):
        self.screen = screen
        self.size = 2
        self.members = [firstPoint, secondPoint]
        self.line = line(screen, firstPoint, secondPoint)


    def update(self):
        self.line.update()
        self.members[0].update()
        self.members[1].update()

class group:
    def __init__(self, screen, points):
        self.screen = screen
        self.points = points
        self.pairs = []
        self.center = [0,0]
        self.updateCenter()
        self.createPairs()

    def createPairs(self):
        i = 0
        while i < len(self.points) -1:
            p = pair(self.screen, self.points[i], self.points[i+1])
            self.pairs.append(p)
            i += 1
        self.pairs.append(pair(self.screen, self.points[i], self.points[0]))

    def updateCenter(self):
        xt = 0
        yt = 0
        for point in self.points:
            xt += point.x
            yt += point.y
        xt /= len(self.points)
        yt /= len(self.points)
        self.center = [xt, yt]

    def returnPoints(self):
        s = ""
        for point in self.points:
            subS = "( " + str(point.x) + " , " + str(point.y) + " ) "
            s += subS
        return s

    def update(self):
        for pair in self.pairs:
            pair.update()
        self.updateCenter()


class renderGroup:
    def __init__(self, points=[], lines=[], pairs=[], groups=[], btns=[], rigidbodies=[]):
        self.points = points
        self.lines = lines
        self.pairs = pairs
        self.groups = groups
        self.btns = btns
        self.rbs = rigidbodies

    def update(self):
        for point in self.points:
            point.update()
        for line in self.lines:
            line.update()
        for pair in self.pairs:
            pair.update()
        for group in self.groups:
            group.update()
        for btn in self.btns:
            btn.update()
        for rb in self.rbs:
            rb.update()








