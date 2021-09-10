
from alphabet_cipher import convert_word_to_int


def wordSort(lyst: list[str], maxWord: str) -> list[str]:
    '''
    INPUT: List of any length with string values (words) in the range [a, maxWord], where each word is less than or equal to the maxWord (e.g., "zzz")

    OUTPUT: List of lowercase string values (words) sorted in ascending order (case-insensitive)

    Complexity: O(2(k+n)), or just O(n) linear if we ignore the constants 2 and maxWord (which I don't think we should, as k could equal 1 billion! This is why bucket sort is only good for a low range of integer values k, and great also if its a short sequence of integers)

    Justification: Step 1 is O(k), step 2 is O(n), and step 3 is O(n+k). Adding all of these together results in O(k) + O(n) + O(k+n) = O(2(k+n))
    '''

    # list to store sorted values, O(1)
    sortedList = []

    # maxWord integer value, O(1)
    maxWordInt = convert_word_to_int(maxWord)

    # 1) Array initialization of size maxWord, fill with zeroes. This will be our "bucket" list
    # This operation is constant O(maxWordInt + 1), where maxWordInt is the upper limit of the range of converted word integer values. Adding + 1 to ensure we don't get an off-by-one indexError.
    buckets = [0 for _ in range(maxWordInt + 1)]

    # # 2) For each word in the sequence, set its corresponding bucket buckets[wordInt] to bucket[wordInt] + 1
    # # This operation is O(n), where n is the length of the word sequence to be sorted
    # also, create cipher dict for reformatting word integers back into words after we sort
    cipher_dict = {}

    for word in lyst:
        word_int = convert_word_to_int(word)
        buckets[word_int] = buckets[word_int] + 1
        cipher_dict[word_int] = word.lower()

    # 3) Sorting is complete, reformatting to print... For each index in the range(1..maxWordInt), for each iteration in range(buckets[index]), append that bucket's index to sortedList
    # This operation has two steps. First step, checking buckets for all non-zero elements is O(maxWordInt + 1).
    # The second step, appending bucket index to sortedList, is O(n) for all non-zero elements. So the total running time for this operation is O(n+k)
    for idx in range(0, maxWordInt + 1):
        if buckets[idx] != 0:
            for _ in range(buckets[idx]):
                sortedList.append(cipher_dict[idx])

    return sortedList

    # step 1 is O(k), step 2 is O(n), and step 3 is O(n+k). Adding all of these together results in O(k) + O(n) + O(k+n) = O(2(k+n))


# lyst = ["c", "zzA", "aBb", "bAa", "Acd", "B", "CA", "zzz", "ZR", "IL"]
# max_word = "zzz"
# print(wordSort(lyst, max_word))
