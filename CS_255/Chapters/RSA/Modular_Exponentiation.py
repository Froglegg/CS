# in Cryptography, it is important to be able to find modular exponent (b^n mod m) efficiently
# base on section 4.2.4 in Discrete Math (Rosen)
def Modular_Exponentation(b, n, m):
    """
    INPUTS: base b, exponent n, and modulus integer m
    OUTPUTS: remainder of base^exponent divided by m (b^n mod m)
    """
    # conduct binary expansion of integer n, reverse string because we will walk backwards through it
    binaryExpansion = Binary_Expansion_Integer(n)[::-1]
    # set x to 1, initial power to base % modulus
    x = 1
    power = b % m
    for i in binaryExpansion:
        # if character is a 1
        if i == "1":
            # set x to x*power mod m
            x = ((x*power) % m)
        # increment power by power*power % m
        power = ((power*power) % m)

    # x equals b^n % m
    return x


def Binary_Expansion_Integer(num: int):
    if num < 0:
        isNeg = True
        num = abs(num)
    else:
        isNeg = False

    result = ''
    if num == 0:
        result = '0'
    while num > 0:
        result = str(num % 2) + result
        num = num//2
    if isNeg:
        result = '-' + result

    return result


# print(Modular_Exponentation(3, 644, 645))

# print("CORRECT IS")
# # python builtin modular exponentiation
# print(pow(3, 644, 645))
