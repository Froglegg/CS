from LinkedQueue import LinkedQueue


def queue_quick_sort(S: LinkedQueue):
    ''' running time is O(n^2) worst case in this implementation...
    In practice however, when L and G are similar size, the performance is O(nLogn)
    '''
    n = len(S)
    if n < 2:
        return

    # pivot
    p = S.first()
    # less than pivot
    L = LinkedQueue()
    # equal to pivot
    E = LinkedQueue()
    # greater than pivot
    G = LinkedQueue()

    while not S.is_empty():

        if S.first() < p:
            L.enqueue(S.dequeue())
        elif p < S.first():
            G.enqueue(S.dequeue())
        else:
            E.enqueue(S.dequeue())

    # recursion
    queue_quick_sort(L)
    queue_quick_sort(G)

    # concatenate results, less than, equal to, and then greater than in that order
    while not L.is_empty():
        S.enqueue(L.dequeue())
    while not E.is_empty():
        S.enqueue(E.dequeue())
    while not G.is_empty():
        S.enqueue(G.dequeue())

    # return sorted sequence
    return S


# testQueue = LinkedQueue([1, 2, 3])
# for i in range(10, 0, -1):
#     testQueue.enqueue(i)

print(testQueue)
queue_quick_sort(testQueue)
print(testQueue)
