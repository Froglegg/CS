def indexOfMin(lyst):
    ''' mimic pythons 'min' operator, return idx of min item'''
    minIndex = 0
    currIndex = 1
    while currIndex < len(lyst):
        if lyst[currIndex] < lyst[minIndex]:
            minIndex = currIndex
        currIndex += 1
    return minIndex
    # linear O(n) complexity, where n is size of list


def sequentialSearch(target, lyst):
    ''' mimic python's 'in' operator return position of target item if found, else return -1'''
    position = 0
    while position < len(lyst):
        if target == lyst[position]:
            return position
        position += 1
    return -1
    # best case performace, finds on first item O(1)
    # worst case performance, goes thruogh each item in list O(n)
    # average performance, O((n + 1)/2), ignore the constant because they wont matter in very large datasets, so avg is still O(n)
