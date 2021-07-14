from comparable import Comparable
from linked_queue import LinkedQueue
from node import Node


class PriorityLinkedQueue(LinkedQueue):
    '''a linked-based priority queue implementation'''

    def __init__(self, sourceCollection=None) -> None:
        super().__init__(sourceCollection=sourceCollection)

    def add(self, newItem):
        '''inserts new item after items of greater or equal priority or ahead of items of lesser priority. 
        A has greater priority than B if A < B
        Assumes newItem is a comparable (see Comparable class)
        '''
        print('hey')
        if self.isEmpty() or newItem >= self.rear.data:
            # new item goes to rear, use super class method and pass self into first argument position
            LinkedQueue.add(self, newItem)
        else:
            # search for position where the new item is less
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


pq = PriorityLinkedQueue([Comparable("Third Class", 3), Comparable(
    "Second Class", 2), Comparable("Third Class", 3), Comparable("First Class", 1), Comparable(
    "Second Class", 2)])

print(pq)
pq.pop()
print(pq)
