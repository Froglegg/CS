def geomean(list):
    total_sum = list[0]
    for i in range(1, len(list)):
        total_sum *= list[i]
    return pow(total_sum, 1.0/(float(len(list))))


print(geomean([5, 20, 27, 32, 35]))
