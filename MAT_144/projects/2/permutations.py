# Douglas E. Lewit of Oakton Community College and Northeastern Illinois University.
# Generating lists of permutations in Python.
# This is much easier in Haskell with the use of Applicative Functors or Monads!


from functools import reduce

from sys import setrecursionlimit

setrecursionlimit(10000)  # Increase Python's default stack limit.


class Permutations():

    # __init__ is the default constructor function for all Python classes.
    def __init__(self, lyst, number):
        self.lyst = lyst
        self.number = number
        self.permutations_with_repetition = self.compute_permutations(
            lyst, number)
        self.permutations_without_repetition = list(filter(
            self.all_unique, self.permutations_with_repetition))

    def cartesianProductHelper(self, lyst1, lyst2):
        result = []
        for i in lyst1:
            for j in lyst2:
                result.append([i, j])
        return result

    def flatten(self, nested_lists):
        if not(bool(nested_lists)):
            return nested_lists
        else:
            head = nested_lists[0]
            tail = nested_lists[1:]
            if type(head) == list:
                return self.flatten(head) + self.flatten(tail)
            else:
                return [head] + self.flatten(tail)

    def cartesianProduct(self, args_list):
        try:
            return list(map(self.flatten, reduce(lambda x, y: self.cartesianProductHelper(x, y), args_list)))
        except TypeError:
            return [args_list]

    def compute_permutations(self, lyst, n):
        """The integer n must be greater than 
        or equal to 1."""
        args = [lyst for _ in range(n)]
        return self.cartesianProduct(args)

    def all_unique(self, lyst):
        """This function returns a Boolean value.
           If the list contains all unique elements,
           the function returns True, otherwise False"""
        if not(bool(lyst)):
            return True
        else:
            head = lyst[0]
            tail = lyst[1:]
            if tail.count(head) > 0:
                return False
            else:
                return self.all_unique(tail)


# How many permutations of the letters "ABCDEFG" contain the string "ABC"?
p = Permutations(["A", "B", "C", ], 3)

print(p.permutations_without_repetition)
abc_permutations_list = []

for sublist in p.permutations_without_repetition:
    # build substring from sublist
    substring = "".join(sublist)
    # find method returns -1 if substring is not found in string, else returns index of substring
    if substring.find("ABC") != -1:
        # append sublist to permuations list
        abc_permutations_list.append(sublist)

print(len(abc_permutations_list))
print(abc_permutations_list[-1])
