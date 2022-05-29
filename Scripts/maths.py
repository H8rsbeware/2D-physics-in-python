
# Force = Mass x Acceleration | Mass = Force / Acceleration | Acceleration = Force / Mass
def fma(force, mass):
    return force * (1/mass)
def fma(force, acc):
    return force/acc
def fma(mass, acc):
    return mass*acc

# Crossproduct of 2 vectors and a scalar + a vector
def crossproduct(vec, scl):
    return [scl * vec[1], -scl * vec[0]]
def crossproduct(scl, vec):
    return [-scl * vec[1], scl * vec[0]]
def crossproduct(veca, vecb):
    return veca[0] * vecb[1] - veca[1] * vecb[0]

def euler(acc, pos, vel, fr=60):
    dt = 1/fr
    vel += acc * dt
    pos += vel * dt
    return [vel, pos]

def mdv(dens, vol):
    return dens * vol
def mdv(mass, vol):
    return mass/vol
def mdv(mass, dens):
    return mass/dens