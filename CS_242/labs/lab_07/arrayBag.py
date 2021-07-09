from arrays import Array


class ArrayBag(object):
    ''' An array bag is an array-based implementation of a bag collection'''
    # class variable
    DEFAULT_CAPACITY = 10

    def __init__(self, sourceCollection=None) -> None:
        super().__init__()

        self.items = Array(ArrayBag.DEFAULT_CAPACITY)
        self.size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    # Accessor methods
    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        return self.size

    def __str__(self):
        return "{" + f"{', '.join(map(str, self))}" + "}"

    def __iter__(self):
        ''' supports iteration over a view of self, importatnt for other methods to work!'''
        cursor = 0
        while cursor < len(self):
            # yield sends each item to the caller, the for loop
            yield self.items[cursor]
            cursor += 1

    def __add__(self, other):
        result = ArrayBag(self)
        for item in other:
            result.add(item)
        return result

    def __eq__(self, other):
        if self is other:
            return True
        if type(self) != type(other) or len(self) != len(other):
            return False
        for item in self:
            if self.count(item) != other.count(item):
                return False
        return True

    def count(self, items):
        return 0

    # Mutator methods
    def clear(self):
        self.size = 0
        self.items = Array(ArrayBag.DEFAULT_CAPACITY)

    def add(self, item):
        # check array memory / load factor here, increase size if necessary
        # increasing size of array

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

    def remove(self, item):
        if not item in self:
            raise KeyError(str(item) + " is not in bag")
        targetIndex = 0
        for targetItem in self:
            if targetItem == item:
                break
            targetIndex += 1
        # shift items to the right of target index by one
        for i in range(targetIndex, len(self) - 1):
            self.items[i] = self.items[i + 1]
        # decrement logical size
        self.size -= 1

        # check array memory / load factor here, decrease size if necessary
# performant choice is, if logical size is less than or equal to the 1/4 the length of b and the length of b is greater than 2x the default capacity
        if self.size <= len(self.items) // 4 and len(self.items) >= ArrayBag.DEFAULT_CAPACITY * 2:
            temp = Array(len(self.items) // 2)
            for i in range(self.size):
                temp[i] = self.items[i]
            self = temp


# aBag = ArrayBag(["a", "b", "c", "d", "e", "f", "g", "h"])
