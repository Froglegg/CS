class LinkedQueue():
    '''FIFO queue implementation using a singly-linked list for storage'''
    class _Node:
        '''lightweight, private class for storing a singly linked node'''
        # streamline memory usage for Nodes with slots instead of dict
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self, sourceCollection=None) -> None:
        self._tail = None
        self._size = 0
        if sourceCollection:
            for element in sourceCollection:
                self.enqueue(element)

    def __len__(self):
        return self._size

    def __iter__(self):
        cursor = self._tail._next
        itemCount = len(self)
        while itemCount > 0:
            # yeild to the caller
            yield cursor._element
            cursor = cursor._next
            itemCount -= 1

    def __str__(self):
        return f"{[i for i in self]}"

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Exception('queue is empty')
        head = self._tail._next
        return head._element

    def dequeue(self):
        if self.is_empty():
            raise Exception('queue is empty')
        oldhead = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = oldhead._next
        self._size -= 1
        return oldhead._element

    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            # initialize circularly
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def rotate(self):
        '''rotate front element to back of queue '''
        if self._size > 0:
            # old head becomes new tail
            self._tail = self._tail._next
