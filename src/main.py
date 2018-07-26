"""IMPORT STATEMENTS"""
# 3rd party modules
import numpy as np

# Local moduless
from genetics.population import Population
# from genetics.visualize import visualize

# test
if __name__ == '__main__':

    pop = Population(100)

    for generation in range(100):
        pop.next_generation()
        # visualize(pop.generation_best)

        print("Generation: {} \nMax fitness: {} | Average fitness: {}".format(
              generation, pop.generation_best.time, np.mean(pop.fitness))
              )

        # pop.hist_fitness_and_error()
