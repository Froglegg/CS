
from Collections.AbstractCollection import AbstractCollection


class AbstractDict(AbstractCollection):

    def __init__(self, keys, values):
        AbstractCollection.__init__(self)
        if keys and values:
            valuesIter = iter(values)
            for key in keys:
                self[key] = next(valuesIter)

    def __str__(self):
        return '{' + ", ".join(map(str, self.entries())) + '}'

    def __add__(self, other):
        result = type(self)(self.keys(), self.values())

        for key in other:
            result[key] = other[key]
        return result

    def __eq__(self, other):
        if self is other:
            return True
        if type(self) != type(other) or len(self) != len(other):
            return False
        for key in self:
            if not key in other:
                return False
        return True

    def __iter__(self):
        return iter(self)

    def keys(self):
        return map(lambda key: key.key, self)

    def values(self):
        return map(lambda key: self[key.key], self)

    def entries(self):
        return map(lambda key: Entry(key.key, self[key.key]), self)

    def get(self, key, defaultValue=None):
        ''' returns value assocaited with key if present, else None'''
        return self[key] or defaultValue


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
