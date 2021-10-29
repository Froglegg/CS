from Graph import Graph


def BFS(g: Graph, s: Graph.Vertex, discovered: dict):
    '''Perform BFS of the undiscovered portion of the graph starting at veretex s
    discovered is a dict mapping each vertex to the edge that was used to discover it during the BFS 
    s should be mapped to None prior to the call, eg, result = {vertices[0]: None}
    Newly discovered vertices will be added to the dictionary as a result
    '''
    level = [s]
    while len(level) > 0:
        next_level = []
        u: Graph.Vertex
        for u in level:
            for edge in g.incident_edges(u):
                v = edge.opposite(u)
                if v not in discovered:
                    discovered[v] = edge
                    next_level.append(v)
        level = next_level


def construct_path(u, v, discovered):

    path = []
    if v in discovered:
        # we build list from vertices v to u and then reverse it at the end
        path.append(v)
        walk = v

        while walk is not u:

            e = discovered[walk]
            parent = e.opposite(walk)
            path.append(parent)
            walk = parent
        path.reverse()
    return path


def BFS_complete(g):
    '''perform BFS for entire graph and return a forest as a dictionary'''
    forest = {}
    for u in g.vertices():
        if u not in forest:
            forest[u] = None
            BFS(g, u, forest)
    return forest


testGraph = Graph(directed=True)

for letter in ["a", "b", "c", "d", "e"]:
    testGraph.insert_vertex(letter)

vertices = [v for v in testGraph.vertices()]
# print([f"{i}" for i in vertices])

testGraph.insert_edge(vertices[0], vertices[1], 2)
testGraph.insert_edge(vertices[1], vertices[2], 8)
testGraph.insert_edge(vertices[2], vertices[3], 3)
testGraph.insert_edge(vertices[3], vertices[4], 11)

result = {vertices[0]: None}

BFS(testGraph, vertices[0], result)

for i in result.items():
    print(i[0], i[1])

path = construct_path(vertices[2], vertices[4], result)

print([f'{i}' for i in path])

graphForest = BFS_complete(testGraph)

for entry in graphForest.items():
    print(entry[0], entry[1])
