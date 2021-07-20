# from LinkedBST import LinkedBST
from Collections.Comparable import Comparable
from LinkedBST import LinkedBST


def test():
    lyst = []
    for i in range(9):
        lyst.append(Comparable(i//2 if i % 2 == 0 else i -
                               i * 2, i//2 if i % 2 == 0 else i - i * 2))

    bst = LinkedBST(lyst)
    # print(bst)

    # for i in bst:
    #     print(i)
    # for i in bst.inOrder():
    #     print(i)
    # for i in bst.postOrder():
    #     print(i)
    # for i in bst.levelOrder():
    #     print(i)

    # print(bst.findMin().data, bst.findMin().data)

    bst.add(Comparable(7, 7))
    # print(bst)
    bst.replace(Comparable(7, 7), Comparable('-2', -2))
    print(bst)
    print(bst.findItem(Comparable('-2', -2)).getPriority())
    # print(bst)


test()
