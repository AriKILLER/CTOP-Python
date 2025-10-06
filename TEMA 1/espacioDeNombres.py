from math import pi as PI
from math import sin as seno

pi = 3.14

def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None

print(sin(pi/2))
print(seno(PI/2))
