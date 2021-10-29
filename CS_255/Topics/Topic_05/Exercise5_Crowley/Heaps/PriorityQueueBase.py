class PriorityQueueBase:
    class _Item:
        __slots__ = '_key', '_value', '_index'

        def __init__(self, k, v, index=None) -> None:
            self._key = k
            self._value = v
            self._index = index

        def __lt__(self, o: object) -> bool:
            return self._key < o._key

        def __le__(self, o: object) -> bool:
            return self._key <= o._key

        def __eq__(self, o: object) -> bool:
            if type(self) is not type(o):
                return False
            return self._key == o._key

        def __ne__(self, o: object) -> bool:
            return not (self == o)

        def __str__(self) -> str:
            return f"Key: {self._key}, Value: {self._value}, Index: {self._index}"

    def is_empty(self):
        return len(self) == 0
