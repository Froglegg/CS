from tabulate import tabulate

example = [["MO-123", "Tote-123", "Item-123", 23, "07/04/2021"],
           ["MO-1234", "Tote-1234", "Item-1234", 64, "07/07/2021"]]

print(tabulate(example, headers=[
    "MO (Grandparent) Tag", "Tote (parent)", "Item (child) #", "Quantity (item)", "Need date (grandparent)" "Quantity (child)"], tablefmt='github', numalign="left"))


def binarySearch(target, sortedLyst):
    '''note! This assumes that list is already sorted!!! '''
    iterationTable = []

    left = 0
    right = len(sortedLyst) - 1
    while left <= right:
        midpoint = (left + right) // 2
        iterationTable.append([left, right, midpoint])
        if target == sortedLyst[midpoint]:
            print(tabulate(iterationTable, headers=[
                "Left", "Right", "Midpoint"], tablefmt='github', numalign="left"))
            return midpoint
        elif target < sortedLyst[midpoint]:
            right = midpoint - 1
        else:
            left = midpoint + 1
    print(tabulate(iterationTable, headers=[
        "Left", "Right", "Midpoint"], tablefmt='github', numalign="left"))
    return -1


testLyst = [20, 44, 48, 55, 62, 66, 74, 88, 93, 99]
binarySearch(90, testLyst)
