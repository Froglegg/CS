from Heaps.Heap import AdaptableHeapPriorityQueue as PQ


class Node(object):
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def children(self):
        return(self.left, self.right)

    def printTree(self):
        def recurse(node, level=0):
            if node != None:

                recurse(node.right, level + 1)
                print(' ' * 6 * level + '->', node.value)
                recurse(node.left, level + 1)

        recurse(self)

    def encodingTable(self):

        def recurse(node, binaryStr=''):

            if node.value is not None and type(node.value) is str:

                return {node.value: binaryStr}

            (l, r) = node.children()

            d = dict()

            d.update(recurse(l, binaryStr + '0'))
            d.update(recurse(r, binaryStr + '1'))

            return d

        return recurse(self)


def Huffman(X: str):
    '''
    Input: String X of length n with d distinct characters
    Output: Huffman coding tree for X
    '''
    # Compute the frequency of each character c of X
    frequencyTable = {}
    for char in X:
        if char in frequencyTable:
            frequencyTable[char] += 1
        else:
            frequencyTable[char] = 1

    # Initialize a priority queue Q
    Q = PQ()

    freq = sorted(frequencyTable.items(),
                  key=lambda x: x[1], reverse=True)

    # for each character c in X string, create a single node binary tree storing c
    # and insert tree into priority q with key as frequencyTable[c] and value as tree
    for char in freq:
        # create node storing character key from frequency map
        node = Node(char[0])
        # insert node into priority queue, with its priority key as the characters frequency table value
        Q.add(char[1], node)

    # dequeue PQ and create new binary node with dequeued nodes as left and right subtrees
    while len(Q) > 1:
        (freq1, TreeNode1) = Q.remove_min()
        (freq2, TreeNode2) = Q.remove_min()
        # create new binary tree with freq1+freq2 as node value, and left/right subtrees
        tree = Node(freq1+freq2, TreeNode1, TreeNode2)

        # add new binary tree to queue, with key as the sum of the two frequencies (tree.value)
        Q.add(tree.value, tree)

    (_, tree) = Q.remove_min()

    return tree


testStr = "add ab\nto 2**abd"

testTree: Node = Huffman(testStr)

testTree.printTree()

encodingTable = testTree.encodingTable()


print(' Char | Encoding ')
print('----------------------')

for (char, encoding) in encodingTable.items():
    print(' %-4r |%12s' % (char, encoding))

s = ""

for c in testStr:
    s += encodingTable[c]
print(s)
