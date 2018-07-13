# Import 3rd party modules
import numpy as np
from math import sqrt
from scipy import integrate
import matplotlib.pyplot as plt

from genetics.DNA import DNA
from genetics.constants import P1, P2


class Path():
    """A class holding the attributes of an individual path."""

    def __init__(self, external_DNA=None):
        """Initialize the class."""

        # Make a path
        if external_DNA == None:
            self.dna = DNA()
        else:
            self.dna = DNA(external_DNA)

    def evaluate(self):
        """Time required to traverse a path and error estimation."""

        # Differential time as a function of x
        def dt(x):
            return sqrt((1 + self.dna.f.derivative()(x)**2) / (-self.dna.f(x)))

        # Integrate dt over the domain [0,1]
        try:
            T = integrate.quad(dt, a=P1[0], b=P2[0], limit=100)
            self.time = T[0]
            self.err = T[1]
            self.is_valid = True
        except:
            self.time = -1
            self.err = 0
            self.is_valid = False
