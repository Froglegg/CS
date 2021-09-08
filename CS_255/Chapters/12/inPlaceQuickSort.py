def in_place_quick_sort(S: list, a: int, b: int):
    '''O log n '''
    ''' sort the list from S[a] to S[b] inclusive using the quick sort algorithm'''
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
        # scands did not strictly cross
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


test = [1, 53, 12, 0, 21, 42, 46, 3, 54, 7]

in_place_quick_sort(test, 0, len(test)-1)
print(test)
