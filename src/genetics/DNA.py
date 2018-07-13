# Import 3rd party modules
from scipy.interpolate import UnivariateSpline
import numpy as np
from genetics.constants import P1, P2, MUTATION_RATE, BASES, f_linear


class DNA():
    """A class holding the function and geneology of a path."""

    def __init__(self, external_genes=None, mutation_rate=MUTATION_RATE, bases=BASES):

        # Constants
        self.mutation_rate = MUTATION_RATE
        self.bases = BASES

        # Make a path
        if external_genes == None:
            path = self.generate_path()
        else:
            path = external_genes

        # Assign the x-coords, y-coods, and function as attributes
        self.x = path[0]
        self.y = path[1]
        self.f2 = path[2]

        # Geneology
        self.parent_A = path[3]
        self.parent_B = path[4]

    def generate_path(self):
        """Returns a path for the particle to follow."""

        # Make the domain
        x = np.linspace(P1[0], P2[0], self.bases)
        y = [P1[1]] + [f_linear(coord) + (-10 * np.random.uniform())
                       for coord in x[1:-1]] + [P2[1]]

        # Iterpolate the data (x, y) to create the path
        f2 = UnivariateSpline(x, y, k=4, s=0)

        # Return x-coords, y-coords, and interpolated function
        return x, y, f2, None, None

    def reproduction(self, partner):
        """Returns a genetic offspring of two paths."""

        # Create child's y-path
        child_y = [P1[1], P2[1]]
        for i in range(BASES - 2):
            if i < int(round((BASES - 2) / 2)):
                child_y.insert(-1, self.y[i + 1])
            else:
                child_y.insert(-1, partner.y[i + 1])

        # Mutate the child's y-path
        for coord in self.x[1:-1]:
            # If the random float is less than the mutation rate, then that y-coord is random
            if np.random.uniform() < self.mutation_rate:
                child_y[i] = f_linear(coord) + (-5 * np.random.uniform())

        # Return the interpolated child path
        x = np.linspace(0, 1, self.bases)
        y = child_y
        f2 = UnivariateSpline(x, y, k=4, s=0)
        child = [x, y, f2, self, partner]

        return child
