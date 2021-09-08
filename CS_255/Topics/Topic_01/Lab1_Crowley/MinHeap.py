class MinHeap(object):
    '''
    MinHeap implementation uses a O(logN) insertion method to insert integers into the appropriate, 
    ascending sorted position (lowest at bottom of heap to highest at top). See "add" method for details. 

    The total complexity for building the min heap is n log n, or O(nLogN), where n = size of source collection 
    '''

    def __init__(self, sourceCollection=None):
        super().__init__()
        self.size = 0
        self.heap = []

        if sourceCollection:
            # O(NlogN) initialization, building heap...
            for item in sourceCollection:
                try:
                    # for each item in colleciton of length N, fire this O(logN) insertion method
                    self.add(int(item))
                except:
                    print(
                        "Please make sure source collection can be converted to integers!")

    def __len__(self):
        return self.size

    def __iter__(self):
        '''
        returns heap list to iterator 
        '''
        return iter(self.heap)

    def __str__(self):
        '''
        returns string representation of heap
        '''
        return f"{self.heap}"

    def __getitem__(self, key):
        return self.heap[key]

    def __setitem__(self, index, value):
        try:
            self.heap.__setitem__(index, value)
        except IndexError:
            for _ in range(index-len(self)+1):
                self.heap.append(None)
            self.heap.__setitem__(index, value)

    def isEmpty(self):
        return len(self) == 0

    def add(self, item):
        ''' 
        Insertions into the min heap inserts items in the correct sorted position
        It begins by inserting the first element at the bottom of the heap (the first item being added)
        It then enters a loop that walks the new elements up the heap until the new elements value is less than or equal to its parents
        When this process stops, the element is in the proper place 

        Complexity: This method is logarithmic O(logN) 
        Justification: At most you must make logN comparisons to walk up the tree from the bottom.

        '''

        self.size += 1
        self.heap.append(item)

        curPos = len(self.heap)-1

        while curPos > 0:

            parent = (curPos - 1)
            parentItem = self.heap[parent]

            if parentItem <= item:
                break

            else:
                self.heap[curPos] = self.heap[parent]
                self.heap[parent] = item
                curPos = parent
