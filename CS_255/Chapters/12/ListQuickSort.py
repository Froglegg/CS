iterations = 0


def quickSort(S: list):
    ''' running time is O(n^2) worst case in this implementation...
    In practice however, when L and G are similar size, the performance is O(nLogn)
    '''
    global iterations
    iterations += 1
    n = len(S)
    if n < 2:
        # if list is empty or only has one element, return
        return S

    # pivot is last element in list
    p = S[-1]

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

    # recursion
    quickSort(L)
    quickSort(G)

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


test = [i for i in range(1000, 0, -1)]


sorted = quickSort(test)
print(sorted)
print(iterations)
