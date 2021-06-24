def swap(lyst, i, j):
    ''' exchanges items at positions i and j '''
    # you could say lyst[i], lyst[j] = lyst[j], lyst[i] but this code shows what going
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp


def selectionSort(lyst):
    i = 0
    # do n - 1 searches
    while i < len(lyst)-1:
        # for the smallest
        minIndex = i
        j = i + 1
        while j < len(lyst):
            if lyst[j] < lyst[minIndex]:
                minIndex = j
            j += 1
        if minIndex != i:
            swap(lyst, minIndex, i)
        i += 1


lyst = [3, 2, 5, 1, 4]
selectionSort(lyst)
print(lyst)
# selection sort is O(n^2)


def bubbleSort(lyst):
    n = len(lyst)
    while n > 1:
        i = 1
        while i < n:
            if lyst[i] < lyst[i-1]:
                swap(lyst, i, i-1)
            i += 1
        n -= 1


def insertionSort(lyst):
    i = 1
    while i < len(lyst):
        itemToInsert = lyst[i]
        j = i - 1
        while j >= 0:
            if itemToInsert < lyst[j]:
                lyst[j+1] = lyst[j]
                j -= 1
            else:
                break
        lyst[j+1] = itemToInsert
        i += 1
