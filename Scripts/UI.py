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


    def updateAll(self):
        self.line.update()
        self.members[0].update()
        self.members[1].update()


