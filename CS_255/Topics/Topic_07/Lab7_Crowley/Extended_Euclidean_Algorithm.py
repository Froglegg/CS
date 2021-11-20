# Based on https://www.geeksforgeeks.org/python-program-for-basic-and-extended-euclidean-algorithms-2/
# note
# The Euclidean Algorithm computes for us the greatest common divisor of two integers.
# The extended version actually gives integers x and y such that ax+by=gcd(a,b)

def extended_Euclidean_Algorithm(self, a, b):
    # Base Case
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = self.extended_Euclidean_Algorithm(b % a, a)

    # Update x and y using results from recursive call
    x = y1 - (b//a) * x1
    y = x1
    # return gcd of a and b, as well as the integers x and y such that ax+by=gcd(a,b)
    return gcd, x, y
