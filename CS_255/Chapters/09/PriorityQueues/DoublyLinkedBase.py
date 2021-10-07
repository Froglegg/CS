class _DoublyLinkedBase:

    class _Node:
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next) -> None:
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self) -> None:
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor: _Node, successor: _Node):
        '''add element e between two exisiting nodes and return new node'''
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node: _Node):
        ''' delete non-sentinel node and return its element'''
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        # record deleted element
        element = node._element
        # deprecate node
        node._prev = node._next = node._element = None
        # return deleted element
        return element
