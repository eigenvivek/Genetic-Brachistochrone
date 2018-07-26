# Import 3rd party modules
from scipy.interpolate import UnivariateSpline
import numpy as np
from genetics.constants import P1, P2, MUTATION_RATE, BASES
from genetics.curves import f_linear


class DNA():
    """A class holding the function and geneology of a path."""

    def __init__(self, external_DNA=None, mutation_rate=MUTATION_RATE, bases=BASES):

        # Constants
        self.mutation_rate = MUTATION_RATE
        self.bases = BASES

        # Make a path
        self.x = np.linspace(P1[0], P2[0], self.bases)
        if external_DNA == None:
            genes = self.intialize_DNA()
        else:
            genes = external_DNA

        # Assign the x-coords, y-coods, and function as attributes
        self.y = genes[0]
        self.f = genes[1]

    def intialize_DNA(self):
        """Returns a path for the particle to follow."""

        # Make the domain
        y = [P1[1], P2[1]]
        for coord in self.x[1:-1]:
            y.insert(-1, f_linear(coord) + (-2 * np.random.uniform()))

        # Iterpolate the data (x, y) to create the path
        f = UnivariateSpline(self.x, y, k=4, s=0)

        # Return x-coords, y-coords, and interpolated function
        return [y, f]

    def reproduce(self, partner):
        """Returns a genetic offspring of two paths."""

        # Create child's y-path
        child_y = [P1[1], P2[1]]
        for i in range(BASES - 2):
            nucleotide = np.random.choice([self, partner]).y[i + 1]
            child_y.insert(-1, nucleotide)

        # Mutate the child's y-path
        for coord in self.x[1:-1]:
            # If the random float is less than the mutation rate, then that y-coord is random
            if np.random.uniform() < self.mutation_rate:
                child_y[i] = f_linear(coord) + (-10 * np.random.uniform())

        # Return the interpolated child path
        y = child_y
        f = UnivariateSpline(self.x, y, k=4, s=0)

        return [y, f]
