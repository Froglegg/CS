class BagInterface(object):

    # constructor
    def __init__(self, sourceCollection=None) -> None:
        super().__init__()
        pass

    # Accessor methods
    def isEmpty(self):
        return True

    def __len__(self):
        return 0

    def __str__(self):
        return ""

    def __iter__(self):
        return None

    def __add__(self, other):
        return None

    def __eq__(self, other):
        return False

    def count(self, items):
        return 0

    # Mutator methods
    def clear(self):
        pass

    def add(self, item):
        pass

    def remove(self, item):
        pass
