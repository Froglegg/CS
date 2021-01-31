# to find a sum of a sequence of numbers, don't do loops, just use this Gauss formula
def gauss_sum(min, max):
    term1 = max + min
    term2 = max - min
    print(term1, term2)
    sum = (term1 * (term2+1)) / 2
    return sum


print(gauss_sum(37, 87))
