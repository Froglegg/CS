from Collections.AbstractCollection import AbstractCollection
from LinkedVertex import LinkedVertex
from LinkedEdge import LinkedEdge
from tabulate import tabulate


class LinkedDirectedGraph(AbstractCollection):

    def __init__(self, sourceCollection=None) -> None:
        self.edgeCount = 0
        self.toEdges = []
        self.vertices: dict(LinkedVertex) = dict()

        AbstractCollection.__init__(self, sourceCollection)

    # def __str__(self):
    #     return f"{[[f'{edge}' for edge in v.neighboringVertices()] for v in self.vertices]}"

    def __contains__(self, label):
        return self.containsVertex(label)

    def clear(self):
        self.__init__()

    def clearEdgeMarks(self):
        for vertex in self.vertices.values():
            for e in vertex.edgeList:
                e.clearMark()

    def clearVertexMarks(self):
        for vertex in self.vertices.values():
            vertex.clearMark()

    def isEmpty(self):
        return len(self.vertices) == 0

    def sizeEdges(self):
        return self.edgeCount

    def sizeVertices(self):
        return self.size

    # Function to print adjacency list representation of a graph

    def printGraph(self):
        for vertex in self.vertices.values():
            print(vertex, end=": ")
            # print current vertex and all its neighboring vertices
            for neighborVertex in vertex.neighboringVertices():
                print(f"({vertex} —> {neighborVertex}) ", end="")
            print()

    def add(self, label: str):
        self.addVertex(label)

    def containsVertex(self, label) -> bool:
        return label in self.vertices

    def getVertex(self, label):
        if self.containsVertex(label):
            return self.vertices[label]
        raise KeyError("That vertex doesn't exist!")

    def addVertex(self, label):
        ''' adds a vertex with the given label to the graph'''
        self.vertices[label] = LinkedVertex(label)
        self.size += 1

    def removeVertex(self, label: str) -> bool:
        '''returns True if vertex was removed, false otherwise'''
        removedVertex: LinkedVertex = self.vertices.pop(label, None)
        if removedVertex is None:
            return False
        # examine all other vertices to remove edges
        # directed at the removed vertex
        for vertex in self.getVertices():
            if vertex.removeEdgeTo(removedVertex):
                self.edgeCount -= 1
        # examine al edges from the removed vertex to others
        for _ in removedVertex.incidentEdges():
            self.edgeCount -= 1

        self.size -= 1
        return True

    def containsEdge(self, edge: LinkedEdge) -> bool:
        for v in self.vertices.values():
            if edge in v.edgeList:
                return True
        return False

    def addEdge(self, fromLabel: str, toLabel: str, weight: int) -> None:
        '''connects the vertices with and edge with the given weight'''
        fromVertex = self.getVertex(fromLabel)
        toVertex = self.getVertex(toLabel)

        fromVertex.addEdgeTo(toVertex, weight)
        self.toEdges.append(toLabel)
        self.edgeCount += 1

    def getEdge(self, fromLabel: str, toLabel: str) -> LinkedEdge or None:
        ''' returns the edge containing the two vertices, or None if no edge exists'''
        fromVertex = self.getVertex(fromLabel)
        toVertex = self.getVertex(toLabel)
        return fromVertex.getEdgeTo(toVertex)

    def removeEdge(self, fromLabel: str, toLabel: str):
        ''' returns true if edge remove, or else false'''
        fromVertex = self.getVertex(fromLabel)
        toVertex = self.getVertex(toLabel)
        edgeRemovedFlag = fromVertex.removeEdgeTo(toVertex)
        if edgeRemovedFlag:
            self.edgeCount -= 1
        return edgeRemovedFlag

    def edges(self):
        edges = set()
        for v in self.vertices.values():
            for edge in v.edgeList:
                edges.add(edge)
        return iter(edges)

    def getVertices(self):
        return iter(self.vertices.values())

    def incidentEdges(self, label):
        return self.vertices[label].incidentEdges()

    def neighboringVertices(self, label):
        return self.vertices[label].neighboringVertices()

    def shortestPaths(self, sourceVertex: LinkedVertex) -> list:
        ''' runs Djikstra's algorithm to find shortest path from source vertex to every vertex in graph'''
        results = []
        included = {}

        INFINITY = "-"

        def addWithInfinity(a, b):
            if a == INFINITY or b == INFINITY:
                return INFINITY
            else:
                return a + b

        def init(results, included):
            for idx, vertex in enumerate(self.vertices.values()):

                edge: LinkedEdge = sourceVertex.getEdgeTo(vertex)
                results.append([idx, vertex.getLabel(), 0, None])

                if vertex == sourceVertex:
                    results[idx][2] = 0
                    results[idx][3] = None
                    included.update({vertex.getLabel(): True})

                elif edge:
                    results[idx][2] = edge.getWeight()
                    results[idx][3] = sourceVertex.getLabel()
                    included.update({vertex.getLabel(): False})

                else:
                    results[idx][2] = INFINITY
                    results[idx][3] = None
                    included.update({vertex.getLabel(): False})

            return {"results": results, "included": included}

        def compute(results, included):

            # while not all vertices are included in the list
            while False in included.values():
                # iterate through our results rows
                for row in results:

                    label = row[1]
                    weight = row[2]
                    parent = row[3]

                    isIncluded: bool = included[label]

                    # if it's not included in the list and has a weight, include it
                    if not isIncluded and type(weight) is int:
                        included[label] = True
                    else:
                        # else, iterate through the results again, find each other vertex that is not included
                        # and whether they have an edge to the current vertext

                        for row2 in results:
                            label2 = row2[1]
                            weight2 = row2[2]

                            isIncluded2: bool = included[label2]

                            fromVertex = self.vertices[label]
                            toVertex = self.vertices[label2]

                            if isIncluded2 == False:

                                edge: LinkedEdge = fromVertex.getEdgeTo(
                                    toVertex)

                                if edge:

                                    newDistance = addWithInfinity(
                                        weight, edge.getWeight())

                                    if weight2 is INFINITY or newDistance < weight2:
                                        row2[2] = newDistance
                                        row2[3] = label
                                elif label2 not in self.toEdges:
                                    row2[2] = 0

            return results

        initialize = init(results, included)

        computed = compute(initialize["results"], initialize["included"])

        title = f"Set of shortest paths for origin {sourceVertex.getLabel()}"

        table = tabulate(computed, headers=[
                         "Index", "Vertex", "Distance", "Parent"], tablefmt="github", numalign="left")
        return {"title": title, "table": table, "computed": computed}


g = LinkedDirectedGraph(["A", "B", "C", "D", "E"])

edgeList = [["C", "A", 3], ["A", "C", 4], ["B", "C", 2],
            ["A", "B", 5], ["C", "B", 8], ["C", "D", 4]]

for edge in edgeList:
    g.addEdge(edge[0], edge[1], edge[2])

g.printGraph()

test: LinkedVertex = g.getVertex("A")
shortestPath = g.shortestPaths(test)

print(shortestPath["title"])
print(shortestPath["table"])
