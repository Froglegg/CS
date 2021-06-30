from node import Node
from abstract_stack import AbstractStack


class LinkedStack(AbstractStack):
    def __init__(self, sourceCollection=None) -> None:
        self.items = None
        super().__init__(sourceCollection)

    # accessors
    def __iter__(self):
        def visitNodes(node):
            if node != None:
                visitNodes(node.next)
                tempList.append(node.data)

        tempList = list()
        visitNodes(self.items)
        return iter(tempList)

    def peek(self):
        if self.isEmpty():
            raise KeyError("The stack is Empty")
        return self.items.data

    # mutators
    def clear(self):
        self.size = 0
        self.items = None

    def push(self, item):
        self.items = Node(item, self.items)
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise KeyError("The stack is empty.")
        oldItem = self.items.data
        self.items = self.items.next
        self.size -= 1
        return oldItem


# lStack = LinkedStack([1, 2, 3])
# for i in lStack:
#     print(i)
# print(lStack)
# lStack.pop()
# print(lStack)
# lStack.peek()
# print(lStack.peek())
# lStack.push(4)
# print(lStack)
# lStack.clear()
# print(lStack)
# lStack.peek()
# print(lStack.items.data)
