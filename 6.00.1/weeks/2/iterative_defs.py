def multiply_iter(a, b):
    """
    iterative function, input a: int, b: positive int
    returns a plus itself b times
    """
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result


multiply_iter(4, 2)


def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    result = 1
    while exp > 0:
        result *= base
        exp -= 1
    return result


print(iterPower(2, 3))
