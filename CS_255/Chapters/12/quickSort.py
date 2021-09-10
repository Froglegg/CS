from random import randint

iterations = 0


def quickSort(S: list[int]) -> tuple[list, str]:
    '''
    Sorts a list of integers ascending from using a randomized, in-place implementation of the quick-sort algorithm. Best used for large datasets. 

    INPUT: List of any length with integer values

    OUTPUT: Mutates list directly, however also returns tuple of sorted list and number of iterations. 

    Complexity: very reliable and expected O(n*logN) running time, very rarely worst case O(n^2)

    Justification: 

    Because we must iterate through each item in a sequence, any sorting algorithm will always be at least O(n)

    Because quick sort is more efficient when the pivot is closer to the median of the sequence or subsequence, randomizing the pivot selection mathematically results in 1/2 chance of making a "good" choice, when a "good" choice is defined by a pivot for which the length of items < pivot is >= 1/4 of the subsequence length and the length of items > pivot is <= 3/4 of the subsequence length. The number of operations that occur here are O(n) linear.

    When recursing through subsequences and creating a relatively balanced tree, we have an O(logN) number of subsequences that require processing. So O(n) * O(logN) = O(n*logN)
    '''
    def random_in_place_quick_sort(S, left, right):
        ''' sort the list from S[a] to S[b] inclusive using the quick sort algorithm'''
        global iterations
        iterations += 1
        # range is trivially sorted, base case
        if left >= right:
            return

        # select random pivot
        pivot_idx = randint(left, right)

        # swap pivot with left
        S[left], S[pivot_idx] = S[pivot_idx], S[left]

        # create subsequences
        idx = left
        for i in range(left+1, right+1):
            if S[i] < S[left]:
                idx += 1
                S[idx], S[i] = S[i], S[idx]

        # put pivot (currently marked by left index) into proper place
        S[idx], S[left] = S[left], S[idx]

        # recursively sort left and right subsequences
        random_in_place_quick_sort(S, left, idx-1)
        random_in_place_quick_sort(S, idx + 1, right)

        return S

    if S is None or len(S) < 2:
        return (S, f"iterations: {iterations}")

    sorted = random_in_place_quick_sort(S, 0, len(S) - 1)
    return (sorted, f"iterations: {iterations}")


# test = [randint(1, 10000) for _ in range(100)]

# test = quickSort(test)
# print(test)
