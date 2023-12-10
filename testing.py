import random

def generate_random_points(num_points, x_range=(0, 100), y_range=(0, 100)):
    """
    Generate random coordinate points within the specified ranges.

    Parameters:
    - num_points (int): Number of points to generate.
    - x_range (tuple): Range for x-coordinate, default is (0, 10).
    - y_range (tuple): Range for y-coordinate, default is (0, 10).

    Returns:
    - List of tuples representing random coordinate points.
    """
    points = [(round(random.uniform(x_range[0], x_range[1])), round(random.uniform(y_range[0], y_range[1]))) for _ in range(num_points)]
    return points

# Example: Generate 5 random points in the range [0, 10] for both x and y coordinates
random_points = generate_random_points(95)
print(random_points)
