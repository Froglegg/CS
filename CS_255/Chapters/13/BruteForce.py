def BruteForce(T, P):
    '''returns the lowest index of T text at which substring P begins (or else -1)'''
    n, m = len(T), len(P)
    # try every potential starting index within T
    for i in range(n-(m+1)):
        # k is an index into pattern P
        k = 0
        # kth character of P matches
        while k < m and T[i+k] == P[k]:

            k += 1
        # if we reach the end of the pattern
        if k == m:
            # substring T[i:i+m] matches P
            return i
    # else, failed to find a match starting with any i
    return -1


test = "a test string"
substring = "str"
print(BruteForce(test, substring))
