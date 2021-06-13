# define a list
oddSquares = []
# populate the list
for x in range(1, 11):
    if (x % 2 == 1):
        oddSquares.append(x**2)
# display the list contents
print(oddSquares)
print(f"length of list is: {len(oddSquares)}")
# prints
# [1, 9, 25, 49, 81]
# length of list is: 5
