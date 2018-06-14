"""IMPORT STATEMENTS"""
# 3rd party modules
import numpy as np

# Local moduless
from population import Population

"""GLOBAL VARIABLES"""
# Constant for setting figsize
GOLDEN = (1 + 5 ** 0.5) / 2

# DNA constants
MUTATION_RATE = 0.1
BASES = 20

# Make the endpoints P1 and P2
P1 = (0, 0)
P2 = (1, np.random.uniform(-1,0))

#test
if __name__ == '__main__':
    pop = Population()
    pop.population[0].visualize()
