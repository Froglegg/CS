import heapq

'''Heapq module provides functions that allow a standard Python list to be managed as a heap.
elements serve as their own key, however
'''
example = [44, 43, 51, 42, 3, 40, 48, 36, 10, 14, 50, 39, 45, 33,
           32, 31, 28, 4, 34, 10, 2, 7, 22, 18, 53, 5, 4, 40, 1, 17, 8, 9]

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
