from Collections.ArrayBag import ArrayBag
from AbstractSet import AbstractSet


class ArraySet(AbstractSet, ArrayBag):
    ''' array based implementation of a set'''

    def __init__(self, sourceCollection=None) -> None:
        ArrayBag.__init__(self, sourceCollection)

    def add(self, item):
        ''' adds item to the set if its not in the set'''
        if not item in self:
            ArrayBag.add(self, item)
