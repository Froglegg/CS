from linkedStructures import Node
# one pointer or ref, head, generates the linked strucutre.
# The pointer is manipulated in such a way that the most recently insterted item is awlways at the beginning of the strucutre
head = None
# add five nodes to beginning of linked structure
for count in range(1, 6):
    head = Node(count, head)

# print contents of structure
# head pointer is reset to the next node, until the head pointer becomes none (as it was in the beginning)
# thus as the end of this process, the nodes are effectively ddeleted from the linked strucutre and are recycled during the next garbage collection
# while head != None:
#     print(head.data)
#     head = head.next

# traversals
# use a probe pointer, so we don't delete the nodes as we traverse the structure

# probe = head
# while probe != None:
#     print(probe.data)
#     probe = probe.next

# searching
# always a sequential O(n) linear operation... not as efficient as array structures
# probe = head
# targetItem = 3
# while probe != None and targetItem != probe.data:
#     probe = probe.next
# if probe != None:
#     print(f"target item found: {str(probe.data)}")
# else:
#     print("target item not in linked structure")

# replacement
# also sequential O(n) linear, not as efficient as arrays
# probe = head
# targetItem = 3
# newItem = "foo"
# while probe != None and targetItem != probe.data:
#     probe = probe.next

# if probe != None:
#     probe.data = newItem
#     print(f"item replaced with {newItem}")
# else:
#     print('replacement item target not found')

# insertion at beginning, uses constant time and memory! better than arrays which use linear time/memory to insert at any position, since the array needs to be resized and each data item in the array needs to be copied into the next position...
# head = Node(newItem, head)

# insertion at end of struct
# head pointer is either None, and so you just set the head pointer to the new node
# or, head pointer is not None (null), and you simply use the traversal pattern
# newItem = "foo"
# newNode = Node(newItem)
# if head is None:
#     head = newNode
# else:
#     probe = head
#     while probe.next != None:
#         probe = probe.next
#     probe.next = newNode

# remove from beginning
# resetting head to the next node deletes the previous node.
# removedItem = head.data
# head = head.next

# removing at end, linear O(n) in time and constant in memory O(k)
# removedItem = head.data
# if only one node
# if head.next is None:
#     head = None
# else there is more than one node, search structure for secont to last node and set its next pointer to None
# else:
#     probe = head
#     while probe.next.next != None:
#         probe = probe.next
#     removedItem = probe.next.data
#     probe.next = None
#     print(removedItem)

# inserting at any position
# linear time performance, konstant memory
# index = 3
# newItem = "foo"
# if head is None or index <= 0:
#     head = Node(newItem, head)
# else:
    # search for note at position index - 1 or the last position
    # probe = head
    # while index > 1 and probe.next != None:
    #     probe = probe.next
    #     index -= 1
    # insert new node at position index -1
    # or last position
    # probe.next = Node(newItem, probe.next)

# removing at any position
# index = 3
# if only one item or index is first position
# if index <= 0 or head.next is None:
#     removedItem = head.data
#     head = head.next
#     print(removedItem)
# else:
    # search for node at position index -1 or
    # the next to last position
    # probe = head
    # while index > 1 and probe.next.next != None:
    #     probe = probe.next
    #     index -= 1
    # removedItem = probe.next.data
    # probe.next = probe.next.next
    # print(removedItem)
