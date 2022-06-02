import env

# Force = Mass x Acceleration | Mass = Force / Acceleration | Acceleration = Force / Mass
def fma(mass, acc):
    return mass*acc
def afm(force, mass):
    return force * (1/mass)
def mfa(force, acc):
    return force/acc


# Crossproduct of 2 vectors and a scalar + a vector
def crossproduct(veca, vecb):
    return veca[0] * vecb[1] - veca[1] * vecb[0]
def crossproductvs(vec, scl):
    return [scl * vec[1], -scl * vec[0]]
def crossproductsv(scl, vec):
    return [-scl * vec[1], scl * vec[0]]

# Eulers rule for velocity and position over time
def euler(acc, pos, vel, fr=60):
    dt = 1/fr
    vel += acc * dt
    pos += vel * dt
    return [vel, pos]

# Mass = density * volume and the rearragement
def mdv(dens, vol):
    return dens * vol
def dmv(mass, vol):
    return mass/vol
def vmd(mass, dens):
    return mass/dens

# box collider check in a env.rendergroup
def checkColliders(rendergroup):
    # Gets length of the group, makes sure it above 1, and starts an index
    rbs = rendergroup.rbs
    i = len(rbs)
    j = 0
    if i <= 1:
        return
    # [tl,tr,br,bl]
    # Checks crossover between lines (currently only 3 lines (-top)) of the box colliders
    while (j < i):
        r = rbs[j].boxcollider.points
        tl = r[0]
        tr = r[1]
        br = r[2]
        bl = r[3]

        w = 0
        while (w < i):
            if not w == j:
                nr = rbs[w].boxcollider.points
                rtl = nr[0]
                rtr = nr[1]
                rbr = nr[2]
                rbl = nr[3]

                if (rtl.x < br.x < rtr.x) and (rtl.y < br.y < rbl.y):
                    return [rbs[j],rbs[w]]
                if (rtl.x < bl.x < rtr.x) and (rtr.y < bl.y < rbr.y):
                    return [rbs[j],rbs[w]]
            w += 1
        j += 1

# Gets collider overlap between two groups and calculates the force required to correct for it
def getColliderAdjustments(screen, a, b):

    ag = a.pairs
    bg = b.pairs

    for pair in ag:
        q = pair.members[0]
        qr = pair.members[1]
        r = minusVector(qr,q)

        for cpair in bg:
            p = cpair.members[0]
            ps = cpair.members[1]
            s = minusVector(ps,p)

            if p is not q or qr is not ps:
                if crossproduct((minusVector(q,p)), r) == 0 and crossproduct(r,s) == 0:
                    t0 = dot(minusVector(q,p), r) / dot(r, r)
                    t1 = dot((minusVector(plusVector(q,s), p)),r) / dot(r,r)
                    print(str(t0) + ", " + str(t1))

                elif crossproduct(r,s) != 0:
                    u = (crossproduct((minusVector(q,p)), r)) / (crossproduct(r,s))
                    dist = minusVector(plusVector(q , multiplyVector(u , s)), q)
                    print(dist)

                    a.force.x = a.mass * dist[0]
                    a.force.y = a.mass * dist[1]

                if u is 0:
                    return u

    return False

def minusVector(a, b):
    e = 0
    if isinstance(a, env.point) and isinstance(b, env.point):
        e = [a.x - b.x, a.y -b.y]
    elif isinstance(a, env.point):
        e = [a.x - b[0], a.y - b[1]]
    elif isinstance(b, env.point):
        e = [a[0] - b.x, a[1] - b.y]
    else:
        e = [a[0] - b[0], a[1] - b[1]]
    return e

def plusVector(a, b):
    e = 0
    if isinstance(a, env.point) and isinstance(b, env.point):
        e = [a.x + b.x, a.y +b.y]
    elif isinstance(a, env.point):
        e = [a.x + b[0], a.y + b[1]]
    elif isinstance(b, env.point):
        e = [a[0] + b.x, a[1] + b.y]
    else:
        e = [a[0] + b[0], a[1] + b[1]]
    return e

def multiplyVector(a,b):
    if isinstance(a, env.point) and isinstance(b, env.point):
        e = [a.x * b.x, a.y * b.y]
        return e
    elif isinstance(b, env.point):
        e = [b[0] * a, b[1] * a]
        return e
    return [0,0]

# Dot product
def dot(a,b):
    return sum([a[i][0]*b[i] for i in range(len(b))])