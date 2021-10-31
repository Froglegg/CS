
from itertools import groupby
from heapq import *


class Node(object):
    left = None
    right = None
    item = None
    weight = 0

    def __init__(self, i, w):
        self.item = i
        self.weight = w

    def setChildren(self, ln, rn):
        self.left = ln
        self.right = rn

    def __repr__(self):
        return "%s - %s -- %s _ %s" % (self.item, self.weight, self.left, self.right)

    def __lt__(self, o):
        return self.weight < o.weight

    def __gt__(self, o):
        return self.weight > o.weight


def huffman(input):
    # above code
    itemqueue = [Node(a, len(list(b))) for a, b in groupby(sorted(input))]
    heapify(itemqueue)
    while len(itemqueue) > 1:
        l = heappop(itemqueue)
        r = heappop(itemqueue)
        n = Node(None, r.weight+l.weight)
        n.setChildren(l, r)
        heappush(itemqueue, n)

    codes = {}

    def codeIt(s, node):
        if node.item:
            if not s:
                codes[node.item] = "0"
            else:
                codes[node.item] = s
        else:
            codeIt(s+"0", node.left)
            codeIt(s+"1", node.right)

    codeIt("", itemqueue[0])
    return codes, "".join([codes[a] for a in input])


print(huffman("add ab\nto 2**abd"))
