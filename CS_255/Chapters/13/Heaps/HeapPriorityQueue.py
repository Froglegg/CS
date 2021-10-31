from Heaps.PriorityQueueBase import PriorityQueueBase


class HeapPriorityQueue(PriorityQueueBase):
    '''min-heap using arrays'''

    # private methods, j in parent left and right is len(_data) - 1

    def _parent(self, j):
        return (j-1)//2

    def _left(self, j):
        return 2*j + 1

    def _right(self, j):
        return 2*j+2

    def _has_left(self, j):
        # index beyond end of list?
        return self._left(j) < len(self._data)

    def _has_right(self, j):
        # index beyond end of list?
        return self._right(j) < len(self._data)

    def _swap(self, i, j):
        '''swap elements at i and j in array'''
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            # recur at position of parent
            self._upheap(parent)

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] <= self._data[left]:
                    small_child = right
            if self._data[small_child] <= self._data[j]:
                self._swap(j, small_child)
                # recur at position of small child
                self._downheap(small_child)

    def _heapify(self):
        # start at parent of last leaf
        start = self._parent(len(self)-1)
        # going to and including the root
        for j in range(start, -1, -1):
            self._downheap(j)
    # public methods

    def __init__(self, sourceCollection=()) -> None:
        '''bottom up heap construction via self._heapify if passed a source collection, 
        linear time consturction O(n), which is faster than adding 
        n keys incrementally'''
        self._data = [self._Item(k, v) for k, v in sourceCollection]
        if len(self._data) > 1:
            self._heapify()

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return f"{[f'{i}' for i in self]}"

    def __iter__(self):
        return iter(self._data)

    def add(self, key, value):
        self._data.append(self._Item(key, value))
        # upheap newly added position
        self._upheap(len(self._data)-1)

    def min(self):
        if self.is_empty():
            raise Exception("Priority queue is empty")
        # root item is always min, if we are correctly enforcing the min heap-order property
        item = self._data[0]
        return(item._key, item._value)

    def remove_min(self):
        if self.is_empty():
            raise Exception("Priority queue is empty")
        # put min item at end of array
        self._swap(0, len(self._data)-1)
        # and remove it
        item = self._data.pop()
        # then fix new root
        self._downheap(0)
        return(item._key, item._value)

    def getData(self):
        joined_string = ""
        for i in self._data:
            joined_string += f"{i._value} "
        return joined_string


# heap = HeapPriorityQueue()

# sourceCollection = [(4, "C"), (5, "A"), (6, "Z"), (15, "K"), (9, "F"), (7, "Q"),
#                     (20, "B"), (16, "X"), (25, "J"), (14, "E"), (12, "H"), (11, "S"), (8, "W")]

# for item in sourceCollection:
#     heap.add(item[0], item[1])
# print(heap)

# print(heap.remove_min())
# print(heap.min())
