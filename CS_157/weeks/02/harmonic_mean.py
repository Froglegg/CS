def harmonic_mean(list):
    denom = (1 / list[0])
    for i in range(1, len(list)):
        denom += (1/list[i])
    return (len(list)/denom)


print(harmonic_mean([1, 4, 4]))
