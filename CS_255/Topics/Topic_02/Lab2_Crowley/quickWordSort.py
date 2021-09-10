from random import randint
from alphabet_cipher import convert_word_to_int

iterations = 0


def quickWordSort(wordList: list[str]) -> tuple[list, str]:
    '''
    Sorts a list of words ascending from using a randomized, in-place implementation of the quick-sort algorithm. Best used for large datasets. 

    INPUT: List of any length with word (string) values

    OUTPUT: Mutates list directly, however also returns tuple of sorted list and number of iterations. 

    Complexity: very reliably O(n*logN + 2n) running time, very rarely worst case O(n^2)

    *** NOTE *** 
    The additional +2n is due to having to convert each word in the word list into word_integers, and then reformat those back into words to print on the way out

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

    if wordList is None or len(wordList) < 2:
        return (wordList, f"iterations: {iterations}")

    cipher_dict = {}
    word_int_list = []
    # O(n) operation to convert all words into integers
    for word in wordList:
        word_int = convert_word_to_int(word)
        word_int_list.append(word_int)
        cipher_dict[word_int] = word.lower()

    # O(n) list comprehension to reformat word integers back to words by referencing cipher_dict
    sorted = [cipher_dict[i] for i in random_in_place_quick_sort(
        word_int_list, 0, len(word_int_list) - 1)]

    return (sorted, f"iterations: {iterations}")


# test = [randint(1, 10000) for _ in range(100)]

# test = quickSort(test)
# print(test)
