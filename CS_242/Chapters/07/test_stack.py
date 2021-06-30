from array_stack import ArrayStack
from linked_stack import LinkedStack


def test(stackType):
    s = stackType()
    print(f"Len: {len(s)}")
    print(f"empty? {s.isEmpty()}")
    print(f"push 1 - 10: ")
    for i in range(10):
        s.push(i+1)
    print(f"peeking: {s.peek()}")
    print(f"Items (bottom to top): {s}")
    print(f"Length: {len(s)}")
    print(f"Empty: {s.isEmpty()}")
    theClone = stackType(s)

    print(f"Items in clone, bottom to top: {theClone}")
    theClone.clear()
    print(f"Cleared clone, length of clone: {len(theClone)}")

    print(f"Push 11")
    s.push(11)
    print(f"Popping items (top to bottom):", end=" ")
    while not s.isEmpty():
        print(s.pop(), end=" ")
    print(f"\nLength: {len(s)}")
    print(f"Empty? {s.isEmpty()}")


test(ArrayStack)
test(LinkedStack)
