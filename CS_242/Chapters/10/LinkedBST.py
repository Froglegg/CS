from Collections.AbstractCollection import AbstractCollection
from BSTNode import BSTNode
from Collections.ArrayStack import ArrayStack
from Collections.LinkedQueue import LinkedQueue
from Collections.Comparable import Comparable


class LinkedBST(AbstractCollection):
    '''Linked based BST implementation
        ITEMS MUST BE COMPARABLES!!!
    '''

    def __init__(self, sourceCollection) -> None:
        '''Sets the initial state of self,
        which includes the contents of sourceCollection, if present.'''
        # external link to entire tree structure is named self.root,
        # on instantiation this var is set to None
        self.root = None
        super().__init__(sourceCollection=sourceCollection)

    def __iter__(self):
        ''' PRE ORDER traversal is default traversal, use probe based loop to visit the nodes,
        along with a stack to support returns to parent nodes during the traveral.
        Upon each visit to a node, its item is yielded.
        '''
        # create a stack, push the root node, if there is one, onto the stack
        stack = ArrayStack()
        stack.add(self.root)
        # while the stack is not empty
        while stack.isEmpty() is False:
            # pop a node from the stack
            node = stack.pop()
            # yield the item in the node
            yield(node.data)
            # push the node's right and left children, if they exist, in that order onto the stack
            if(node.right):
                stack.push(node.right)
            if(node.left):
                stack.push(node.left)

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
                    node.left = BSTNode(item, parent=node, key=keyValue)
                else:
                    recurse(node.left, keyValue)

            # new item is greater than or equal; go right until spot is found
            elif node.right == None:
                node.right = BSTNode(item, parent=node, key=keyValue)

            else:
                recurse(node.right, keyValue)
            # end of recurse
        # Tree is empty, so new item goes at root
        if self.isEmpty():
            self.root = BSTNode(item, parent=None, key=0)
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

    def preOrder(self):
        ''' Use probe based loop to visit the nodes,
        along with a stack to support returns to parent nodes during the traveral.
        Return iterator
        '''
        # create a stack, push the root node, if there is one, onto the stack
        stack = ArrayStack()
        stack.add(self.root)
        lyst = []
        # while the stack is not empty
        while stack.isEmpty() is False:
            # pop a node from the stack
            node = stack.pop()
            # yield the item in the node
            lyst.append(node.data)
            # push the node's right and left children, if they exist, in that order onto the stack
            if(node.right):
                stack.push(node.right)
            if(node.left):
                stack.push(node.left)

        return iter(lyst)

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

    def levelOrder(self):
        '''supports levelorder traversal on a view of self, uses a queue and a list...'''

        # create list to gather items/data visited
        lyst = list()
        # create queue to schedule nodes for visitation, add root node, if there is one
        queue = LinkedQueue()
        queue.add(self.root)

        # while queue is not empty, the front node is popped, and its item is added to the list
        while queue.isEmpty() == False:
            frontNode = queue.pop()
            lyst.append(frontNode.data)
            # the popped node's left and right children, if they exist, are added to the queue
            if frontNode.left:
                queue.add(frontNode.left)
            if frontNode.right:
                queue.add(frontNode.right)

        # when the loop terminates, the method returns an iterator on the lyst
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
