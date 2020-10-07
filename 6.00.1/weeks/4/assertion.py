def avg(grades):
    assert len(grades) != 0, "no grades data"
    return sum(grades)/len(grades)


print(avg([1, 2]))
print(avg([]))
