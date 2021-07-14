from AbstractList import AbstractList
from arrays import Array


class ArrayList(AbstractList):
    DEFAULT_CAPACITY = 10

    def __init__(self, sourceCollection=None) -> None:
        self.items = Array(ArrayList.DEFAULT_CAPACITY)
        super().__init__(sourceCollection=sourceCollection)

    # Accessors
    def __iter__(self):
        cursor = 0
        while cursor < len(self):
            yield self.items[cursor]
            cursor += 1

    def __getitem__(self, i):
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        return self.items[i]

    # Mutators
    def __setitem__(self, i, item):
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        self.items[i] = item

    def __increasePhysicalSize(self):
        ''' check array memory / load factor here, increase size if necessary'''
        if self.size == len(self.items):
            # create new array and copy data from old array
            # double the size of the array instead of adding one new cell each time the array needs to be resized to ensure better performance
            temp = Array(len(self.items)*2)
            for i in range(self.size):
                temp[i] = self.items[i]
            # reset old array variable to new array, old arrays memory is left out for the garbage collector
            self.items = temp
            print("increased physical size of array x 2")

    def __decreasePhysicalSize(self):
        ''' check array memory / load factor here, decrease size if necessary '''
# performant choice is, if logical size is less than or equal to the 1/4 the length of b and the length of b is greater than 2x the default capacity
        if self.size <= len(self.items) // 4 and len(self.items) >= ArrayList.DEFAULT_CAPACITY * 2:
            temp = Array(len(self.items) // 2)
            for i in range(self.size):
                temp[i] = self.items[i]
            self = temp
            print("decreaed physical size of array // 2 ")

    def insert(self, i, item):
        # resize array here if necessary
        self.__increasePhysicalSize()
        if i < 0:
            i = 0
        elif i > len(self):
            i = len(self)
        if i < len(self):
            for j in range(len(self), i, -1):
                self.items[j] = self.items[j-1]
        self.items[i] = item
        self.size += 1
        self.incModCount()

    def pop(self, i=None):
        if i == None:
            i = len(self)-1
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        item = self.items[i]
        for j in range(i, len(self)-1):
            self.items[j] = self.items[j+1]
        self.size -= 1
        self.incModCount()
        # resize array here if necessary
        self.__decreasePhysicalSize()
        return item

    def listIterator(self):
        pass
