"""IMPORT STATEMENTS"""
# 3rd party modules
import numpy as np

# Local moduless
from genetics.population import Population

#test
if __name__ == '__main__':

    pop = Population(250)

    for generation in range(100):
        pop.evaluate()

        if generation % 5 == 0:
            max_f = round(max(pop.fitness), 3)
            avg_f = round(np.average(pop.fitness), 3)
            print("Generation: {} \nMax fitness: {} | Average fitness: {}".format(
                  generation, max_f, avg_f)
            )


        pop.assemble_pool()
        pop.generate_offspring()
        pop.generation += 1
