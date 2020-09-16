# A clever mathematical trick (due to Euclid) makes it easy to find greatest common divisors. Suppose that a and b are two positive integers:

# If b = 0, then the answer is a

# Otherwise, gcd(a, b) is the same as gcd(b, a % b)


def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    else:
        print(f"A is {a} and B is {b}")
        return gcdRecur(b, a % b)


gcdRecur(9, 12)
