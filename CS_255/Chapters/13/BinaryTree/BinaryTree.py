class Tree:
    def __init__(self, value=None, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value

    def __str__(self):
        '''returns string representation with the tree rotated 90 degrees counterclockwise'''
        def recurse(node, level):
            s = ""
            if node != None:
                s += recurse(node.right, level + 1)
                s += "| " * level
                s += str(node.value) + "\n"
                s += recurse(node.left, level+1)
            return s
        return recurse(self, 0)

    # def PrintTree(self):
    #     print(self.value)
    #     if self.left:
    #         self.left.PrintTree()
    #     if self.right:
    #         self.right.PrintTree()


# try:
#     root = Tree(10)
#     root.left = Tree(3)
#     root.right = Tree(8)
#     root.left.left = Tree(1)
#     root.left.right = Tree(6)
#     root.right.right = Tree(12)
#     root.PrintTree()
# except:
#     print("An exception has occurred!")
