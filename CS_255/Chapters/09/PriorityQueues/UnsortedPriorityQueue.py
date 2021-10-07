from PositionalList import PositionalList
from PriorityQueueBase import PriorityQueueBase


class UnsortedPriorityQueue(PriorityQueueBase):
    '''a min-oriented priority queue implemented with an unsorted list'''

    def __init__(self) -> None:
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)

    def _find_min(self):
        if self.is_empty():
            raise Exception("Priority Queue is empty.")
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)
        return small

    def add(self, key, value):
        self._data.add_last(self._Item(key, value))

    def min(self):
        p = self._find_min()
        item: self._Item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        p = self._find_min()
        item: self._Item = self._data.delete(p)
        return (item._key, item._value)


pq = UnsortedPriorityQueue()
for i in range(9, 0, -1):
    pq.add(i, i)

for i in pq:
    print(i)
