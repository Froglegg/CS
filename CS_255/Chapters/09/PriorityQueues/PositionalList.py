from DoublyLinkedBase import _DoublyLinkedBase


class PositionalList(_DoublyLinkedBase):
    '''A sequential container of elements allowing positional access'''
    # nested position class
    class Position:
        '''An Abstraction representing the location of a single element'''

        def __init__(self, container, node: _DoublyLinkedBase._Node) -> None:
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other: _DoublyLinkedBase._Node):
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not(self == other)
    # utility method

    def _validate(self, p: Position):
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper position type")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._node._next is None:
            raise ValueError("p is no longer valid")
        return p._node

    # utility method
    def _make_position(self, node: _DoublyLinkedBase._Node):
        if node is self._header or node is self._trailer:
            # boundary error
            return None
        else:
            # legit position
            return self.Position(self, node)

    # accessors
    def first(self):
        return self._make_position(self._header._next)

    def last(self):
        return self._make_position(self._trailer._prev)

    def before(self, p: Position):
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p: Position):
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    # mutators
    def _insert_between(self, e, predecessor: _DoublyLinkedBase._Node, successor: _DoublyLinkedBase._Node):
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p: Position, e):
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p: Position, e):
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        original = self._validate(p)
        return self._delete_node(original)

    def replace(self, p, e):
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value


def insertion_sort(L: PositionalList):
    if len(L) > 1:
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)
            value = pivot.element()
            if value > marker.element():
                marker = pivot
            else:
                walk = marker
                while walk != L.first() and L.before(walk).element() > value:
                    walk = L.before(walk)
                L.delete(pivot)
                L.add_before(walk, value)


# data = PositionalList()
# for i in range(10):
#     data.add_first(i)
# for i in data:
#     print(i)
