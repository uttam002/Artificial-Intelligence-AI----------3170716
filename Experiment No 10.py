import random

# Define a simple objective function (fitness) that we want to maximize
def fitness_function(x):
    # Example: A simple quadratic function y = -(x-5)^2 + 10, maximized at x=5
    return -(x - 5) ** 2 + 10

# Hill Climbing Algorithm
def hill_climbing(starting_point, step_size, max_iterations):
    # Start with the current point being the starting point
    current_point = starting_point
    current_fitness = fitness_function(current_point)
    
    # Loop through a maximum number of iterations
    for iteration in range(max_iterations):
        # Generate a new point by moving in a random direction
        new_point = current_point + random.choice([-step_size, step_size])
        new_fitness = fitness_function(new_point)
        
        # If the new point is better, move to that point
        if new_fitness > current_fitness:
            current_point = new_point
            current_fitness = new_fitness
            
        # Print the current point and fitness value for each iteration
        print(f"Iteration {iteration}: Point = {current_point}, Fitness = {current_fitness}")
    
    # Return the best point found
    return current_point, current_fitness

# Parameters for the Hill Climbing algorithm
starting_point = random.uniform(0, 10)  # Starting point between 0 and 10
step_size = 0.1                         # Step size for each move
max_iterations = 100                    # Maximum number of iterations

# Run the Hill Climbing algorithm
best_point, best_fitness = hill_climbing(starting_point, step_size, max_iterations)

# Print the best point and fitness value
print("Best Point: ", best_point)
print("Best Fitness: ", best_fitness)
