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

class btn:
    def __init__(self, screen, x, y, width, height, outline, solid, toggleOutline, toggleSolid, face=1):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.outline = pygame.image.load(outline)
        self.solid = pygame.image.load(solid)
        self.tOutline = pygame.image.load(toggleOutline)
        self.tSolid = pygame.image.load(toggleSolid)
        self.face = face
        self.hover = False

    def update(self):
        mx,my = pygame.mouse.get_pos()
        if (mx < self.x+ self.width/2) & (mx > self.x- self.width/2) & (my < self.y + self.height/2) & (my > self.y- self.height/2):
            self.hover = True
            if self.face == 1:
                self.screen.blit(self.tSolid, self.tSolid.get_rect())
            if self.face == 0:
                self.screen.blit(self.solid, self.solid.get_rect())

        else:
            if self.face == 1:
                self.screen.blit(self.tOutline, self.tOutline.get_rect())
            if self.face == 0:
                self.screen.blit(self.outline, self.outline.get_rect())
            self.hover = False







