class Population():
    """A class holding a population of paths."""

    def __init__(self, n_paths=10):

        # Generate a specified number of paths
        self.population_size = n_paths
        self.population = [Path() for i in range(self.population_size)]

        # Path evaluation
        self.fitness = None
        self.normalized_fitness = None
        self.error = None

        # Mating pool and parent selection
        self.mating_pool = []

        # Historical records
        self.historical_fitness = []
        self.historical_error = []
        self.generation = 0

    """Hidden functions for processing fitness and error."""
    # 1. Calculate the T^(-1) for each path
    cohort_evaluate = lambda self: [path.evaluate()[0] for path in self.population]
    # 2. Calculate the error estimate
    cohort_error = lambda self: [path.evaluate()[1] for path in self.population]

    def evaluate(self):

        # Evaluate the fitness, normalized fitness, and error
        self.fitness = [path.evaluate()[0] for path in self.population]
        self.normalized_fitness = [F/max(self.fitness) for F in self.fitness]
        self.error = [path.evaluate()[1] for path in self.population]

        # Save the measurements
        self.historical_fitness.append(self.fitness)
        self.historical_error.append(self.error)


    def assemble_pool(self):
        """Return a mating pool from the existing curves."""
        for i in range(len(self.population)):

            if self.normalized_fitness[i] != 0:
                # If the path is valid
                n = int(self.normalized_fitness[i] * 100)
            else:
                # Else if the path is invalid
                n = 0

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
            self.mating_pool.remove(parent_A)
            self.mating_pool.remove(parent_B)

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
        fig, ax = plt.subplots(figsize=(6,6/GOLDEN),
                               ncols=2, nrows=1)

        # Plot 1: normalized fitness histogram
        ax[0].hist(self.historical_fitness[generation])
        ax[0].set_title('Fitness Scores')
        ax[0].set_xlabel('Score ' + r'($T^{-1})$')
        ax[0].set_ylabel('Frequency')

        # Plot 2: error histogram
        ax[1].hist(self.historical_error[generation])
        ax[1].set_title('Error')
        ax[1].set_xscale('log')
        ax[1].set_xlabel('Error estimate')
        ax[1].set_ylabel('Frequency')

        # Render
        plt.tight_layout()
        plt.show()
