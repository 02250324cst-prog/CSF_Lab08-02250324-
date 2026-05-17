from collections import deque
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

def shortest_path(graph, start, goal):
    visited = set()
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        vertex = path[-1]

        if vertex == goal:
            return path

        if vertex not in visited:
            visited.add(vertex)

            for neighbour in graph[vertex]:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

path = shortest_path(graph, 'A', 'F')

print("Shortest path from A to F:")
print(" -> ".join(path))