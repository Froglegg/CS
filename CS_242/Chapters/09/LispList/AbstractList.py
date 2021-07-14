from AbstractCollection import AbstractCollection


class AbstractList(AbstractCollection):
    def __init__(self, sourceCollection=None) -> None:
        '''retains a count of modifications to the list'''
        self.modCount = 0
        super().__init__(sourceCollection=sourceCollection)

    def getModCount(self):
        return self.modCount

    def incModCount(self):
        self.modCount += 1

    def index(self, item):
        position = 0
        for data in self:
            if data == item:
                return position
            else:
                position += 1
        if position == len(self):
            raise ValueError(str(item) + " is not in list.")

    def add(self, item):
        '''adds item to end of list'''
        self.insert(len(self), item)

    def remove(self, item):
        position = (self.index(item))
        self.pop(position)
