from AbstractCollection import AbstractCollection
from BinaryTree.Comparable import Comparable


class LinkedBST(AbstractCollection):
    '''Linked based BST implementation
        ITEMS MUST BE COMPARABLES!!!
    '''

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

    def __init__(self, sourceCollection) -> None:
        '''Sets the initial state of self,
        which includes the contents of sourceCollection, if present.'''
        # external link to entire tree structure is named self.root,
        # on instantiation this var is set to None
        self.root = None
        super().__init__(sourceCollection=sourceCollection)

    def __str__(self):
        '''returns string representation with the tree rotated 90 degrees counterclockwise'''
        def recurse(node, level):
            s = ""
            if node != None:
                s += recurse(node.right, level + 1)
                s += "| " * level
                s += str(node.data) + "\n"
                s += recurse(node.left, level+1)
            return s
        return recurse(self.root, 0)

    def __add__(self, other):
        for i in other:
            self.add(i)

    def clear(self):
        self.root = None
        self.size = 0

    def add(self, item: Comparable):
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
            self.root = self.Node(item, parent=None, key=0)
        # otherwise, search for the item's spot
        else:
            recurse(self.root, keyValue=0)

        self.size += 1
        # note that, in all cases, an item is added in a leaf node

    def replace(self, itemToReplace: Comparable, item: Comparable):
        '''Replacing an item should not enable users to go against the spirit of the BST
        This function simply removes the item to be replaced, and then adds the incoming item 
        That way, it's appropriate place will be found in the tree
        If users want to replace item at the node's place in the tree, they'll need to pass in the same priority of the node
        '''
        popped = self.remove(itemToReplace)
        self.add(item)
        return popped

    def remove(self, item: Comparable):
        ''' 
        following directions in Lambert led to a dead end
        this function taken from https://runestone.academy/runestone/books/published/pythonds/Trees/SearchTreeImplementation.html
        '''
        if self.size > 1:
            nodeToRemove = self.__findNode(item)
            if nodeToRemove:
                self.__remove(nodeToRemove)
                self.size -= 1
            else:
                raise KeyError('Error, item not in tree')
        elif self.size == 1 and self.root.data == item:
            self.root = None
            self.size -= 1
        else:
            raise KeyError('Error, key not in tree')

    def __remove(self, nodeToRemove):

        if nodeToRemove.isLeaf():  # leaf, has no children
            if nodeToRemove == nodeToRemove.parent.left:
                nodeToRemove.parent.left = None
            else:
                nodeToRemove.parent.right = None

        elif nodeToRemove.hasBothChildren():  # interior, has two children
            succ = nodeToRemove.findSuccessor()
            succ.spliceOut()
            nodeToRemove.key = succ.key
            nodeToRemove.data = succ.data

        else:  # this node has one child
            if nodeToRemove.hasLeftChild():
                if nodeToRemove.isLeftChild():
                    nodeToRemove.left.parent = nodeToRemove.parent
                    nodeToRemove.parent.left = nodeToRemove.left
                elif nodeToRemove.isRightChild():
                    nodeToRemove.left.parent = nodeToRemove.parent
                    nodeToRemove.parent.right = nodeToRemove.left
                else:
                    nodeToRemove.replaceNodeData(nodeToRemove.left.key,
                                                 nodeToRemove.left.data,
                                                 nodeToRemove.left.left,
                                                 nodeToRemove.left.right)
            else:
                if nodeToRemove.isLeftChild():
                    nodeToRemove.right.parent = nodeToRemove.parent
                    nodeToRemove.parent.left = nodeToRemove.right
                elif nodeToRemove.isRightChild():
                    nodeToRemove.right.parent = nodeToRemove.parent
                    nodeToRemove.parent.right = nodeToRemove.right
                else:
                    nodeToRemove.replaceNodeData(nodeToRemove.right.key,
                                                 nodeToRemove.right.data,
                                                 nodeToRemove.right.left,
                                                 nodeToRemove.right.right)

    def findItem(self, item: Comparable):
        '''
        takes data item and returns data item if item is found, returns None otherwise'''

        # recusive helper function
        def recurse(node):
            if node is None:
                return None
            elif item == node.data:
                return node.data
            elif item < node.data:
                return recurse(node.left)
            else:
                return recurse(node.right)
        # top level call on root made
        return recurse(self.root)

    def __findNode(self, item):
        '''takes data item and returns node reference'''
        # recusive helper function
        def recurse(node):
            if node is None:
                return None
            elif item == node.data:
                return node
            elif item < node.data:
                return recurse(node.left)
            else:
                return recurse(node.right)
        # top level call on root made
        return recurse(self.root)

    def inOrder(self):
        '''supports inorder traversal on a view of self'''
        lyst = list()

        def recurse(node):
            # if tree is not empty
            if node != None:
                # visit left subtree
                recurse(node.left)
                # append item at root of tree
                lyst.append(node.data)
                # visit right subtree
                recurse(node.right)

        recurse(self.root)
        return iter(lyst)

    def postOrder(self):
        '''supports postorder traversal on a view of self'''
        lyst = list()

        def recurse(node):
            # if tree is not empty
            if node != None:
                # visit left subtree
                recurse(node.left)
                # visit right subtree
                recurse(node.right)
                # append item at root of tree
                lyst.append(node.data)

        recurse(self.root)
        return iter(lyst)

    def findMax(self, tree=None):
        ''' returns rightmost item in tree'''
        if tree == None:
            tree = self.root

        def recurse(node):
            if node.right != None:
                return recurse(node.right)
            return node

        return recurse(tree)

    def findMin(self, tree=None):
        ''' returns leftmost item in tree'''
        if tree == None:
            tree = self.root

        def recurse(node):
            if node.left != None:
                return recurse(node.left)
            return node

        return recurse(tree)


lyst = []
for i in range(9):
    lyst.append(Comparable(i//2 if i % 2 == 0 else i -
                           i * 2, i//2 if i % 2 == 0 else i - i * 2))

bst = LinkedBST(lyst)
# print(bst)
bst.remove(Comparable(4, 4))
print(bst.findMax().data)
print(bst)
