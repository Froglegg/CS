from Collections.Arrays import Array
from Collections.Node import Node


from Collections.AbstractCollection import AbstractCollection


class Entry(object):
    ''' represents dictionary entry, supports comparisons by key'''

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str(self.key) + ": " + str(self.value)

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.key == other.key

    def __lt__(self, other):
        if type(self) != type(other):
            return False
        return self.key < other .key

    def __le__(self, other):
        if type(self) != type(other):
            return False
        return self.key <= other.key


class HashDict(AbstractCollection):
    '''hash based dictionary'''
    DEFAULT_CAPACITY = 9

    def __init__(self, keys=None, values=None, capacity=None):
        AbstractCollection.__init__(self)
        if capacity is None:
            self.capacity = HashDict.DEFAULT_CAPACITY
        else:
            self.capacity = capacity

        self.array = Array(self.capacity)
        self.foundNode = self.priorNode = None
        self.index = -1
        if keys and values:
            valuesIter = iter(values)
            for key in keys:
                self[key] = next(valuesIter)

    def __contains__(self, key):
        '''return true if item is in the set or false otherwise '''
        self.index = abs(hash(key)) % len(self.array)
        self.priorNode = None
        self.foundNode = self.array[self.index]

        while self.foundNode != None:
            if self.foundNode.data.key == key:
                return True
            else:
                self.priorNode = self.foundNode
                self.foundNode = self.foundNode.next
        return False

    def __str__(self):
        return "{" + f"{', '.join(map(str, self))}" + "}"

    def __iter__(self):
        ''' iterates over array of linked lists, returns each item in each bucket'''
        for node in self.array:
            while node != None:
                # yield node data to caller
                yield node.data
                node = node.next

    def __getitem__(self, key):
        if key in self:

            return self.foundNode.data.value
        else:
            raise KeyError("Missing: " + str(key))

    def __setitem__(self, key, value):
        if key in self:
            self.foundNode.data.value = value
        else:
            newNode = Node(Entry(key, value), self.array[self.index])
            self.array[self.index] = newNode
            self.size += 1

    def __add__(self, other):
        result = type(self)(self.keys(), self.values())

        for key in other.keys():
     
            result[key] = other[key]
        return result

    def __eq__(self, other):
        if self is other:
            return True
        if type(self) != type(other) or len(self) != len(other):
            return False
        for key in self:
            if not key in other:
                return False
        return True

    def keys(self):
        return map(lambda key: key.key, self)

    def values(self):
        return map(lambda key: self[key.key], self)

    def entries(self):
        return map(lambda key: Entry(key.key, self[key.key]), self)

    def get(self, key, defaultValue=None):
        ''' returns value assocaited with key if present, else None'''
        return self[key] or defaultValue

    def pop(self, key, defaultValue=None):
        if key in self:
            value = self.foundNode.data

            if self.priorNode:
                self.priorNode.next = self.foundNode.next

            self.foundNode = None
            self.array[self.index] = None
            self.size -= 1
            return value

        return defaultValue

    def clear(self):
        self.size = 0
        self.foundNode = self.priorNode = None
        self.index -= 1
        self.array = Array(HashDict.DEFAULT_CAPACITY)
