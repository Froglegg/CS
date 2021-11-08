from typing import ByteString
from Heaps.Heap import AdaptableHeapPriorityQueue as PQ


class HuffmanClass:
    # nested huffman tree node class
    class HuffmanNode(object):

        def __init__(self, value=None, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right

        def children(self):
            return(self.left, self.right)

        def hasChildren(self):
            return (self.left or self.right)

        def printTree(self):
            def recurse(node, level=0):
                if node != None:
                    recurse(node.right, level + 1)
                    if not node.hasChildren():
                        print(' ' * 6 * level + '->',
                              repr(chr(int(node.value))))
                    else:
                        print(' ' * 6 * level + '->', repr(node.value))
                    recurse(node.left, level + 1)

            recurse(self)

        def __str__(self):
            return str(self.value)

    def __init__(self, X: ByteString = b"") -> None:
        '''Huffmans class inits with a byte string and encodes it using Huffman's Algorithm (see self.encode)'''
        self.plainText = X
        self.frequencyTable = {}
        # pq for debugging purposes
        self.priorityQueue = PQ()
        self.encoded = self.encode(X)
        self.decoded = None

    def getFrequencyTable(self):
        '''returns python dict with character keys and frequency integers as values'''
        return self.frequencyTable

    def getPriorityQueue(self):
        return self.priorityQueue

    def printTree(self):
        if self.encoded is not None:
            self.encoded.printTree()

    def getEncodingTable(self) -> dict:
        '''
        Returns python dict with character keys and huffman binary strings as values
        '''
        # if empty, i.e., there was nothing in the input file, return None
        if self.encoded is None:
            return {}

        def recurse(node, binaryStr=''):

            if node.value is not None and type(node.value) is str:

                return {node.value: binaryStr}

            (l, r) = node.children()

            d = dict()

            d.update(recurse(l, binaryStr + '0'))
            d.update(recurse(r, binaryStr + '1'))

            return d

        return recurse(self.encoded)

    def getEncodingTableStr(self) -> str:
        s = ' Char | Encoding \n----------------------'

        for (char, encoding) in self.getEncodingTable().items():
            s += (' %-4r |%12s' % (char, encoding))

        return s

    def getEncoding(self) -> str:
        encodingTable = self.getEncodingTable()

        s = ""

        for c in self.plainText:
            s += encodingTable[str(c)]

        return s

    def decode(self, binaryString: str):
        '''
           Input: encoded Huffman Binary string
           Output: decoded plaintext
           complexity: quadratic O(n^2)
        '''

        encodingTable = self.getEncodingTable()
        byteString = ""
        decodedString = ""

        for bit in binaryString[2:]:
            byteString += bit

            for char, code in encodingTable.items():
                if byteString == code:
                    decodedString += chr(int(char))
                    byteString = ""
                    break

        return decodedString

    def encode(self, X: str):
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

        self.frequencyTable = frequencyTable

        # Initialize a priority queue Q
        Q = PQ()

        # sort frequency table items by frequency
        freq = sorted(frequencyTable.items(),
                      key=lambda x: x[1], reverse=True)

        # for each character c in X string, create a single node binary tree storing c
        # and insert tree into priority q with key as frequencyTable[c] and value as tree
        for item in freq:

            # create node storing character key from frequency map
            node = self.HuffmanNode(str(item[0]))

            # insert node into priority queue, with its priority key as the characters frequency table value
            Q.add(item[1], node)

            # insert into self.pq for debugging purposes
            self.priorityQueue.add(item[1], node)

        # dequeue PQ and create new binary node with dequeued nodes as left and right subtrees
        while len(Q) > 1:

            (freq1, TreeNode1) = Q.remove_min()

            (freq2, TreeNode2) = Q.remove_min()

            # create new binary tree with freq1+freq2 as node value, and left/right subtrees
            tree = self.HuffmanNode(freq1+freq2, TreeNode1, TreeNode2)

            # add new binary tree to queue, with key as the sum of the two frequencies (tree.value)
            Q.add(tree.value, tree)

        if Q.is_empty():

            return None

        else:

            (_, tree) = Q.remove_min()

            return tree
