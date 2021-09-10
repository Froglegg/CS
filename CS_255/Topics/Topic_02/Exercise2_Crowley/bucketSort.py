def bucketSort(sequence: list[int], k: int):
    '''

    INPUT: List of any length with integer values in the range [1, k]

    OUTPUT: List of integers sorted in ascending order

    Complexity: O(2(k+n)), or just O(n) linear if we ignore the constants 2 and k (which I don't think we should, as k could equal 1 billion! This is why bucket sort is only good for a low range of integer values k, and great also if its a short sequence of integers)

    Justification: Step 1 is O(k), step 2 is O(n), and step 3 is O(n+k). Adding all of these together results in O(k) + O(n) + O(k+n) = O(2(k+n)) 
    '''

    # list to store sorted values, O(1)
    sortedList = []

    # 1) Array initialization of size k, fill with zeroes. This will be our "bucket" list
    # This operation is constant O(k), where k is the upper limit of the range of integer values. Adding +1 to k ensures we don't get an indexError.
    buckets = [0 for _ in range(k+1)]

    # 2) For each integer in the sequence, set its corresponding bucket buckets[integer] to bucket[integer] + 1
    # This operation is O(n), where n is the length of the sequence to be sorted
    for integer in sequence:
        buckets[integer] = buckets[integer] + 1

    # 3) For each index in the range(1..k), for each iteration in range(buckets[index]), append that bucket's index to sortedList
    # This operation has two steps. First step, checking buckets for all non-zero elements is O(k).

    # The second step, appending bucket index to sortedList, is O(n) for all non-zero elements. So the total running time for this operation is O(n+k)
    for idx in range(0, k):
        if buckets[idx] != 0:
            for _ in range(buckets[idx]):
                sortedList.append(idx)

    return sortedList

    # step 1 is O(k), step 2 is O(n), and step 3 is O(n+k). Adding all of these together results in O(k) + O(n) + O(k+n) = O(2(k+n))
