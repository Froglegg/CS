from _typeshed import Self
from HeapPriorityQueue import HeapPriorityQueue


class AdaptableHeapPriorityQueue(HeapPriorityQueue):
    ''' a Locator based priority queue implemented with a binary heap'''
    # nested Locator class
    class Locator(HeapPriorityQueue._Item):
        '''token for locating an entry of the priority queue'''
        __slots__ = "_index"

        def __init__(self, k, v, j) -> None:
            super().__init__(k, v)
            self._index = j
    # private methods

    def _swap(self, i, j):
        '''override swap to record new indices'''
        super()._swap(i, j)
        # reset locator indices, post-swap
        self._data[i]._index = i
        self._data[j]._index = j

    def _bubble(self, j):
        if j > 0 and self._data[j] < self._data[self._parent(j)]:
            self._upheap(j)
        else:
            self._downheap(j)

    # public methods
    def add(self, key, value):
        # init locator index
        token = self.Locator(key, value, len(self._data))
        self._data.append(token)
        self._upheap(len(self._data)-1)
        return token

    def update(self, loc, newkey, newval):
        j = loc._index
        if not (0 <= j < len(self and self._data[j] is loc)):
            raise ValueError("Invalid locator")
        loc._key = newkey
        loc._value = newval
        self._bubble(j)

    def remove(self, loc):
        j = loc._index
        if not (0 <= j < len(self and self._data[j] is loc)):
            raise ValueError("Invalid locator")
        # if item at last position, just remove it
        if j == len(self - 1):
            self._data.pop()
        else:
            # swap item to last position
            self._swap(j, len(self)-1)
            # remove it from the list
            self._data.pop()
            # fix item displaced by swap
            self._bubble(j)
        return (loc._key, loc._value)
