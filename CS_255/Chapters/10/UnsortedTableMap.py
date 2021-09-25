from MapBase import MapBase


class UnsortedTableMap(MapBase):
    '''Simple map implementation using an unordered list'''

    def __init__(self) -> None:
        self._table = []

    def __getitem__(self, k: str) -> any:
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError("Key Error: " + repr(k))

    def __setitem__(self, k: str, v: any) -> None:
        for item in self._table:
            if k == item._key:
                item._value = v
                return
        self._table.append(self._Item(k, v))

    def __delitem__(self, k: str) -> None:
        for j in range(len(self._table)):
            if k == self._table[j]._key:
                self._table.pop(j)
                return
        raise KeyError("Key Error: " + repr(k))

    def __len__(self) -> int:
        return len(self._table)

    def __iter__(self):
        for item in self._table:
            yield item._key
