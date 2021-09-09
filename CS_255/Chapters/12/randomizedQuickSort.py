'''
To get best case for quick sort, we need L and G to be divided equally
e.g., having the pivot as close to the middle as possible
To do this, we pick a random element in the collection as our pivot
'''
from random import randrange
iterations = 0
pivotIterations = 0


def randomizedQuickSort(S: list[int]):
    ''' 
    Input: S list of n integers of any size

    Output: sortedList of integers ascending

    Complexity: a highly probable O(n * Logn)

    Justification: 
    '''
    global iterations
    iterations += 1
    n = len(S)
    if n < 2:
        # if list is empty or only has one element, return
        return S

    def choosePivot(S):
        global pivotIterations
        pivotIterations += 1
        # pivot is random index in list
        pivotIndex = randrange(len(S))
        p = S[pivotIndex]

        # less than pivot
        L = []
        # equal to pivot
        E = []
        # greater than pivot
        G = []

        # while S has "truthiness", or, isn't empty
        for el in S:
            if el < p:
                L.append(el)
            elif p < el:
                G.append(el)
            else:
                E.append(el)

        if len(S) <= 2 or ((len(S)/4 <= len(L) <= (3*len(S))/4) and (len(S)/4 <= len(G) <= (3*len(S))/4)):
            return (L, E, G)

        # if ((len(S)/4 <= len(L) <= (3*len(S))/4) and (len(S)/4 <= len(G) <= (3*len(S))/4)):
        #     return (L, E, G)
        else:
            return choosePivot(S)

    (L, E, G) = choosePivot(S)
    print(L, E, G)

    # recursion
    randomizedQuickSort(L)
    randomizedQuickSort(G)

    sorted = []
    # concatenate results, less than, equal to, and then greater than in that order
    while L:
        sorted.append(L.pop())
    while E:
        sorted.append(E.pop())
    while G:
        sorted.append(G.pop())

    # return sorted sequence
    return sorted


test = [randrange(100) for _ in range(100)]


sorted = randomizedQuickSort(test)
print(sorted)
print(iterations + pivotIterations)
