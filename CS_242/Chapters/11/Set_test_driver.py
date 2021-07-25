from ArraySet import ArraySet
from HashSet import HashSet


def test(s:HashSet):
    a = s([22, 87, 23])
    b = s([87])

    print(b.isSubset(a))
    # union | shou ld be
    # # {1, 2, 3, 4}
    # print(a | b)

    # # intersection & should be {2,3}
    # print(a & b)

    # # diff should be {1}
    # print(a-b)
    # # should be False
    # print(a == b)

    # print(a.remove(1))
    # print(a.size)


test(HashSet)
