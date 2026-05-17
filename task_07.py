graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

vertices = len(graph)

edges = 0
for vertex in graph:
    edges += len(graph[vertex])

edges = edges // 2  

print("Number of vertices:", vertices)
print("Number of edges:", edges)

print("\nDegree of each vertex:")

for vertex in graph:
    print(vertex + ":", len(graph[vertex]))

visited = set()

def dfs(vertex):
    visited.add(vertex)

    for neighbour in graph[vertex]:
        if neighbour not in visited:
            dfs(neighbour)

dfs('A')

if len(visited) == len(graph):
    print("\nThe graph is connected.")
else:
    print("\nThe graph is not connected.")

print("The graph is undirected.")