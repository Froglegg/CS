from HashMapBase import HashMapBase
from UnsortedTableMap import UnsortedTableMap


class ChainHashMap(HashMapBase):
    '''Hash Map implemented with separate chaining for collision resolution'''

    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError("Key Error: " + repr(k))
        return bucket[k]

    def _bucket_setitem(self, j, k, v):
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap()
        oldSize = len(self._table[j])
        self._table[j][k] = v
        if(len(self._table[j]) > oldSize):
            self._n += 1

    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError("Key Error: " + repr(k))
        del bucket[k]

    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:
                for key in bucket:
                    yield key


test = ChainHashMap()
test["test"] = "hey"
for i in test:
    print(i)
    print(test[i])
