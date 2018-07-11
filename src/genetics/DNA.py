# Import 3rd party modules
from scipy.interpolate import UnivariateSpline
from scipy.interpolate import interp1d
import numpy as np
from genetics.constants import P1, P2, MUTATION_RATE, BASES


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

        # Seperate x's and y's
        x = [p[0] for p in [P1, P2]]
        y = [p[1] for p in [P1, P2]]

        # Linearly interpolate the two points
        f = interp1d(x, y, kind='linear')

        # Make the domain
        x = np.linspace(0, 1, self.bases)
        y = []

        # Fill in the range
        for coord in x:

            # Bound the curve at the two points p1 and p2
            if (coord == min(x)):
                y.append(P1[1])
            elif (coord == max(x)):
                y.append(P2[1])

            # For every point excluding the boundary, add uniform noise
            else:
                y.append(f(coord) + np.random.uniform(-2, f(coord)))

        # Iterpolate the data (x, y) to create the path
        f2 = UnivariateSpline(x, y, k=4, s=0)

        # Return x-coords, y-coords, and interpolated function
        return x, y, f2, None, None


    def reproduction(self, partner):
        """Returns a genetic offspring of two paths."""

        # Create empty array for the child's y-path
        child_y = [0] * (len(self.y) - 2)

        # Create the child's y-path
        for i in range(len(child_y)):
            if i < int(round((len(self.y)-1)/2)):
                child_y[i] = self.y[i+1]
            else:
                child_y[i] = partner.y[i+1]

            if 1 == 2:
                for i in range(len(child_y)):
                    # If the random float is less than the mutation rate, then that y-coord is random
                    if np.random.uniform(0, 1) < self.mutation_rate:
                        child_y[i] = np.random.uniform(-2, -0.1)

        child_y.insert(0, 0)
        child_y.insert(-1, self.y[-1])

        # Mutate the child's y-path
        for i in range(len(child_y)):
            # If the random float is less than the mutation rate, then that y-coord is random
            if np.random.uniform(0, 1) < self.mutation_rate:
                child_y[i] = np.random.uniform(0, -0.1)

        # Return the interpolated child path
        x = np.linspace(0, 1, self.bases )
        y = child_y
        f2 = UnivariateSpline(x, y, k=4, s=0)
        child = [x, y, f2, self, partner]

        return child
