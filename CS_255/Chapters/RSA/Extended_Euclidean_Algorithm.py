def extended_Euclidean_Algorithm(a, b):
    # Base Case
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = extended_Euclidean_Algorithm(b % a, a)

    # Update x and y using results from recursive call
    x = y1 - (b//a) * x1
    y = x1

    return gcd, x, y
