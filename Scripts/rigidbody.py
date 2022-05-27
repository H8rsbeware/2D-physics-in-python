import sys, pygame, UI

class rigidbody(UI.group):
    def __init__(self, screen, points, mass, acceleration=(0, -9.81)):
        UI.group.__init__(self, screen, points)
        self.screen = screen
        self.points = points
        self.pairs = []
        self.center = [0, 0]
        self.mass = mass
        self.acceleration = acceleration
        self.force = [0, 0]


        self.updateForce(acceleration)
        self.createPairs()
        self.updateCenter()

    def update(self):
        self.updateForce(self.acceleration)
        for point in self.points:
            point.x += self.force[0]
            point.y -= self.force[1]

        for pair in self.pairs:
            pair.update()
        self.updateCenter()



    def updateForce(self, acceleration):
        self.force = self.mass * acceleration

