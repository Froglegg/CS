def in_place_quick_sort(S: list, a: int, b: int):
    '''
    Sorts a list from S[a] to S[b] inclusive using the quick-sort algorithm

    INPUT: List of any length with integer values in the range [1, k]

    OUTPUT: List of integers sorted in ascending order

    Complexity: O(logN)

    Justification: 
    '''
    # range is trivially sorted
    if a >= b:
        return
    # last element of range is pivot
    pivot = S[b]
    # will scan rightward
    left = a
    # will scan leftward
    right = b - 1

    while left <= right:
        # scan until reaching equal value or larger than pibot (or right marker)
        while left <= right and S[left] < pivot:
            left += 1
        # scan until reaching value equal or smaller than pivot
        while left <= right and pivot < S[right]:
            right -= 1
        # scans did not strictly cross
        if left <= right:
            # swap values
            S[left], S[right] = S[right], S[left]
            # shrink range
            left, right = left+1, right - 1

    # put Pivot into its final place (currently marked by left index)
    S[left], S[b] = S[b], S[left]
    # make recursive calls
    in_place_quick_sort(S, a, left-1)
    in_place_quick_sort(S, left+1, b)
    # sorts in place, but also can return
    return S
