from HashMapBase import HashMapBase


class ProbeHashMap(HashMapBase):
    '''Hash Map implemented with linear probing for collision resolution'''
    # sentinel marks location of previous deletions
    _AVAIL = object()

    def _is_available(self, j):
        return self._table[j] is None or self._table[j] is ProbeHashMap._AVAIL

    def _find_slot(self, j, k):
        ''''''
        firstAvail = None
        while True:
            if self._is_available(j):
                if firstAvail is None:
                    firstAvail = j
                if self._table[j] is None:
                    return (False, firstAvail)
            elif k == self._table[j]._key:
                return (True, j)
            j = (j+1) % len(self._table)

    def _bucket_getitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError("Key Error: " + repr(k))
        return self._table[s]._value

    def _bucket_setitem(self, j, k, v):
        found, s = self._find_slot(j, k)

        if not found:
            self._table[s] = self._Item(k, v)
            self._n += 1
        else:
            self._table[s]._value = v

    def _bucket_delitem(self, j, k):
        found, s = self._find_slot(j, k)

        if not found:
            raise KeyError("Key Error: " + repr(k))
        # mark as vacated / available
        self._table[s] = ProbeHashMap._AVAIL

    def __iter__(self):
        for i in range(len(self._table)):
            if not self._is_available(i):
                yield self._table[i]._key


test = ProbeHashMap()
print(test)
test["test"] = "OK"

print(test["test"])
for i in test:
    print(i)
    print(test[i])
