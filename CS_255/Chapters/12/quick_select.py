from random import choice


def quick_select(S, k):
    '''return the kth smallest element of list S, for k from 1 to len(S)'''
    '''O(n)'''
    if len(S) == 1:
        return S[0]
    pivot = choice(S)
    L = [x for x in S if x < pivot]
    E = [x for x in S if x == pivot]
    G = [x for x in S if x > pivot]
    if k <= len(L):
        return quick_select(L, k)
    elif k <= len(L) + len(E):
        return pivot
    else:
        j = k - len(L) - len(E)
        return quick_select(G, j)


test = [1, 564, 23, 64, 23, 2]
thirdSmallestElement = quick_select(test, 3)
print(thirdSmallestElement)
secondSmallestElement = quick_select(test, 2)
print(secondSmallestElement)
firstSmallestElement = quick_select(test, 1)
print(firstSmallestElement)
