from collections import deque

# Total number of missionaries and cannibals
TOTAL_M = 3
TOTAL_C = 3

# Function to check if a state is valid
def is_valid_state(m_left, c_left):
    m_right = TOTAL_M - m_left
    c_right = TOTAL_C - c_left

    # Missionaries or cannibals count should not be negative or exceed total
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False

    # Missionaries should not be outnumbered
    if (m_left > 0 and m_left < c_left):
        return False
    if (m_right > 0 and m_right < c_right):
        return False

    return True


# Function to generate all possible next states
def get_next_states(state):
    m_left, c_left, boat = state
    next_states = []

    # Possible boat moves (1 or 2 people)
    moves = [(1,0), (0,1), (2,0), (0,2), (1,1)]

    for m, c in moves:
        if boat == 0:  # Boat on left bank → move to right
            new_state = (m_left - m, c_left - c, 1)
        else:          # Boat on right bank → move to left
            new_state = (m_left + m, c_left + c, 0)

        if is_valid_state(new_state[0], new_state[1]):
            next_states.append(new_state)

    return next_states


# BFS to solve the problem
def solve_missionaries_cannibals():
    start_state = (3, 3, 0)   # All on left bank
    goal_state = (0, 0, 1)    # All on right bank

    queue = deque()
    queue.append(start_state)

    visited = set()
    visited.add(start_state)

    parent = {}
    parent[start_state] = None

    while queue:
        current_state = queue.popleft()

        if current_state == goal_state:
            print("\nSolution Found!\n")
            print_solution(parent, current_state)
            return

        for next_state in get_next_states(current_state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append(next_state)
                parent[next_state] = current_state

    print("No solution exists.")


# Function to print solution path
def print_solution(parent, state):
    path = []

    while state is not None:
        path.append(state)
        state = parent[state]

    path.reverse()

    print("Steps to solve the problem:\n")
    for step in path:
        side = "Left Bank" if step[2] == 0 else "Right Bank"
        print(f"Missionaries Left: {step[0]}, Cannibals Left: {step[1]}, Boat: {side}")


# ---------------- MAIN PROGRAM ----------------

print("Missionaries and Cannibals Problem")
print("Using Breadth-First Search (BFS)\n")

solve_missionaries_cannibals()
