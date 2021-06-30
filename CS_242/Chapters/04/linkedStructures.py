class Node(object):
    '''represents singly linked node'''

    def __init__(self, data, next=None) -> None:
        super().__init__()
        self.data = data
        self.next = next


# empty link
node1 = None
# A node with data and an empty link
node2 = Node("A", None)
# A node with data and link to node2
node3 = Node("B", node2)

node1 = Node("C", node3)
