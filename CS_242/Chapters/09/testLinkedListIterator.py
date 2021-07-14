from LinkedList import LinkedList, LinkedListIterator


def test():
    backingStore = LinkedList()
    li = LinkedListIterator(backingStore)
    for i in range(9):
        li.insert(i+1)

    print("Printing numbers 1-9:")
    for i in range(len(backingStore)):
        print(li.next())

    li.first()
    print(f"should be 1: {li.next()}")
    li.next()
    li.insert(1.5)
    print(f"should be 1.5: {li.previous()}")
    li.first()

    print("Printing numbers 1-9, should include 1.5 in second position")
    for i in range(len(backingStore)):
        print(li.next())
    li.first()
    li.next()
    li.next()
    print(f"removing second item, 1.5: {li.remove()}")
    li.first()
    print("Printing numbers 1-9, should NOT include 1.5 in second position")
    for i in range(len(backingStore)):
        print(li.next())
    li.first()
    li.next()
    print(f"replacing 1 with 69")
    li.replace(69)
    li.first()
    print("Printing numbers 1-9, should include 69 in first position")
    for i in range(len(backingStore)):
        print(li.next())
    li.last()
    print(li.previous())
    print("replacing 9 with 69")
    li.replace(69)
    li.last()
    print("Printing numbers descending, should include 69 in first and last positions:")
    for i in range(len(backingStore)):
        print(li.previous())
    print("removing all numbers")
    for i in range(len(backingStore)):
        li.next()
        print(li.remove())
    print(
        f"printing LI has previous, should be false as it is now empty: {li.hasPrevious()}")


test()
