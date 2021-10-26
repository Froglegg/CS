# Richard Hayes Crowley
# MAT_144_project_1

# 9.  Given a list of integers and an element x,
# locate x in this list using a recursive implementation of linear search.
def recursive_linear_search(index, stop, x, lyst):
    if lyst[index] == x:
        return index
    elif index == stop:
        raise Exception("Item not found!")
    return recursive_linear_search(index + 1, stop, x, lyst)


lyst = [i for i in range(10)]
print(recursive_linear_search(0,  11, lyst))
