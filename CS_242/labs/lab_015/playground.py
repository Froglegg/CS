myList = [2, 3, 5, 7, 11]
yourList = list(myList)
r = yourList is myList
print(r)

setA = set([19, 4, 26, 8])
setB = set()
setB.issubset(setA)
