class Node:

    # singly linked node
    def __init__(self, data=None):
        self.data = data
        self.next = None


class singly_linked_list:

    def __init__(self):
        # create an empty list
        self.head = None
        self.tail = None
        self.count = 0

    def iterate_item(self):
        # iterate through the list
        current_item = self.head
        while current_item:
            val = current_item.data
            current_item = current_item.next
            yield val

    def append_item(self, data):
        # append items on the list
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.count += 1

    def get_head(self):
        if self.head:
            return str(self.head.data)
        return "No head!"

    def get_tail(self):
        if self.tail:
            return str(self.tail.data)
        return "No tail!"


items = singly_linked_list()
items.append_item("item 1")
items.append_item("item 2")
items.append_item("item 3")
items.append_item("item 4")
items.append_item("item 5")
for val in items.iterate_item():
    print(val)
print("\nhead.data: ", items.get_head())
print("tail.data: ", items.get_tail())
