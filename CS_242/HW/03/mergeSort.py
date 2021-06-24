from array import Array


def mergeSort(lyst):
    # lyst is list being sorted
    # copyBuffer temp space needed during merge
    copyBuffer = Array(len(lyst))
    mergeSortHelper(lyst, copyBuffer, 0, len(lyst)-1)


def mergeSortHelper(lyst, copyBuffer, low, high):
    #  low, high bounds of sublist
    # middle midpoint of sublist
    if low < high:
        middle = (low+high)//2
        mergeSortHelper(lyst, copyBuffer, low, middle)
        mergeSortHelper(lyst, copyBuffer, middle + 1, high)
        merge(lyst, copyBuffer, low, middle, high)


def merge(lyst, copyBuffer, low, middle, high):
    # low begining of first sorted sublist
    # end of first sorted sublist
    # middle + 1 is beginning of second sorted sublist
    # high is end of second sorted sublist
    # initialize i1 and i2 to the first items in each sublist
    i1 = low
    i2 = middle + 1
    #  interleave items from the sublists into the copyBuffer in such a way that order is maintained
    for i in range(low, high+1):
        if i1 > middle:
            # first sublist exhausted
            copyBuffer[i] = lyst[i2]
            i2 += 1
        elif i2 > high:
            # second sublist exhausted
            copyBuffer[i] = lyst[i2]
            i1 += 1
        elif lyst[i1] < lyst[i2]:
            # item in first sublist <
            copyBuffer[i] = lyst[i1]
            i1 += 1
        else:
            # item in second sublist <
            copyBuffer[i] = lyst[i2]
    # copy sorted items back to proper position in list
    for i in range(low, high+1):
        lyst[i] = copyBuffer[i]
