def union(setA: set, setB: set):
    return setA.union(setB)


def intersection(setA: set, setB: set):
    return setA.intersection(setB)


def difference(setA: set, setB: set):
    return setA.difference(setB)


def symmetricDifference(setA: set, setB: set):
    return setA.symmetric_difference(setB)


def singleAttributeSubset(attribute: str, team: dict):
    attributeSet = set()

    for teamMember in team.items():
        if attribute in teamMember[1]:
            attributeSet.add(teamMember[0])

    return attributeSet


setA = set({1, 3, 10, 0})
setB = set({2, 7, -4})

print(setA.intersection(setB))
blnCheck1 = setA.isdisjoint(setB)
blnCheck2 = setA.issubset(setB)


print(blnCheck1 and blnCheck2)
print(blnCheck1 or blnCheck2)
