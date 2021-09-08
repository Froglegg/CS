# Lab1_Crowley

from os import listdir
from MinHeap import MinHeap


def sumOfK(k: int, heap: MinHeap, unsortedList: list) -> tuple:
    '''
    sumOfK uses a loop to determine whether there exists a pair of integers in a
    list of integers such that the sum of integer A and integer B are equal to a given integer k

    Inputs: target integer k, sorted list of integers (minHeap), and unsorted list (to return in tuple data string)
    Output: returns a tuple with the target k integer, the sorted integer list, the unsorted integer list, a "yes" or "no" indicating whether a pair of integers exists such that
    integer A + integer B are equal to the given input k, and a string that displays the two integers and their sum.

    Preconditions: input k must be an integer, and input heap must be sorted

    Complexity: Linear O(n)
    Justification: The while loop used within the body of this function will never loop more than n times, where n is the length of the heap being looped through 
    We increase the left pointer position and decrease the right pointer position each time we find a sum, 
    or we increase the left pointer position if the sum is less than the target constant k, or decrease the right pointer in the case that the sum of the two integers is greater than the target constant k
    Because the min heap is already sorted, we are able to compare each element with one another in the list in an O(n) fashion by following this method.
    '''

    def calculateSum(a, b, k) -> str or bool:
        if a + b == k:
            return f"{a} + {b} = {k}"
        return False

    p1Pos = 0
    p2Pos = len(heap)-1

    p1 = heap[p1Pos]
    p2 = heap[p2Pos]

    curPos = len(heap)-1
    # using a set will enable us to prevent duplicates, i.e. in the case of k = 24 and there are two "12" integers in the list. We don't need to see 12+12 = 24 twice.
    resultList = set()

    # loops will never exceed O(n)
    while curPos >= 0:
        sum = calculateSum(p1, p2, k)
        # If we find the sum, increase the left pointer position and decrease the right pointer position
        if sum:
            resultList.add(sum)
            p2Pos -= 1
            p1Pos += 1
            p1 = heap[p1Pos]
            p2 = heap[p2Pos]
            curPos -= 1
        # if the sum is greater than the target k, decrease pointer 2 position to the left and set p2 pointer to that value
        elif p1 + p2 > k:
            p2Pos -= 1
            p2 = heap[p2Pos]
            curPos -= 1

        # if the sum is less than the target k, increase pointer 1 position to the right and set p1 pointer to that value
        elif p1 + p2 < k:
            p1Pos += 1
            p1 = heap[p1Pos]
            curPos -= 1

    # if no results, return false result
    if len(resultList) < 1:
        return (str(k), f"{unsortedList}", f"{heap}", "No", "")
    else:
        return (str(k), f"{unsortedList}", f"{heap}", "Yes", resultList)


def main():
    '''
    This implementation uses a min-heap, which has a logarithmic O(logN) insertion
    My minHeap design follows patterns I learned in CS_242 and by following Lambert: Fundamentals of Python Data Structures
    '''
    resultList = []

    for file in listdir("."):
        # find all files in current directory that end in .txt

        if file.startswith("in") and file.endswith(".txt"):

            # break into list of lines
            lines = [line.strip() for line in open(file, 'r')]
            unsortedList = [int(i) for i in lines[2].split(" ")]
            # execute sumOfK function using second and third lines (target constant and list of integers respectively) and append result to resultsList
            resultList.append(
                sumOfK(int(lines[1]),  MinHeap(unsortedList), unsortedList))

    # for each result in result list, write output file
    for idx, result in enumerate(resultList):

        with open(f"out{idx + 1}.txt", 'w') as f:

            f.writelines(f'{s}\n' for s in result)


if __name__ == "__main__":
    main()
