import math

a = -9.8

def timeC(u, s):
    if (s > 0):
        s = s*-1
    t = ((-2*u) + math.sqrt((4*u*u)-(4*a*s*-2)))/(2*a)
    if t < 0:
        t = t*-1
    return t