class Node(object):
    '''represents singly linked node'''

    def __init__(self, data, next=None) -> None:
        super().__init__()
        self.data = data
        self.next = next


class Comparable(object):
    ''' Comparable class for priority queue'''

    def __init__(self, data, priority=1) -> None:
        super().__init__()
        self.data = data
        self.priority = priority

    def __str__(self):
        return str(self.data)

    def __eq__(self, other: object) -> bool:
        if self is other:
            return True
        if type(self) != type(other):
            return False
        return self.priority == other.priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __le__(self, other):
        return self.priority <= other.priority

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def getPriority(self):
        return self.priority


class PriorityLinkedQueue(object):
    '''a linked-based priority queue implementation'''

    # special methods
    def __init__(self, sourceCollection=None) -> None:
        super().__init__()
        self.size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.enqueue(item)

    def __iter__(self):
        def visitNodes(node):
            if node != None:
                visitNodes(node.next)
                tempList.append(node.data)
        tempList = list()
        visitNodes(self.front)
        return iter(tempList)

    def __len__(self):
        return self.size

    def __str__(self):
        return "[" + f"{', '.join(map(str, self))}" + "]"

    def __add__(self, other):
        result = PriorityLinkedQueue(self)
        for item in other:
            result.enqueue(item)
        return result

    def __eq__(self, other):
        if self is other:
            return True
        if type(self) != type(other) or len(self) != len(other):
            return False
        otherIter = iter(other)
        for item in self:
            if item != next(otherIter):
                return False
        return True

    # accessors
    def isEmpty(self):
        return len(self) == 0

    def peek(self):
        if self.isEmpty():
            raise KeyError("The queue is empty.")
        return str(self.front.data)

    def count(self, item):
        '''returns # of instances of item in self'''
        count = 0
        for el in self:
            if el is item:
                count += 1
            elif el == item:
                count += 1
        return count

    # mutators

    def enqueue(self, newItem):
        '''inserts new item after items of greater or equal priority or ahead of items of lesser priority. 
        A has greater priority than B if A < B
        Assumes newItem is a comparable (see Comparable class)
        '''
        if self.isEmpty() or newItem >= self.rear.data:
            # new item goes to the rear of the queue, if its priority is less than or equal to the item current in the rear, else if the queue is empty, it goes in the front
            newNode = Node(newItem, None)
            if self.isEmpty():
                self.front = newNode
            else:
                self.rear.next = newNode
            self.rear = newNode
            self.size += 1
        else:
            # search for position where the new item has less priority
            probe = self.front
            # step through nodes until newItem is less than or equal to probe.data
            while newItem >= probe.data:
                trailer = probe
                probe = probe.next
            # instantiate new Node for new item to go into the queue
            newNode = Node(newItem, probe)
            if probe == self.front:
                # new item goes to front
                self.front = newNode
            else:
                # new item goes between two nodes
                trailer.next = newNode
            self.size += 1

    def dequeue(self):
        if self.isEmpty():
            raise KeyError("The queue is empty.")
        oldItem = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return oldItem

    def clear(self):
        self.size = 0
        self.front = None
