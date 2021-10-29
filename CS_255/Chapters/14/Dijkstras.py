from Graph import Graph
from Heaps.Heap import AdaptableHeapPriorityQueue


def Dijsktras(g: Graph, src: Graph.Vertex):
    '''
    Compute shortest path distance from source src to reachable vertices of g
    Graph g can be undirected or directed, but must be weighted such that edge.element returns a numeric weight

    return dictionary mapping each reachable vertex to its distance from src
    '''
    d = {}
    cloud = {}
    pq = AdaptableHeapPriorityQueue()
    pqLocator = {}

    # for each vertex v of the graph, add an entry to the priority queue, with
    # the src vertex key having distance 0 and all others having infinite distance
    for v in g.vertices():
        if v is src:
            d[v] = 0
        else:
            # syntax for positive infinity
            d[v] = float('inf')
        # save locator for future updates
        pqLocator[v] = pq.add(d[v], v)

    while not pq.is_empty():
        key, u = pq.remove_min()
        # its correct d[u] value
        cloud[u] = key
        # u is no longere in pq
        del pqLocator[u]
        # typecasting e to graph edge
        e: Graph.Edge
        # outgoing edges (u,v)
        for e in g.incident_edges(u):
            v = e.opposite(u)
            if v not in cloud:
                # perform relaxation step on edge (u,v)
                weight = e.weight()
                # better path to v?
                if d[u] + weight < d[v]:
                    # update distance
                    d[v] = d[u] + weight
                    # update pq entry
                    pq.update(pqLocator[v], d[v], v)
    # cloud only includes reachable values
    return cloud


def shortestPathTree(g: Graph, s: Graph.Vertex, d: dict):
    '''
    Reconstruct shortest path tree rooted at vertex s, given distance map d.

    Return tree as a map from each reachable vertex v (other than s) to the edge
    e=(u,v), that is used to reach v from its parent u in the tree

    '''
    tree = {}
    v: Graph.Vertex
    for v in d:
        if v is not s:
            # consider INCOMING edges
            e: Graph.Edge
            for e in g.incident_edges(v, False):
                u = e.opposite(v)
                weight = e.weight()
                if d[v] == d[u] + weight:
                    tree[v] = e
    return tree


testGraph = Graph(directed=True)

for letter in ["a", "b", "c", "d", "e"]:
    testGraph.insert_vertex(letter)

vertices = [v for v in testGraph.vertices()]
# print([f"{i}" for i in vertices])

testGraph.insert_edge(vertices[0], vertices[1], 2)
testGraph.insert_edge(vertices[1], vertices[2], 8)
testGraph.insert_edge(vertices[2], vertices[3], 3)
testGraph.insert_edge(vertices[3], vertices[4], 11)
# testGraph.insert_edge(vertices[0], vertices[3], 1)

root = vertices[0]
shortest_path_dict = Dijsktras(testGraph, root)

print(f"All shortest paths from {root} a la Dijkstra's")
for entry in shortest_path_dict.items():
    print(f"From {root} to {entry[0]}: {entry[1]}")

tree = shortestPathTree(testGraph, root, shortest_path_dict)
print('')
print(f"shortest path tree with {root} as root: ")
for i in tree.items():
    print(i[0], i[1])
