from BinaryTree.BinaryTree import Tree
from Heaps.Heap import AdaptableHeapPriorityQueue as PQ
from Node import Node


def Huffman(X: str):
    '''
    Input: String X of length n with d distinct characters
    Output: Huffman coding tree for X
    '''
    # Compute the frequency of each character c of X
    frequencyMap = {}
    for char in X:
        if char in frequencyMap:
            frequencyMap[char] += 1
        else:
            frequencyMap[char] = 1

    # Initialize a priority queue Q
    Q = PQ()

    # for each character c in X string, create a single node binary tree storing c
    # and insert tree into priority q with key as frequencyMap[c] and value as tree
    for char in X:

        node = Node(char)

        Q.add(frequencyMap[char], node)

    # print([f"{i}" for i in Q])

    # dequeue PQ and create new binary tree with dequeued trees as left and right subtree
    while len(Q) > 1:
        (freq1, T1) = Q.remove_min()
        (freq2, T2) = Q.remove_min()
        tree = Node()
        tree.left = T1
        tree.right = T2
        # add new binary tree to queue, with key as the sum of the two frequencies
        Q.add(freq1+freq2, tree)

    (_, tree) = Q.remove_min()

    return tree


testStr = "add ab\nto 2**abd"

testTree: Tree = Huffman(testStr)

# testTree.printTree()
