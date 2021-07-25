class AbstractCollection(object):
    def __init__(self, sourceCollection=None) -> None:
        super().__init__()
        self.size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        return self.size

    def __str__(self):
        return "{" + f"{''.join(map(str, self))}" + "}"

    def __add__(self, other):
        result = type(self)(self)
        for item in other:
            result.add(item)
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

    def count(self, item):
        '''returns # of instances of item in self'''
        count = 0
        for el in self:
            if el is item:
                count += 1
            elif el == item:
                count += 1
        return count

    def add(self, item):
        '''adds items to self'''
        pass

    def remove(self, item):
        '''precondition, item is in self... raises keyError if item is not in self'''
        pass
