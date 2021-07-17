from LinkedList.node import TwoWayNode
from LinkedList.AbstractList import AbstractList


class LinkedList(AbstractList):

    def __init__(self, sourceCollection=None) -> None:
        '''uses a circular structure with a "dummy" sentinel node
           the empty TwoWayNode instance self.head is the sentinel node... 
           the cursor will set its head NOT to the head node, which is the dummy sentinel, but to the next node, which is the first node containing data (if it exists)
           when the cursor cycles around to the dummy head sentinel node, the iterators loop terminates.
        '''

        self.head = TwoWayNode()

        self.head.previous = self.head.next = self.head
        super().__init__(sourceCollection=sourceCollection)

    # accessors
    def __iter__(self):
        cursor = self.head.next
        while cursor != self.head:
            yield cursor.data
            cursor = cursor.next

    # helpers
    def getNode(self, i):
        '''Helper method that returns a pointer to the node at position i'''

        # constant time access to head node
        if i == len(self):
            return self.head

        # or last data node
        if i == len(self) - 1:
            return self.head.previous

        probe = self.head.next
        while i > 0:
            probe = probe.next
            i -= 1
        return probe

    def __getitem__(self, i):
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        return self.getNode(i).data

    # mutators

    def __setitem__(self, i, item):
        '''replaces element at i with item'''
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range!")
        self.getNode(i).data = item

    def insert(self, i, item):
        if i < 0:
            i = 0
        elif i > len(self):
            i = len(self)
        theNode = self.getNode(i)
        newNode = TwoWayNode(item, theNode.previous, theNode)
        theNode.previous.next = newNode
        theNode.previous = newNode
        self.size += 1
        self.incModCount()

    def pop(self, i=None):
        # return last data node if index not specified
        if i == None:
            i = len(self) - 1

        if i < 0 or i > len(self) - 1:
            raise IndexError("List index out of range")

        popped = self.getNode(i)

        popped.previous.next = popped.next

        popped.next.previous = popped.previous

        self.size -= 1

        self.incModCount()

        return popped.data

    def replace(self, i, item):
        '''do not increment mod count with replace method'''
        if i < 0:
            i = 0
        elif i > len(self):
            i = len(self)

        theNode = self.getNode(i)
        newNode = TwoWayNode(item, theNode.previous, theNode.next)

        # break link of the node being replaced
        theNode.previous.next = newNode
        theNode.next.previous = newNode
        return theNode.data
