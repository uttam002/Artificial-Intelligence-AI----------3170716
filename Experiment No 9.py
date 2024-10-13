import random

# Define a function to create an individual chromosome (a list of genes)
def create_individual(length):
    # Each individual will have genes represented as 0 or 1 (binary representation)
    return [random.randint(0, 1) for _ in range(length)]

# Define the fitness function (to evaluate how good an individual is)
def fitness(individual):
    # In this example, fitness is simply the sum of the individual's genes
    return sum(individual)

# Selection function: Select two individuals from the population based on their fitness (higher fitness = higher chance of being selected)
def selection(population, fitness_fn):
    # Select individuals using a weighted random choice based on fitness
    total_fitness = sum(fitness_fn(individual) for individual in population)
    chosen = random.choices(
        population,
        weights=[fitness_fn(individual) / total_fitness for individual in population],
        k=2
    )
    return chosen

# Crossover function: Create a new individual by combining parts of two parent individuals
def crossover(parent1, parent2):
    # Randomly select a crossover point
    point = random.randint(1, len(parent1) - 1)
    # Create a child by combining the first part of parent1 with the second part of parent2
    child = parent1[:point] + parent2[point:]
    return child

# Mutation function: Randomly change a gene in an individual
def mutate(individual, mutation_rate=0.01):
    # For each gene, there's a mutation_rate chance of it being flipped (0 to 1 or 1 to 0)
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = 1 - individual[i]  # Flip the gene
    return individual

# Genetic Algorithm function
def genetic_algorithm(population_size, gene_length, generations, mutation_rate):
    # Initialize the population (list of individuals)
    population = [create_individual(gene_length) for _ in range(population_size)]
    
    # Iterate through the number of generations
    for generation in range(generations):
        # Create a new population through selection, crossover, and mutation
        new_population = []
        for _ in range(population_size // 2):  # We will create population_size individuals
            parent1, parent2 = selection(population, fitness)
            child1 = crossover(parent1, parent2)
            child2 = crossover(parent2, parent1)
            new_population.append(mutate(child1, mutation_rate))
            new_population.append(mutate(child2, mutation_rate))
        
        # Replace the old population with the new one
        population = new_population
    
    # Return the best individual from the final population
    best_individual = max(population, key=fitness)
    return best_individual, fitness(best_individual)

# Parameters for the genetic algorithm
population_size = 10    # Number of individuals in the population
gene_length = 8         # Number of genes in each individual
generations = 50        # Number of generations to evolve
mutation_rate = 0.01    # Probability of a gene being mutated

# Run the genetic algorithm
best_solution, best_fitness = genetic_algorithm(population_size, gene_length, generations, mutation_rate)

# Print the best solution and its fitness score
print("Best Individual: ", best_solution)
print("Best Fitness: ", best_fitness)
