import sys

# Number of cities
N = 4

# Distance matrix
distance = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Variable to store minimum cost
min_cost = sys.maxsize

# List to store best path
best_path = []


# Function to solve TSP using backtracking
def tsp(current_city, visited, current_cost, path):
    global min_cost, best_path

    # If all cities are visited and return to starting city
    if len(visited) == N:
        total_cost = current_cost + distance[current_city][0]
        
        if total_cost < min_cost:
            min_cost = total_cost
            best_path = path + [0]
        return

    # Try visiting all unvisited cities
    for next_city in range(N):
        if next_city not in visited:
            tsp(
                next_city,
                visited + [next_city],
                current_cost + distance[current_city][next_city],
                path + [next_city]
            )


# ---------------- MAIN PROGRAM ----------------

# Starting from city 0
tsp(0, [0], 0, [0])

print("Travelling Salesman Problem Solution\n")
print("Minimum Cost:", min_cost)
print("Best Path:", " -> ".join(map(str, best_path)))
