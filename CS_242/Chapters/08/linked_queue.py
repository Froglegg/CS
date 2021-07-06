from abstract_collection import AbstractCollection
from node import Node


class LinkedQueue(AbstractCollection):
    def __init__(self, sourceCollection) -> None:
        super().__init__(sourceCollection=sourceCollection)

    def add(self, newItem):
        newNode = Node(newItem, None)
        if self.isEmpty():
            self.front = newNode
        else:
            self.rear.next = newNode
        self.rear = newNode
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise KeyError("The queue is empty.")
        oldItem = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return oldItem
