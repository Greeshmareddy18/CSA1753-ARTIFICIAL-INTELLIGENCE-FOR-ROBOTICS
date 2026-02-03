
from collections import deque

def water_jug(jug1, jug2, target):
    visited = set()
    queue = deque([(0, 0)])

    while queue:
        a, b = queue.popleft()

        if a == target or b == target:
            print("Solution reached:", (a, b))
            return

        if (a, b) in visited:
            continue

        visited.add((a, b))

        # Possible operations
        queue.extend([
            (jug1, b),           # Fill jug1
            (a, jug2),           # Fill jug2
            (0, b),              # Empty jug1
            (a, 0),              # Empty jug2
            (min(a + b, jug1), a + b - min(a + b, jug1)),  # Pour jug2 → jug1
            (a + b - min(a + b, jug2), min(a + b, jug2))   # Pour jug1 → jug2
        ])

# Example
water_jug(4, 3, 2)
