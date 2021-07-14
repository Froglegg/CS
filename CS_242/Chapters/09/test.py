from ArrayList import ArrayList, ArrayListIterator


def testList(listType):
    s = listType()
    print(f"Len: {len(s)}")
    print(f"empty? {s.isEmpty()}")
    print(f"add 1 - 9: ")
    for i in range(9):
        s.add(i+1)

    print(f"Items (rear to front): {s}")

    print(f"Length: {len(s)}")

    print(f"Empty: {s.isEmpty()}")

    print("popping first item, 1")
    s.pop(0)
    print(s)
    print("popping last item, 9")
    s.pop()
    print(s)
    print("adding 69 to end")
    s.add(69)
    print(s)
    print("popping 69 from end")
    s.pop()
    print(s)
    print(f"Length: {len(s)}")
    print('inserting 69 to second to last position')
    s.insert(6, 69)
    print(s)
    print('popping 69 from second to last position')
    s.pop(6)
    print(s)

    print(f"Popping items (front to rear):", end=" ")

    while not s.isEmpty():
        print(s.pop(), end=" ")
    print(f"\nLength: {len(s)}")
    print(f"Empty? {s.isEmpty()}")


# testList(ArrayList)


def testIterator(iterator, listType):
    backingStore = listType()
    li = iterator(backingStore)
    print("Adding numbers 1-9 to store")
    for i in range(9):
        li.insert(i+1)
    print(f"List iterator has next: {li.hasNext()}")
    print(f"Next item: {li.next()}")
    print(f"Next item: {li.next()}")
    print(f"Next item: {li.next()}")
    print(f"Previous item: {li.previous()}")
    print(f"Previous item: {li.previous()}")
    print(f"inserting 1.5 at position {li.getPosition()}")
    li.insert(1.5)
    print(f"next item should be 1.5: {li.next()}")
    print(f"Previous item should be 1.5: {li.previous()}")
    print(f"next item should be 1.5: {li.next()}")
    print(f"next item should be 2: {li.next()}")
    print(f"Going to end of list: {li.last()}")
    print(f"prev item should be last item in list, #9: #{li.previous()}")

    print(f"replacing with 69", {li.replace(69)})
    print(f"next, should b 69 {li.next()}")
    print(f"removing 69: {li.remove()}")
    print(f"previous: {li.previous()}")
    print(f"inserting 69, {li.insert(69)}")
    print(f"next, 69: {li.next()}")
    print(f"Going to first position, and then removing all elements")
    li.first()

    for i in range(len(backingStore)):
        li.next()
        print(li.remove())
    print(f"Has next should be false: {li.hasNext()}")
    print("Going to first position, adding numbers one through 9")
    li.first()
    for i in range(9):
        li.insert(i+1)
    print("Going to second position and adding 1.5")
    li.next()
    li.next()
    li.insert(1.5)
    print('going to last position and adding numbers 1-9 again')
    li.last()
    for i in range(9):
        li.insert(i+1)
    print('going to first position and iterating through each number, should have two set of numbers 1-9 and first set include 1.5')
    li.first()
    for i in range(len(backingStore)):
        print(li.next())
    print('removing all items')
    li.first()

    for i in range(len(backingStore)):
        li.next()
        print(li.remove())


testIterator(ArrayListIterator, ArrayList)
