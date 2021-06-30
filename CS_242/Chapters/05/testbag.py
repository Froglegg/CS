from arrayBag import ArrayBag
from linkedBag import LinkedBag


def test(bagType):
    print("testing ", bagType)
    lyst = [2013, 61, 1973]
    print(f"List of items is {lyst}")
    b1 = bagType(lyst)
    print(f"Length, expect 3: {len(b1)}")
    print(f"Bag string: {b1}")
    print(f"2013 in bag, expect true: {2013 in b1}")
    print(f"2012 in bag, expect false: {2012 in b1}")
    print(f"expect the items to be on separaet lines: ")
    for item in b1:
        print(item)
    b1.clear()
    print(f"Clearing the bag, expect empty: {b1}")
    b1.add(25)
    b1.remove(25)
    print(f"Adding then removing 25, expect empty: {b1}")
    b1 = bagType(lyst)
    b2 = bagType(b1)

    print(f"Cloning the bag, expect true for == : {b1 == b2}")
    print(f"Expect false for is: {b1 is b2}")
    print(f"+ the two bags, expect two of each item: {b1 + b2}")

    for item in lyst:
        b1.remove(item)

    print(f"Removing all items, expect empty: {b1}")

    # print(f"Removing non-existant item, expect crash with keyError: ")
    # b2.remove(99)


test(LinkedBag)
