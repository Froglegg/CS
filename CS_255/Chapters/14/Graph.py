class Graph:
    '''Representation of a simple graph using an adjacency map'''

    class Vertex:
        __slots__ = '_element'

        def __init__(self, x) -> None:
            self._element = x

        def element(self):
            return self._element

        def __hash__(self):
            return hash(id(self))

        def __str__(self):
            return f"{self._element}"

    class Edge:
        __slots__ = '_origin', '_destination', '_weight'

        def __init__(self, u, v, weight) -> None:
            self._origin = u
            self._destination = v
            self._weight = weight

        def endpoints(self):
            return (self._origin, self._destination)

        def opposite(self, v):
            return self._destination if v is self._origin else self._origin

        def weight(self):
            return self._weight

        def __hash__(self):
            return hash((self._origin, self._destination))

        def __str__(self):
            return "{" + f'{self._origin} --> {self._destination}: {self.weight()}' + "}"

    def __init__(self, directed=False) -> None:
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing

    def __iter__(self):
        return iter([i for i in self._outgoing.keys()])

    def __getitem__(self, key):
        return self._outgoing[key]

    def is_directed(self):
        return self._incoming is not self._outgoing

    def vertex_count(self):
        return len(self._outgoing)

    def vertices(self):
        return self._outgoing.keys()

    def edge_count(self):
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        return total if self.is_directed() else total // 2

    def edges(self):
        result = set()
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())
        return result

    def get_edge(self, u, v):
        return self._outgoing[u].get(v)

    def degree(self, v, outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])

    def incident_edges(self, v, outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            yield edge

    def insert_vertex(self, x=None):
        v = self.Vertex(x)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}
        return v

    def insert_edge(self, u, v, weight=None):
        e = self.Edge(u, v, weight)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e


# test = Graph()
# for i in range(10):
#     test.insert_vertex(i)

# vertexList = [i for i in test]
# test.insert_edge(vertexList[0], vertexList[1])

# print(test.edges())
# print(test.edge_count())

# print(test.get_edge(vertexList[0], vertexList[1]))

# print(test.vertices())
# test.insert_edge(1, 2)

# print(test.incident_edges(2))
