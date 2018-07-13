from scipy.interpolate import interp1d
from scipy import integrate
from math import sqrt
from scipy.interpolate import interp1d

"""GLOBAL VARIABLES"""
# Constant for setting figsize
GOLDEN = (1 + 5 ** 0.5) / 2

# DNA constants
MUTATION_RATE = 0.15
BASES = 10

# Make the endpoints P1 and P2
P1 = (0, 0)
P2 = (1, -2)

# Seperate x's and y's
x = [p[0] for p in [P1, P2]]
y = [p[1] for p in [P1, P2]]

# Linearly interpolate the two points
f_linear = interp1d(x, y, kind='linear')

def dt(x): return sqrt(
    (1 + ((P2[1] - P2[1]) / (P2[0] - P1[0]))**2) / (-f_linear(x)))

T = integrate.quad(dt, a=P1[0], b=P2[0], limit=10)[0]
