import heapq

'''
Read the numbers from the file and create a heap. 
Insert an element by an element from left to right from the file to the heap.
The minimum elementmust be in the root of the heap tree.
'''

in4 = [13, 21, 16, 24, 31, 33, 14, 19, 68, 65, 26, 32]
heap = []

for i in in4:
    heapq.heappush(heap, i)
    print(heap)
