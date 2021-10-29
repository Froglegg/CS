from Graph import Graph
from Heaps.Heap import AdaptableHeapPriorityQueue


def Prim_Jarnik(g: Graph):
    '''
    Compute a MST of weighted graph g

    Returns a list of edges that comprise the MST (in arbitrary order)
    '''

    d = {}
    tree = []
    pq = AdaptableHeapPriorityQueue()
    pqLocator = {}

    # for each v in g, add an entry to the pq, with the
    # source having distance 0 and all others having infinity
    v: Graph.Vertex
    for v in g.vertices():
        # this is the first node
        if len(d) == 0:
            d[v] = 0
        else:
            d[v] = float('inf')
        pqLocator[v] = pq.add(d[v], (v, None))
    while not pq.is_empty():
        key, value = pq.remove_min()
        u, edge = value
        del pqLocator[u]
        if edge is not None:
            tree.append(edge)
        for link in g.incident_edges(u):
            v = link.opposite(u)
            if v in pqLocator:
                weight = link.weight()
                if weight < d[v]:
                    d[v] = weight
                    pq.update(pqLocator[v], d[v], (v, link))
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

MST = Prim_Jarnik(testGraph)
for i in MST:
    print(i)
