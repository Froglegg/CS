def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup. 
    '''
    (oddTup) = (aTup)[0: len(aTup): 2]
    return oddTup


def oddTuples2(aTup):
    return aTup[::2]


#expect (16, 5, 8, 8, 20)
oddTuples2((16, 13, 5, 7, 8, 16, 8, 14, 20))

listA = [1, 4, 3, 0]
listA.sort()
listA.insert(0, 100)
listA = [100, 0, 1, 4, 7, "x", "z", "t", "q", 4, 1, 6, 3]
listA.reverse()
print(listA)
listA.count(100)
