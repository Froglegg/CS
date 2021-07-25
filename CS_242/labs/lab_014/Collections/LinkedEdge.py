
class LinkedEdge(object):

    def __init__(self, fromVertex, toVertex, weight: int = 1) -> None:
        super().__init__()
        self.vertex1 = fromVertex
        self.vertex2 = toVertex
        self.weight = weight
        self.mark = False

    def __hash__(self):
        '''supports hashing on a edge'''
        return hash(str(self))

    def __eq__(self, other):
        '''two edges are equal if they connect to the vertices'''
        if self is other:
            return True
        if type(self) != type(other):
            return False
        return self.vertex1 == other.vertex1 and self.vertex2 == other.vertex2 and self.weight == other.weight

    def __str__(self):
        return f"{self.vertex1.label}>{self.vertex2.label}:{self.weight}"

    def clearMark(self):
        self.mark = False

    def setMark(self):
        self.mark = True

    def isMarked(self):
        return self.mark

    def getWeight(self):
        return self.weight

    def setWeight(self, weight):
        self.weight = weight

    def getOtherVertex(self, vertex):
        if self.vertex1 == vertex:
            return self.vertex2
        elif self.vertex2 == vertex:
            return self.vertex1
        return None

    def getToVertex(self):
        return self.vertex2
