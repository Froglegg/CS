# Efficient method for finding the GCD
# based on section 4.3.7 in Discrete Math (Rosen)
def Euclidean_GCD(a: int, b: int):
    x = a
    y = b
    while y != 0:
        remainder = x % y
        x = y
        y = remainder
    # gcd(a,b) is xs
    return x


print(Euclidean_GCD(414, 662))
print(Euclidean_GCD(91, 287))
