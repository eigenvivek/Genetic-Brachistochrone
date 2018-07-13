import matplotlib.pyplot as plt
import numpy as np

# Import path
from genetics.path import Path
from genetics.constants import GOLDEN


class Population():
    """A class holding a population of paths."""

    def __init__(self, n_paths=10):

        # Generate a specified number of paths
        self.population_size = n_paths
        self.population = [Path() for i in range(self.population_size)]

        # Historical records
        self.historical_fitness = []
        self.historical_error = []
        self.generation = 0

    def evaluate(self):

        # Path evaluation
        self.fitness = []
        self.error = []

        for path in self.population:
            path.evaluate()
            self.fitness.append(path.time)
            self.error.append(path.err)

        # Save the measurements
        self.historical_fitness.append(self.fitness)
        self.historical_error.append(self.error)

    def assemble_pool(self):
        """Return a mating pool from the existing curves."""

        self.mating_pool = []
        max_time = max(self.fitness)
        best_time = np.inf

        for i in range(self.population_size):

            if self.population[i].is_valid:
                if self.population[i].time < best_time:
                    best_time = self.population[i].time
                    self.generation_best = self.population[i]
                n = int(max_time - self.population[i].time)
            else:
                continue

            # Add n copies of the path to the mating pool
            for j in range(n):
                self.mating_pool.append(self.population[i])

    def generate_offspring(self):
        """Return new curve from 2 offspring in the mating pool."""

        # Array for holding offspring paths
        new_paths = [0] * self.population_size

        for i in range(self.population_size):

            # Randomly pick the y-coords from two parents
            parent_A = np.random.choice(self.mating_pool)
            parent_B = np.random.choice(self.mating_pool)

            # Remove parent_A and parent_B from mating pool
            # self.mating_pool.remove(parent_A)
            # self.mating_pool.remove(parent_B)

            # Create child using crossover function
            child = parent_A.dna.reproduction(parent_B.dna)

            # Add new rocket to next generation
            new_paths[i] = Path(external_DNA=child)

        self.population = new_paths

    def next_generation(self):
        self.evaluate()
        self.assemble_pool()
        self.generate_offspring()
        self.generation += 1

    def hist_fitness_and_error(self, generation):
        """Return histograms of error and fitness."""
        fig, ax = plt.subplots(figsize=(6, 6 / GOLDEN),
                               ncols=2, nrows=1)

        # Plot 1: normalized fitness histogram
        ax[0].hist(self.historical_fitness[generation])
        ax[0].set_title('Fitness Scores')
        ax[0].set_xlabel('Cost ' + r'($T$)')
        ax[0].set_ylabel('Frequency')

        # Plot 2: error histogram
        ax[1].hist(self.historical_error[generation])
        ax[1].set_title('Error')
        ax[1].set_xscale('log')
        ax[1].set_xlabel('Error estimate')
        ax[1].set_ylabel('Frequency')

        # Render
        plt.suptitle(f'Generation {int(self.generation-1)}')
        plt.tight_layout()
        plt.show()
