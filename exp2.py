from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}  # adjacency list representation

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    # Recursive DFS
    def dfs_recursive(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=" ")

        for neighbor in self.graph.get(start, []):
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited)

    # Iterative DFS using stack
    def dfs_iterative(self, start):
        visited = set()
        stack = [start]

        while stack:
            node = stack.pop()
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                # add neighbors in reverse to maintain order
                stack.extend(reversed(self.graph.get(node, [])))

    # BFS using queue
    def bfs(self, start):
        visited = set([start])
        queue = deque([start])

        while queue:
            node = queue.popleft()
            print(node, end=" ")
            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)


# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("DFS (Recursive):")
g.dfs_recursive(2)
print("\nDFS (Iterative):")
g.dfs_iterative(2)
print("\nBFS:")
g.bfs(2)
