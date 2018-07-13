"""IMPORT STATEMENTS"""
# 3rd party modules
import numpy as np

# Local moduless
from genetics.population import Population

# test
if __name__ == '__main__':

    pop = Population(250)

    for generation in range(100):
        pop.next_generation()

        print("Generation: {} \nMax fitness: {} | Average fitness: {}".format(
              generation, pop.generation_best.time, np.mean(pop.fitness))
              )
        pop.generation += 1
