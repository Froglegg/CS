class Tree:

    class Node(object):
        '''
        represents a node in a binary tree
        '''

        def __init__(self, data, left=None, right=None, parent=None, key=None) -> None:
            super().__init__()
            self.data = data
            self.left = left
            self.right = right
            self.parent = parent
            self.key = key

    def __init__(self, sourceCollection=None):
        self.root = None
        self.size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    def __len__(self):
        return self.size

    def __str__(self):
        '''returns string representation with the tree rotated 90 degrees counterclockwise'''

        def recurse(node, level):
            s = ""
            print(node)
            if node != None:
                print("NOT NONE")
                s += recurse(node.right, level + 1)
                s += "| " * level
                s += str(node.data) + "\n"
                s += recurse(node.left, level+1)
            return s

        return recurse(self.root, 0)

    def isEmpty(self):
        return len(self) == 0

    def add(self, item):
        '''adds item to the tree
        In general, an items proper place will be:
        - the root node, if the tree is empty
        - a node in the current node's left subtree, if the new item is less than the item in the current node
        - a node in the current node's right subtree, if the new item is greater than or equal to the item in the current node
        '''

        def recurse(node, keyValue):
            keyValue += 1
            # new item is left, go left until spot is found
            if item < node.data:
                if node.left == None:
                    node.left = self.Node(item, parent=node, key=keyValue)
                else:
                    recurse(node.left, keyValue)

            # new item is greater than or equal; go right until spot is found
            elif node.right == None:
                node.right = self.Node(item, parent=node, key=keyValue)

            else:
                recurse(node.right, keyValue)
            # end of recurse

        # Tree is empty, so new item goes at root
        if self.isEmpty():
            print("EMPTY")
            self.root = self.Node(item, parent=None, key=0)

        # otherwise, search for the item's spot
        else:
            recurse(self.root, keyValue=0)

        self.size += 1
        # note that, in all cases, an item is added in a leaf node
