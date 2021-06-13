
# Complete the code below to compute and display the standard deviation of the 	given list of values.

# Note: the standard deviation is the square root of the sum of the square 	differences divided by the length of the list of values.

from math import sqrt
# sample data
data_list = [280, 255, 242, 207, 201]

# determine the mean value
sums = 0
for i in range(len(data_list)):
    sums += data_list[i]

mean = sums / len(data_list)

# for each value, find the square deviation from the mean
difference_squared = 0

for i in range(len(data_list)):
    difference_squared += (data_list[i] - mean) ** 2

# find the square root
print(sqrt(difference_squared))
# returns 66.2872536767062
