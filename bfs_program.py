from collections import deque

# Function to perform BFS traversal
def bfs(graph, start_node):
    
    # Queue for BFS
    queue = deque()
    
    # Set to keep track of visited nodes
    visited = set()
    
    # Add start node to queue and visited set
    queue.append(start_node)
    visited.add(start_node)
    
    print("BFS Traversal Order:")
    
    while queue:
        # Remove the front node from queue
        current_node = queue.popleft()
        print(current_node, end=" ")
        
        # Visit all the adjacent nodes
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


# ---------------- MAIN PROGRAM ----------------

# Graph represented as adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Starting node
start = 'A'

print("Breadth-First Search (BFS) Implementation\n")
bfs(graph, start)
