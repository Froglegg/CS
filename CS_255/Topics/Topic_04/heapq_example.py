import heapq

'''Heapq module provides functions that allow a standard Python list to be managed as a heap.
elements serve as their own key, however
'''
example = [13, 21, 16, 24, 31, 33, 14, 19, 68, 65, 26, 32]
print("EXAMPLE")
print(example)

heapq.heapify(example)
print("HEAPED EXAMPLE")
print(example)

print("INSERT 31")
heapq.heappush(example, 31)
print(example)

print("INSERT 14")
heapq.heappush(example, 14)
print(example)
print("\n")

print("BEGIN DELETE MIN")
while len(example) > 0:
    heapq.heappop(example)
    print(f"heap after delete min: {example}")
