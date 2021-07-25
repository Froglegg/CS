class Node(object):
    '''represents singly linked node'''

    def __init__(self, data, next=None) -> None:
        super().__init__()
        self.data = data
        self.next = next
