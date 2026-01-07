from collections import deque

# Function to solve Water Jug Problem
def water_jug_problem(jug1_capacity, jug2_capacity, target):
    
    # Queue for BFS
    queue = deque()
    
    # Set to store visited states
    visited = set()
    
    # Dictionary to store parent state for path reconstruction
    parent = {}
    
    # Initial state (0, 0)
    start_state = (0, 0)
    queue.append(start_state)
    visited.add(start_state)
    parent[start_state] = None
    
    while queue:
        current_state = queue.popleft()
        jug1, jug2 = current_state
        
        # Check if target is achieved
        if jug1 == target or jug2 == target:
            print("\nTarget achieved!\n")
            print_solution_path(parent, current_state)
            return
        
        # List of all possible next states
        possible_states = []
        
        # 1. Fill Jug 1 completely
        possible_states.append((jug1_capacity, jug2))
        
        # 2. Fill Jug 2 completely
        possible_states.append((jug1, jug2_capacity))
        
        # 3. Empty Jug 1
        possible_states.append((0, jug2))
        
        # 4. Empty Jug 2
        possible_states.append((jug1, 0))
        
        # 5. Pour Jug 1 -> Jug 2
        transfer = min(jug1, jug2_capacity - jug2)
        possible_states.append((jug1 - transfer, jug2 + transfer))
        
        # 6. Pour Jug 2 -> Jug 1
        transfer = min(jug2, jug1_capacity - jug1)
        possible_states.append((jug1 + transfer, jug2 - transfer))
        
        # Process all possible states
        for state in possible_states:
            if state not in visited:
                visited.add(state)
                queue.append(state)
                parent[state] = current_state
    
    print("No solution possible.")


# Function to print solution path
def print_solution_path(parent, state):
    path = []
    
    while state is not None:
        path.append(state)
        state = parent[state]
    
    path.reverse()
    
    print("Steps to reach the solution:\n")
    for step in path:
        print(f"Jug1: {step[0]} liters, Jug2: {step[1]} liters")


# ---------------- MAIN PROGRAM ----------------

jug1_capacity = 4
jug2_capacity = 3
target = 2

print("Water Jug Problem Solution")
print(f"Jug 1 Capacity: {jug1_capacity} liters")
print(f"Jug 2 Capacity: {jug2_capacity} liters")
print(f"Target: {target} liters")

water_jug_problem(jug1_capacity, jug2_capacity, target)
