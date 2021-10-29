class Partition:
    '''Union-find structure for maintaining disjoint sets'''
    class Position:
        __slots__ = '_container', '_element', '_size', '_parent'

        def __init__(self, container, e) -> None:
            '''create position that is leader of its own group'''
            # reference to Partition instance container
            self._container = container
            self._element = e
            self._size = 1
            # convention for a group leader
            self._parent = self

        def element(self):
            return self._element

    def make_group(self, e):
        '''makes a new group containing element e, and returns its Position'''
        return self.Position(self, e)

    def find(self, p):
        '''finds the group containing p and returns its Position'''
        if p._parent != p:
            p._parent = self.find(p._parent)
        return p._parent

    def union(self, p, q):
        '''merges the groups containing elements p and q (if distinct)'''
        a = self.find(p)
        b = self.find(q)
        if a is not b:
            if a._size > b._size:
                b._parent = a
                a._size += b._size
            else:
                a._parent = b
                b._size += a._size
