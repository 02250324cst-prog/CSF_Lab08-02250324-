graph = {}
def add_vertex(vertex):
    if vertex not in graph:
        graph[vertex] = []

def add_edge(v1, v2):
    graph[v1].append(v2)
    graph[v2].append(v1)

def display_graph():
    print("Graph Representation:")
    
    for vertex in graph:
        print(vertex, "->", graph[vertex])

add_vertex('A')
add_vertex('B')
add_vertex('C')
add_vertex('D')

add_edge('A', 'B')
add_edge('A', 'C')
add_edge('B', 'D')

display_graph()