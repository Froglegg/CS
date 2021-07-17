class LinkedListIterator(object):
    def __init__(self, backingStore) -> None:
        super().__init__()
        self.backingStore = backingStore
        self.modCount = backingStore.getModCount()
        self.first()

    def first(self):
        '''resets cursor to the beginning of the backing store'''
        self.cursor = 0
        self.lastItemPos = -1

    def getPosition(self):
        return self.lastItemPos

    # Navigational methods
    def hasNext(self):
        '''returns true if the iterator has a next item or False otherwise'''
        return self.cursor < len(self.backingStore)

    def next(self):
        ''' preconditions: hasNext is true and the list has not been modified EXCEPT by this iterator's mutators
        Returns the current item and advances the cursor to the next item 
        '''
        if not self.hasNext():
            raise ValueError("No next item in list iterator")
        if self.modCount != self.backingStore.getModCount():
            raise AttributeError("Illegal modficiation of backing store")
        self.lastItemPos = self.cursor
        self.cursor += 1
        return self.backingStore.getNode(self.lastItemPos).data

    def last(self):
        '''Moves cursor to end of backing store'''
        self.cursor = len(self.backingStore)
        self.lastItemPos = -1

    def hasPrevious(self):
        return self.cursor > 0

    def previous(self):
        '''preconditions: hasPrevious returns true and the list has not been modified EXCEPT by this iterator's mutators
        Returns the current item and moves the cursor to the previous item 
        '''
        if not self.hasPrevious():
            raise ValueError("No previous item in list iterator")
        if self.modCount != self.backingStore.getModCount():
            raise AttributeError("Illegal modficiation of backing store")
        self.cursor -= 1
        self.lastItemPos = self.cursor
        return self.backingStore.getNode(self.lastItemPos).data

    # Mutators
    def replace(self, item):
        '''preconditions: the current position is defined, and the list has not been modified EXCEPT by this iterator's methods'''
        if self.lastItemPos == -1:
            raise AttributeError("The current position is undefined")
        if self.modCount != self.backingStore.getModCount():
            raise AttributeError("List has been modified illegally")
        nodeReplaced = self.backingStore.replace(self.lastItemPos, item)
        self.lastItemPos = -1
        return nodeReplaced

    def insert(self, item):
        '''Preconditions: the list has not been modified except by this iterator's methods'''
        if self.modCount != self.backingStore.getModCount():
            raise AttributeError("List has been modified illegally")
        if self.lastItemPos == -1:
            # cursor not defined, so add item to end of list
            self.backingStore.add(item)
        else:
            self.backingStore.insert(self.lastItemPos, item)
        self.lastItemPos = -1
        self.modCount += 1

    def remove(self):
        '''preconditions: the current position is defined, and the list has not been modified EXCEPT by this iterator's methods'''
        if self.lastItemPos == -1:
            raise AttributeError("The current position is undefined")
        if self.modCount != self.backingStore.getModCount():
            raise AttributeError("List has been modified illegally")
        item = self.backingStore.pop(self.lastItemPos)
        # if the item was obtained via next, move cursor back
        if self.lastItemPos < self.cursor:
            self.cursor -= 1
        self.modCount += 1
        self.lastItemPos = -1
        return item
