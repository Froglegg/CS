from random import shuffle, sample
from tabulate import tabulate
import time
from english_words import english_words_lower_alpha_set


# a bit expensive to generate a list from such a large set, but using random sampler on sets throws a deprecation warning, and this won't make much difference to a user anyway
english_word_list = list(english_words_lower_alpha_set)


class Algorithims(object):
    def __init__(self, lyst=[]) -> None:
        super().__init__()
        self.lyst = lyst
        self.iterationTable = []
        self.startTime = ""
        self.timeElapsed = ""

    def printList(self):
        print(self.lyst)

    def generateNumericList(self, size=10):
        self.lyst = list(range(1, size+1))
        shuffle(self.lyst)
        print(f"List generated...\n")

    def generateWordList(self, size=10):
        print(size)
        wordList = sample(english_word_list, size)
        self.lyst = wordList
        print(f"List generated... \n")

    def __generateTable(self, headers, table):
        self.iterationTable = tabulate(
            table, headers, tablefmt='github', numalign="left")

    def __startClock(self):
        self.startTime = time.time()

    def __stopClock(self):
        self.timeElapsed = time.time() - self.startTime
        self.startTime = None

    def __swap(self, i, j):
        ''' exchanges items at positions i and j '''
        # you could say lyst[i], lyst[j] = lyst[j], lyst[i] but this code shows what going
        temp = self.lyst[i]
        self.lyst[i] = self.lyst[j]
        self.lyst[j] = temp

    def linearSearch(self, target):
        ''' mimic python's 'in' operator return position of target item if found, else return -1'''
        self.__startClock()

        position = 0

        while position < len(self.lyst):
            if target == self.lyst[position]:
                self.__stopClock()
                print(
                    f"Linear Search complete, {target} found in position {position}. Time elapsed: {self.timeElapsed:0.6f}")
                return 1
            position += 1
        self.__stopClock()
        print(
            f"Linear Search complete, {target} not found.\nTime elapsed: {self.timeElapsed}")
        return -1

    def binarySearch(self, target):
        '''note! This assumes that the list is already sorted!!! '''

        print("Running binary search, sorting list using quickSort and running search...")
        self.quicksort()
        sortedLyst = self.lyst

        self.__startClock()

        iterationTable = []
        left = 0
        right = len(sortedLyst) - 1

        while left <= right:
            midpoint = (left + right) // 2
            iterationTable.append([left, right, midpoint])
            if target == sortedLyst[midpoint]:
                self.__stopClock()
                print("Finished! \nBinary search iteration table\n")
                self.__generateTable(headers=[
                    "Left", "Right", "Midpoint"], table=iterationTable)
                print(self.iterationTable)
                print(
                    f"Index of {target} is {midpoint}. Number of iterations: {len(iterationTable)}. Time elapsed: {self.timeElapsed:0.6f}")
                return 1
            elif target < sortedLyst[midpoint]:
                right = midpoint - 1
            else:
                left = midpoint + 1
        self.__stopClock()
        self.__generateTable(headers=[
            "Left", "Right", "Midpoint"], table=iterationTable)
        print(self.iterationTable)
        print(
            f"Finished!\n{target} not found. Time elapsed: {self.timeElapsed:0.6f}")
        return -1

    def bubbleSort(self):
        self.__startClock()
        n = len(self.lyst)
        while n > 1:
            i = 1
            while i < n:
                if self.lyst[i] < self.lyst[i-1]:
                    self.__swap(i, i-1)
                i += 1
            n -= 1
        self.__stopClock()
        print(f"Bubble sort complete, time elapsed: {self.timeElapsed:0.6f}")

    def selectionSort(self):
        self.__startClock()
        lyst = self.lyst
        i = 0
        # do n - 1 searches
        while i < len(lyst)-1:
            # for the smallest item
            minIndex = i
            j = i + 1
            while j < len(lyst):
                if lyst[j] < lyst[minIndex]:
                    minIndex = j
                j += 1
            if minIndex != i:
                self.__swap(minIndex, i)

            i += 1
        self.__stopClock()
        print(
            f"Selection sort complete, time elapsed: {self.timeElapsed:0.6f}")

    def insertionSort(self):
        self.__startClock()
        lyst = self.lyst
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
        self.__stopClock()
        print(
            f"Insertion sort complete, time elapsed: {self.timeElapsed:0.6f}")

    def quicksort(self):
        lyst = self.lyst
        self.__startClock()
        self.quicksortHelper(lyst, 0, len(lyst)-1)
        self.__stopClock()
        print(f"Quick sort complete, time elapsed: {self.timeElapsed:0.6f}")

    def quicksortHelper(self, lyst, left, right):
        if left < right:
            pivotLocation = self.partition(lyst, left, right)
            self.quicksortHelper(lyst, left, pivotLocation - 1)
            self.quicksortHelper(lyst, pivotLocation + 1, right)

    def partition(self, lyst, left, right):
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
                self.__swap(index, boundary)
                boundary += 1
        # exchange pivot item and boundary item
        self.__swap(right, boundary)

        return boundary
