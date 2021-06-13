def triangularNumbers(nth):
    return ((pow(nth, 2)) + nth)/2


triangleNums = []
# populate the list
for nth in range(1, 11):
    triangleNums.append(triangularNumbers(nth))

# display the list elements
print(triangleNums)

# returns [1.0, 3.0, 6.0, 10.0, 15.0, 21.0, 28.0, 36.0, 45.0, 55.0]
# 10th element is 55.0
