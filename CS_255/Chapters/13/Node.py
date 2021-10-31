class Node(object):
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def printTree(self):
        def recurse(node, level=0):
            if node != None:
                recurse(node.left, level + 1)
                print(' ' * 4 * level + '->', node.value)
                recurse(node.right, level + 1)
        recurse(self)


def printTree(node, level=0):
    if node != None:
        printTree(node.left, level + 1)
        print(' ' * 4 * level + '->', node.value)
        printTree(node.right, level + 1)


# t = Node(1, Node(2, Node(4, Node(7)), Node(9)), Node(3, Node(5), Node(6)))
# t.printTree()
