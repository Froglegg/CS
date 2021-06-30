from tabulate import tabulate


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
            return f"Index of {target} is {midpoint}"
        elif target < sortedLyst[midpoint]:
            right = midpoint - 1
        else:
            left = midpoint + 1
    print(tabulate(iterationTable, headers=[
        "Left", "Right", "Midpoint"], tablefmt='github', numalign="left"))
    return -1


testLyst = [12, 18, 23, 25, 29, 32, 35, 40, 58, 66]
binarySearch(18, testLyst)
