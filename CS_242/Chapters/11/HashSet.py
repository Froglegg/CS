from Collections.AbstractCollection import AbstractCollection
from Collections.Node import Node
from Collections.Arrays import Array

from AbstractSet import AbstractSet


class HashSet(AbstractSet, AbstractCollection):
    '''
    a hashing implementation of a set
    uses "chaining" collision-processing strategy 

    '''
    DEFAULT_CAPACITY = 3

    def __init__(self, sourceCollection=None, capacity=None) -> None:
        if capacity is None:
            self.capacity = HashSet.DEFAULT_CAPACITY
        else:
            self.capacity = capacity

        self.items = Array(self.capacity)
        self.foundNode = self.priorNode = None
        self.index = -1
        AbstractCollection.__init__(self, sourceCollection)

    # accessors
    def __contains__(self, item):
        '''return true if item is in the set or false otherwise '''
        self.index = abs(hash(item)) % len(self.items)
        self.priorNode = None
        self.foundNode = self.items[self.index]

        while self.foundNode != None:
            if self.foundNode.data == item:
                return True
            else:
                self.priorNode = self.foundNode
                self.foundNode = self.foundNode.next
        return False

    def __str__(self):
        return "{" + f"{', '.join(map(str, self))}" + "}"

    def __iter__(self):
        ''' iterates over array of linked lists, returns each item in each bucket'''
        for node in self.items:

            while node != None:
                # yield node data to caller
                yield node.data
                node = node.next

    def clear(self):
        self.size = 0
        self.foundNode = self.priorNode = None

        self.index -= 1
        self.items = Array(HashSet.DEFAULT_CAPACITY)

    def add(self, item):
        if not item in self:
            newNode = Node(item, self.items[self.index])
            self.items[self.index] = newNode
            self.size += 1

    def remove(self, item):
        if item in self:
            value = self.foundNode.data

            if self.priorNode:
                self.priorNode.next = self.foundNode.next

            self.foundNode = None
            self.items[self.index] = None
            self.size -= 1
            return value
        else:
            raise KeyError("Item not in set!")
