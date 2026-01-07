# Function to perform DFS traversal
def dfs(graph, node, visited):
    
    # Mark the current node as visited
    visited.add(node)
    print(node, end=" ")
    
    # Recur for all the adjacent nodes
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


# ---------------- MAIN PROGRAM ----------------

# Graph represented using adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Set to keep track of visited nodes
visited = set()

print("Depth-First Search (DFS) Implementation\n")
print("DFS Traversal Order:")

# Starting DFS from node 'A'
dfs(graph, 'A', visited)
