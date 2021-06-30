''' 
Array data structure
An array is like a list, but the client can use only [], len, iter and str
'''


class Array(object):
    '''Represents an array'''

    def __init__(self, capacity, fillValue=None) -> None:
        ''' capacity is the static size of the array'''
        super().__init__()
        self.items = list()
        for count in range(capacity):
            self.items.append(fillValue)

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, newItem):
        self.items[index] = newItem
