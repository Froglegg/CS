from UnsortedPriorityQueue import UnsortedPriorityQueue


def pq_sort(C):
    n = len(C)
    P = UnsortedPriorityQueue()
    for j in range(n):
        element = C.delete(C.first())
        # use element as key and value
        P.add(element, element)
    for j in range(n):
        (k, v) = P.remove_min()
        # store smallest remaining element in C
        C.add_last(v)


pq = UnsortedPriorityQueue()

for i in range(9, 0, -1):
    pq.add(i, i)

for i in pq:
    print(i)

pq_sort(pq._data)

for i in pq:
    print(i)
