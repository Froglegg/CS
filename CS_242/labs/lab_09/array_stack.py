from arrays import Array
from abstract_stack import AbstractStack


class ArrayStack(AbstractStack):

    DEFAULT_CAPACITY = 10

    def __init__(self, sourceCollection=None):
        self.items = Array(ArrayStack.DEFAULT_CAPACITY)
        AbstractStack.__init__(
            self, sourceCollection).__init__(sourceCollection)

    # accessors
    def __iter__(self):
        cursor = 0
        while cursor < len(self):
            yield self.items[cursor]
            cursor += 1

    def peek(self):
        if self.isEmpty():
            raise KeyError("The stack is Empty")
        return self.items[len(self)-1]

    # mutators
    def clear(self):
        self.size = 0
        self.items = Array(ArrayStack.DEFAULT_CAPACITY)

    def push(self, item):
        #   check array memory / load factor here, increase size if necessary
        #     increasing size of array
        if self.size == len(self.items):
            # create new array and copy data from old array
            # double the size of the array instead of adding one new cell each time the array needs to be resized to ensure better performance
            temp = Array(len(self.items)*2)
            for i in range(self.size):
                temp[i] = self.items[i]
            # reset old array variable to new array, old arrays memory is left out for the garbage collector
            self.items = temp
        self.items[len(self)] = item
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise KeyError("The stack is Empty")
        oldItem = self.items[len(self)-1]
        self.size -= 1

        # check array memory / load factor here, decrease size if necessary
# performant choice is, if logical size is less than or equal to the 1/4 the length of b and the length of b is greater than 2x the default capacity
        if self.size <= len(self.items) // 4 and len(self.items) >= ArrayStack.DEFAULT_CAPACITY * 2:
            temp = Array(len(self.items) // 2)
            for i in range(self.size):
                temp[i] = self.items[i]
            self = temp

        return oldItem
