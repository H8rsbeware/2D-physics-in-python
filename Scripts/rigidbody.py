import sys, pygame, env

class rigidbody(env.group):
    def __init__(self, screen, points, mass, acceleration=(0, -9.81)):
        env.group.__init__(self, screen, points)
        self.screen = screen
        self.points = points
        self.pairs = []
        self.mass = mass
        self.acceleration = acceleration
        self.velocity = 0,0
        self.force = [0, 0]
        self.boxcollider = self.getRectCollider()
        self.center = self.getCenter()

        self.updateForce(acceleration)
        self.createPairs()

        self.colliderview = False
        self.centerview = False

    def update(self):
        self.updateForce(self.acceleration)

        if self.mass is not 0:
            for point in self.points:
                point.x += self.force[0]
                point.y -= self.force[1]

        for pair in self.pairs:
            pair.update()

        self.boxcollider = self.getRectCollider()
        self.center = self.getCenter()
        if self.colliderview:
            for pair in self.boxcollider.pairs:
                pair.update()
        if self.centerview:
            self.center.update()


    def updateForce(self, acceleration):
        self.force = self.mass * acceleration

    #def gravity(self):

    def getCenter(self):
        rect = self.boxcollider
        l,h = self.boxcollider.points[0], self.boxcollider.points[2]

        dx = h.x - l.x
        dy = h.y - l.y
        dx = l.x + dx/2
        dy = l.y + dy/2
        p = env.point(self.screen,dx,dy)
        return p

    def getRectCollider(self):
        r,d = 0,0
        for point in self.points:
            if point.y > d:
                d = point.y
            if point.x > r:
                r = point.x
        l,u = r,d
        for point in self.points:
            if point.y < u:
                u = point.y
            if point.x < l:
                l = point.x

        tl = env.point(self.screen, l, u)
        tr = env.point(self.screen, r, u)
        br = env.point(self.screen, r, d)
        bl = env.point(self.screen, l, d)
        rect = env.group(self.screen, [tl,tr,br,bl])
        return rect

    def showColliders(self, colliders, center):
        self.colliderview = colliders
        self.centerview = center











