from linkedStructures import Node

head = Node(None, None)
# create dummy header
head.next = head

probe = head
index = 1
newItem = "foo"

while index >= 0 and probe.next != head:
    probe = probe.next
    index -= 1
probe.next = Node(newItem, probe.next)
print(probe.data)
