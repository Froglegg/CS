class BSTNode(object):
    '''represents a node in a binary search tree
       taken partially from Lambert, partially from 
       https://runestone.academy/runestone/books/published/pythonds/Trees/SearchTreeImplementation.html
    '''

    def __init__(self, data, left=None, right=None, parent=None, key=None) -> None:
        super().__init__()
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        self.key = key

    def hasLeftChild(self):
        return self.left

    def hasRightChild(self):
        return self.right

    def isLeftChild(self):
        return self.parent and self.parent.left == self

    def isRightChild(self):
        return self.parent and self.parent.right == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.right or self.left)

    def hasAnyChildren(self):
        return self.right or self.left

    def hasBothChildren(self):
        return self.right and self.left

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.left = None
            else:
                self.parent.right = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.left = self.left
                else:
                    self.parent.right = self.left
                self.left.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right
                self.right.parent = self.parent

    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.right.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.right = None
                    succ = self.parent.findSuccessor()
                    self.parent.right = self
        return succ

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.left
        return current

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.data = value
        self.left = lc
        self.right = rc
        if self.hasLeftChild():
            self.left.parent = self
        if self.hasRightChild():
            self.left.parent = self
