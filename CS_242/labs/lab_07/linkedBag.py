from node import Node


class LinkedBag(object):
    '''A linkedBag is a linkedList implementation of a bag collection'''
    # constructor

    def __init__(self, sourceCollection=None) -> None:
        super().__init__()
        self.items = None
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

    def __eq__(self, other):
        if self is other:
            return True
        if type(self) != type(other) or len(self) != len(other):
            return False
        for item in self:
            if self.count(item) != other.count(item):
                return False
        return True

    def __iter__(self):
        # cursor in linked struct is a reference pointer to nodes in the linked structure
        # cursor initially set to the external pointer, self.items, and stops the loop when it reaches the end (None)

        cursor = self.items
        while cursor != None:
            # yeild to the caller
            yield cursor.data
            cursor = cursor.next

    def __add__(self, other):

        result = LinkedBag(self)
        for item in other:

            result.add(item)
        return result

    def count(self, items):
        return 0

    # Mutator methods
    def clear(self):
        self.size = 0
        self.items = None

    def add(self, item):
        self.items = Node(item, self.items)
        self.size += 1

    def remove(self, item):
        if not item in self:
            raise KeyError(str(item) + " not found")
        probe = self.items
        trailer = None
        for targetItem in self:
            if targetItem == item:
                break
            trailer = probe
            probe = probe.next
        # unhook node to be deleted, either first one or one thereafter
        if probe == self.items:
            self.items = probe.next
        else:
            trailer.next = probe.next

        self.size -= 1


# linkedBag = LinkedBag(["1", "2", "3"])
