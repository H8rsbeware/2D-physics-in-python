import sys, pygame

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
