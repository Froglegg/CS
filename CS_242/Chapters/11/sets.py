A = set([0, 1, 2])
B = set([2, 3, 4])
1 in A

# intersection
print(A & B)
# union
print(A | B)
# difference
print(A-B)
# isSubset
print(A.issubset(B))

S = set([3, 9, 6])
S.add(6)
S.add(4)
S.remove(6)

print(S)
