def merge(S1: list, S2: list, S: list):
    '''Merge two sorted python lists s1 and s2 into properly sized list S'''
    i = j = 0
    while i + j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            # copy the ith element of S1 as next item of S
            S[i+j] = S1[i]
            i += 1
        else:
            S[i+j] = S2[j]
            j += 1


def mergeSort(S: list):
    '''Sort the elements of Python list S using merge-sort algorithm'''
    '''O(logN) running time'''
    n = len(S)
    if n < 2:
        # list is already sorted
        return S
    # Divide
    mid = n // 2
    S1 = S[0:mid]
    S2 = S[mid:n]
    # Conquer (with recursion)
    mergeSort(S1)
    mergeSort(S2)
    # combine / merge results
    merge(S1, S2, S)
    return S


print(mergeSort([3, 2, 1, 88, 23, 44, 11, 12, 4, 7, 1, 3, 2, 2, 2]))
