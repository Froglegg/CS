from abstract_collection import AbstractCollection


class AbstractStack(AbstractCollection):
    def __init__(self, sourceCollection) -> None:
        super().__init__(sourceCollection=sourceCollection)

    def add(self, item):
        self.push(item)
