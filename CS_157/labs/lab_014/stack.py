class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def peek(self):
        return self.items[len(self.items) - 1]

    def pop(self):
        return self.items.pop()

    def push(self, item):
        try:
            if self.atCapacity():
                raise Exception
            else:
                self.items.append(item)
        except Exception:
            print("Stack overflow! Please pop an item before pushing")

    def size(self):
        return len(self.items)

    def atCapacity(self):
        return len(self.items) >= 10
