"""IMPORT STATEMENTS"""
# 3rd party modules
import numpy as np

# Local moduless
from genetics.population import Population
from genetics.visualize import visualize
from genetics.curves import T_cycloid

# test
if __name__ == '__main__':

    pop = Population(100)

    for generation in range(100):
        pop.next_generation()
        if generation % 10 == 0:
            visualize(pop.generation_best)

        print("Generation: {} \nBest time: {:.3f} | Average time: {:.3f} | Cycloid time: {:.3f}".format(
              generation, pop.generation_best.time, np.mean(pop.fitness), T_cycloid)
              )

        # pop.hist_fitness_and_error()
