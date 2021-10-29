from Graph import Graph
from Heaps.Heap import HeapPriorityQueue
from Partition import Partition


def Kruskal(g: Graph):
    '''
    Compute MST via Kruskal's algorithm 

    Return a list of edges that comprise the MST 

    The elements of the graph's edges are assumed to be weights
    '''
    # list of edges in a spanning tree
    tree = []
    # entries in pq are edges in G, with weights as keys
    pq = HeapPriorityQueue()
    # keeps track of forest clusters
    forest = Partition()
    # map each node to its Partition entry
    position = {}

    v: Graph.Vertex
    for v in g.vertices():
        position[v] = forest.make_group(v)

    e: Graph.Edge
    for e in g.edges():
        pq.add(e.weight(), e)

    size = g.vertex_count()

    # while tree not spanning and unprocessed edges remain
    while len(tree) != size-1 and not pq.is_empty():
        edge: Graph.Edge
        weight, edge = pq.remove_min()
        u, v = edge.endpoints()

        a = forest.find(position[u])
        b = forest.find(position[v])
        if a != b:
            tree.append(edge)
            forest.union(a, b)
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

MST = Kruskal(testGraph)
for i in MST:
    print(i)
