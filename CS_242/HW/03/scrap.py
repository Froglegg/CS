minIndex = 0
currentIndex = 1
lyst = [1, 2, 3, 4, 5]
while currentIndex < len(lyst):
    if (lyst[currentIndex] < lyst[minIndex]):
        minIndex = currentIndex
        currentIndex += 1
print(minIndex)
