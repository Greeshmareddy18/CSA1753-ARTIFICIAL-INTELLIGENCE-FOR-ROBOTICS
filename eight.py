from collections import deque

GOAL_STATE = (
    (1, 2, 3),
    (8, 0, 4),
    (7, 6, 5)
)

MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def generate_states(state):
    x, y = find_blank(state)
    states = []
    for dx, dy in MOVES:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            temp = [list(row) for row in state]
            temp[x][y], temp[nx][ny] = temp[nx][ny], temp[x][y]
            states.append(tuple(tuple(row) for row in temp))
    return states

def bfs(start_state):
    queue = deque([(start_state, [start_state])])
    visited = {start_state}

    while queue:
        state, path = queue.popleft()
        if state == GOAL_STATE:
            return path

        for next_state in generate_states(state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [next_state]))
    return None

def print_solution(path):
    for step, state in enumerate(path):
        print("\nStep", step)
        for row in state:
            print(row)

initial_state = (
    (1, 2, 3),
    (8, 4, 0),
    (7, 6, 5)
)

solution = bfs(initial_state)

if solution:
    print("Solution Found!")
    print_solution(solution)
else:
    print("No Solution Exists")
