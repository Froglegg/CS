class Comparable(object):
    ''' Comparable class for priority queue'''

    def __init__(self, data, priority=1) -> None:
        super().__init__()
        self.data = data
        self.priority = priority

    def __str__(self):
        return str(self.data)

    def __eq__(self, other: object) -> bool:
        if self is other:
            return True
        if type(self) != type(other):
            return False
        return self.priority == other.priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __le__(self, other):
        return self.priority <= other.priority

    def getData(self):
        return self.data

    def getPriority(self):
        return self.priority
