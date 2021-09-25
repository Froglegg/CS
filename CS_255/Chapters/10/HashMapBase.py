from MapBase import MapBase
from random import randrange


class HashMapBase(MapBase):

    def __init__(self, cap=11, prime=109345121) -> None:
        # Create empty hash table
        self._table = cap * [None]
        # number of entries in map
        self._n = 0
        # prime for MAD compression
        self._prime = prime
        #  scale from [1, prime - 1] for MAD
        self._scale = 1 + randrange(prime - 1)
        # shift from [0, prime - 1] for MAD
        self._shift = randrange(prime)

    def _hash_function(self, k):
        # MAD hash and compression function
        return (hash(k) * self._scale + self._shift) % self._prime % len(self._table)

    def __len__(self) -> int:
        return self._n

    def __getitem__(self, k: str) -> any:
        j = self._hash_function(k)
        return self._bucket_getitem(j, k)

    def __setitem__(self, k: str, v: any) -> None:
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)
        # keep load factor <= 0.5
        if self._n > len(self._table) // 2:
            self._resize(2 * len(self._table)-1)

    def __delitem__(self, k: str) -> None:
        j = self._hash_function(k)
        self._bucket_delitem(j, k)
        self._n -= 1

    def _resize(self, c):
        old = list(self.items())
        self._table = c * [None]
        self._n = 0
        for (k, v) in old:
            self[k] = v
