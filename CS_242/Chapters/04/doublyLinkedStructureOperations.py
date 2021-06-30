from doublyLinkedStructures import TwoWayNode

#  create a doubly linked struct with one node
head = TwoWayNode(1)
tail = head

# add four nodes to the end of the struct
for data in range(2, 6):
    tail.next = TwoWayNode(data, tail)
    tail = tail.next

# print the contents of the struct in reverse order
probe = tail
while probe != None:
    print(probe.data)
    probe = probe.previous
