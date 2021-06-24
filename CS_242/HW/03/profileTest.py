from profiler import Profiler

import random


def quicksort(lyst):
    quicksortHelper(lyst, 0, len(lyst)-1)


def quicksortHelper(lyst, left, right):
    if left < right:
        pivotLocation = partition(lyst, left, right)
        quicksortHelper(lyst, left, pivotLocation - 1)
        quicksortHelper(lyst, pivotLocation + 1, right)


def partition(lyst, left, right):
    # find the pivot and exchange it with the last item
    middle = (left + right) // 2
    pivot = lyst[middle]
    lyst[middle] = lyst[right]
    lyst[right] = pivot
    # set boundary point to first position
    boundary = left
    # move items less than pivot to the left
    for index in range(left, right):
        if lyst[index] < pivot:
            swap(lyst, index, boundary)
            boundary += 1
    # exchange pivot item and boundary item
    swap(lyst, right, boundary)
    return boundary


def swap(lyst, i, j):
    ''' exchanges items at positions i and j '''
    # you could say lyst[i], lyst[j] = lyst[j], lyst[i] but this code shows what going
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp


p = Profiler()
p.test(quicksort, size=15, comp=True, exch=True, trace=False)


def main(size=20, sort=quicksort):
    lyst = []
    for count in range(size):
        lyst.append(random.randint(1, size+1))
    print(lyst)
    sort(lyst)
    print(lyst)


if __name__ == "__main__":
    main()
