import numpy as np
from scipy import integrate
from scipy.interpolate import interp1d
from scipy.optimize import newton
import matplotlib.pyplot as plt

from genetics.constants import P1, P2

# Linearly interpolate the two points
def linear():
    x = [p[0] for p in [P1, P2]]
    y = [p[1] for p in [P1, P2]]
    f_linear = interp1d(x, y, kind='linear')
    def dt(x):
        return np.sqrt((1 + ((P2[1] - P1[1]) / (P2[0] - P1[0]))**2) / (-f_linear(x)))
    T = integrate.quad(dt, a=P1[0], b=P2[0], limit=10)[0]
    return f_linear, T

def cycloid():
    """Return the path of Brachistochrone curve from (0,0) to (x2, y2).

    The Brachistochrone curve is the path down which a bead will fall without
    friction between two points in the least time (an arc of a cycloid).
    It is returned as an array of N values of (x,y) between (0,0) and (x2,y2).

    """

    # First find theta2 from (x2, y2) numerically (by Newton-Rapheson).
    f = lambda theta: -P2[1]/P2[0] - (1-np.cos(theta))/(theta-np.sin(theta))
    theta2 = newton(f, np.pi/2)

    # The radius of the circle generating the cycloid.
    R = -P2[1] / (1 - np.cos(theta2))

    theta = np.linspace(0, theta2, 100)
    x = R * (theta - np.sin(theta))
    y = R * (1 - np.cos(theta))

    # The time of travel
    T = theta2 * np.sqrt(R)
    return x, -y, T

"""Constants"""
f_linear, T_linear = linear()
x, y, T_cycloid = cycloid()
