class Entry(object):
    ''' represents dictionary entry, supports comparisons by key'''

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str(self.key) + ": " + str(self.value)

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.key == other.key

    def __lt__(self, other):
        if type(self) != type(other):
            return False
        return self.key < other .key

    def __le__(self, other):
        if type(self) != type(other):
            return False
        return self.key <= other.key
