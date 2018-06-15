# Import 3rd party modules
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from math import sqrt
from scipy.interpolate import interp1d

# Import local modules
import DNA
from globals import P1, P2

class Path():
    """A class holding the attributes of an individual path."""

    def __init__(self, external_DNA=None):
        """Initialize the class."""

        # Make a path
        if external_DNA == None:
            self.dna = DNA.DNA()
        else:
            self.dna = DNA.DNA(external_DNA)


    def evaluate(self):
        """Returns the inverse time required to traverse a path and error estimation."""

        # Differential time as a function of x
        dt = lambda x: sqrt( (1 + self.dna.f2.derivative()(x)**2) / (-self.dna.f2(x)) )

        # Integrate dt over the domain [0,1]
        try:
            T = integrate.quad(dt, a=0, b=1, limit=10)
            T_inv = T[0] ** (-1)
            err = T[1]
            self.valid = True

        except:
            # Exception occurs if f(x)>0 for x in [0,1]
            T = np.inf
            T_inv = T ** (-1)
            err = 0
            self.valid = False

        return T_inv, err

    def visualize(self, title=None):
        """Returns a plot of the interpolated path."""

        # A more granular domain
        xnew = np.linspace(0,1,1001)

        # Plot setup
        plt.plot(self.dna.x, self.dna.y, 'o')                 # Original points
        plt.plot(xnew, self.dna.f2(xnew), '--', label='Path') # Interpolated path
        plt.plot(xnew, [0]*len(xnew), label='Cutoff')         # Cutoff line at y=0
        plt.plot(xnew, interp1d([P1[0],P2[0]],
                                [P1[1],P2[1]],
                                kind='linear')(xnew))

        # Plot titles
        if title != None:
            plt.title(title)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()

        # Render
        plt.show()
