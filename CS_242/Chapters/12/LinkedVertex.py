from LinkedEdge import LinkedEdge


class LinkedVertex(object):
    def __init__(self, label: str):
        self.label = label
        self.edgeList: list(LinkedEdge) = list()
        self.mark = False

    def __str__(self):
        return f"{self.label}"

    def __eq__(self, other):
        '''the labels are the same'''
        if self is other:
            return True
        if type(self) != type(other):
            return False
        return self.label == other.label

    def __hash__(self):
        '''supports hashing on a vertex'''
        return hash(self.label)

    def clearMark(self):
        self.mark = False

    def setMark(self):
        self.mark = True

    def isMarked(self):
        return self.mark

    def getLabel(self):
        return self.label

    def setLabel(self, label: str, g):
        '''sets the vertex's label to label'''
        g.vertices.pop(self.label, None)
        g.vertices[label] = self
        self.label = label

    def addEdgeTo(self, toVertex, weight: int = 1):
        newEdge = LinkedEdge(self, toVertex, weight)
        self.edgeList.append(newEdge)

    def getEdgeTo(self, toVertex) -> LinkedEdge or None:
        for edge in self.edgeList:
            if edge.vertex2 == toVertex:
                return edge
        return None

    def incidentEdges(self):
        incidentEdges = list()
        for edge in self.edgeList:
            incidentEdges.append(edge.getToVertex())
        return iter(incidentEdges)

    def neighboringVertices(self):
        ''' returns the neighboring vertices of this vertex'''
        vertices = list()
        for edge in self.edgeList:
            vertices.append(edge.getOtherVertex(self))
        return iter(vertices)

    def removeEdgeTo(self, toVertex):
        ''' returns True if edge exists and is removed, else false'''
        edge = LinkedEdge(self, toVertex)
        if edge in self.edgeList:
            self.edgeList.remove(edge)
            return True
        else:
            return False
