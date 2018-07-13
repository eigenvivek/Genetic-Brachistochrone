from genetics.population import Population
import numpy as np
pop = Population(25)
for i in range(30):
    pop.next_generation()
    print(np.mean(pop.fitness))
    pop.generation_best.visualize()
