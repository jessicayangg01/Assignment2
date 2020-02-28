# calculating volume

# Import math function
from math import pi


# Calculates cube volume
def cube_volume(a):
    volume = pow(a, 3)
    # returns calculated value
    return volume


# Calculates pyramid volume
def pyramid_volume(b, h):
    volume = b*b*h/3
    # returns calculated value
    return volume


# calculates ellipsoid volume
def ellipsoid_volume(r1, r2, r3):
    volume = 4/3*pi*r1*r2*r3
    # returns calculated value
    return volume
