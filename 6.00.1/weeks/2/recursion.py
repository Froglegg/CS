

def multiply_recurse(a, b):
    """
    recursive function, input a: int, b:int
    returns itself b times
    """
    if b == 1:
        return a
    else:
        return a + multiply_recurse(a, b-1)


multiply_recurse(4, 2)


def factorial_recurse(n):
    """
    input n : int
    factorial (e.g., number! or 7!) is the product of all positive integers less than or equal to a given integer 
    """

    if n == 1:
        return 1
    else:
        return n * factorial_recurse(n-1)


factorial_recurse(7)


def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    else:
        return base * recurPower(base, exp - 1)


print(recurPower(2, 4))
