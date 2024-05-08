import numpy as np
import random
import math

def distance(point1, point2):
    """
    Computes Euclidean distance between two points.
    """
    return np.linalg.norm(point1 - point2)

def total_distance(path, points):
    """
    Computes the total distance of the path.
    """
    total = 0
    for i in range(len(path) - 1):
        total += distance(points[path[i]], points[path[i + 1]])
    return total

def acceptance_probability(old_cost, new_cost, temperature):
    """
    Calculates the acceptance probability for a new solution.
    """
    if new_cost < old_cost:
        return 1.0
    else:
        return math.exp((old_cost - new_cost) / temperature)

def solve_tsp(points, initial_temperature=1000.0, cooling_rate=0.999, iterations=10000):
    """
    Performs simulated annealing to solve the TSP.
    """
    num_points = len(points)
    current_path = list(range(num_points))
    random.shuffle(current_path)  # Random initial path
    current_cost = total_distance(current_path, points)

    best_path = current_path
    best_cost = current_cost

    temperature = initial_temperature
    for _ in range(iterations):
        # Generate a new candidate solution by randomly swapping two cities
        new_path = current_path.copy()
        index1, index2 = random.sample(range(num_points), 2)
        new_path[index1], new_path[index2] = new_path[index2], new_path[index1]
        new_cost = total_distance(new_path, points)

        # Decide whether to accept the new solution
        if acceptance_probability(current_cost, new_cost, temperature) > random.random():
            current_path = new_path
            current_cost = new_cost

        # Update the best solution if necessary
        if new_cost < best_cost:
            best_path = new_path
            best_cost = new_cost

        # Cool the temperature
        temperature *= cooling_rate

    return best_cost
