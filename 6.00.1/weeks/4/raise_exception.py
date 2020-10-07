def get_ratios(L1, L2):
    """
    Assumes L1 and L2 are lists of equal length of numbers
    Returns list consisting of L1/L2
    """
    ratios = []
    for index in range(len(L1)):
        try:
            ratios.append(L1[index]/float(L2[index]))
        except ZeroDivisionError:
            ratios.append(float('NaN'))
        except:
            raise ValueError("get_ratios called with bad arg")
    return ratios


# get_ratios([1, 2, 3], [3, 2, 1])
# get_ratios([1, 2, 3], [0, 0, 1])
get_ratios([1, "hey", 3], [3, 2, 1])
