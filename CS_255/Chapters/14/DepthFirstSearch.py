from Graph import Graph


def DFS(graph: Graph, vertex: Graph.Vertex, discovered: dict):
    '''
    Perform DFS of the undiscovered portion of Graph starting at Vertex
    discovered is a dictionary mapping each vertex to the edge that was used to discover it during DFS
    s should be mapped to None prior to the call
    Newly discovered vertices will be added to the dictionary as a result
    '''
    edge: Graph.Edge
    # for every outgoing edge in vertex
    for edge in graph.incident_edges(vertex):

        adjacentVertex: Graph.Vertex = edge.opposite(vertex)
        # if the adjacent vertex has not been visited
        if adjacentVertex not in discovered:
            # edge is the tree edgee that discovered the adjacentVertex
            discovered[adjacentVertex] = edge
            # recursively explore from adjacentVertex
            DFS(graph, adjacentVertex, discovered)


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


def DFS_complete(g):
    '''perform DFS for entire graph and return a forest as a dictionary'''
    forest = {}
    for u in g.vertices():
        if u not in forest:
            forest[u] = None
            DFS(g, u, forest)
    return forest


testGraph = Graph(directed=True)

for letter in ["a", "b", "c", "d", "e"]:
    testGraph.insert_vertex(letter)

vertices = [v for v in testGraph.vertices()]
# print([f"{i}" for i in vertices])

testGraph.insert_edge(vertices[0], vertices[1])
testGraph.insert_edge(vertices[1], vertices[2])
testGraph.insert_edge(vertices[2], vertices[3])
testGraph.insert_edge(vertices[3], vertices[4])


# result = {vertices[0]: None}

# DFS(testGraph, vertices[0], result)

# for entry in result.items():
#     print(entry[0], entry[1])

# path = construct_path(vertices[0], vertices[4], result)

# print([f'{i}' for i in path])

graphForest = DFS_complete(testGraph)

for entry in graphForest.items():
    print(entry[0], entry[1])
