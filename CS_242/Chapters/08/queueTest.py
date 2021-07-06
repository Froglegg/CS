
from linked_queue import LinkedQueue
from priority_linked_queue import PriorityLinkedQueue
from comparable import Comparable


def test(stackType):
    s = stackType()
    print(f"Len: {len(s)}")
    print(f"empty? {s.isEmpty()}")
    print(f"add 1 - 10: ")
    for i in range(10):
        if stackType == PriorityLinkedQueue:
            s.add(Comparable(i+1, i % 2))
        else:
            s.add(i+1)
    print(f"peeking: {s.peek()}")
    print(f"Items (rear to front): {s}")
    print(f"Length: {len(s)}")
    print(f"Empty: {s.isEmpty()}")
    print(f"Popping items (front to rear):", end=" ")
    while not s.isEmpty():
        print(s.pop(), end=" ")
    print(f"\nLength: {len(s)}")
    print(f"Empty? {s.isEmpty()}")


test(PriorityLinkedQueue)
