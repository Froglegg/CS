# Find the power set of any set using the Python programming language.

# Using the Python language to generate the power set of any given set.  There are some assumptions made here.  For example, my powerSet function doesn't check the input list to see whether or not it represents a true list.  For example, the list [1, 2, 3, 3] cannot be used to represent a set because it contains repeated elements.  However, the list [1, 2, 3] may be used to represent a set because the list doesn't contain any repetition of elements.  Sets and power sets are covered in the Chapter 2 homework assignment, along with sequences, matrices, recurrence relations and a few other topics related to sets.

def decimalToBinary(base10, accum=[]):
    if base10 <= 0:
        return accum
    else:
        quotient = base10 // 2
        remainder = base10 % 2
        return decimalToBinary(quotient, [remainder] + accum)


def padWithZeroes(n, binary):
    length = len(binary)
    if length >= n:
        return binary
    else:
        return [0 for _ in range(n - length)] + binary


def selectIfOne(binary, xs):
    if len(binary) != len(xs):
        print()
        print("Your two argument lists must have the same length.  Try again!")
        return
    result = []
    pairedData = zip(binary, xs)
    for (x, y) in pairedData:
        if x == 1:
            result.append(y)
    return result


def powerSet(someSet):
    length = len(someSet)
    size = 2**length
    powerset = []
    for k in range(1, size):
        powerset.append(selectIfOne(padWithZeroes(
            length, decimalToBinary(k)), someSet))
    powerset.insert(0, [])
    sortedSet = []
    for k in range(1 + size):
        sortedSet += sorted([x for x in powerset if len(x) == k])
    return sortedSet


s1 = set(["hey", "there", "bob"])
print(powerSet(s1))
