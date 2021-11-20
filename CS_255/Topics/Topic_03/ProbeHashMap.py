from random import randrange
from collections.abc import MutableMapping


class ProbeHashMap(MutableMapping):
    '''Hash Map implemented using probing for collision resolution'''
    # sentinel marks location of previous deletions as AVAILABLE
    _AVAIL = object()

    # Item is our Key/Value pair item subclass
    class _Item:
        __slots__ = '_key', '_value', '_collisions', '_hashedKey'

        def __init__(self, k, v, collisions, hashedKey) -> None:
            self._key = k
            self._value = v
            self._collisions = collisions
            self._hashedKey = hashedKey

        def __eq__(self, o: object) -> bool:
            return self._key == o._key

        def __ne__(self, o: object) -> bool:
            return not (self == o)

        def __lt__(self, o: object) -> bool:
            return self._key < o._key

        def __str__(self) -> str:
            return f"(Key: {self._key}, Value: {self._value}, HashedKey: {self._hashedKey}, Collisions: {self._collisions})"

    # Init with a length of 11 and large prime number
    # optionally pass in a custom hash function (for testing different probing functions)
    def __init__(self, cap=11, prime=109345121, hashFunction: any = None,
                 probeFunction: str = None) -> None:
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

        self._customHashFunction = hashFunction if hashFunction else None

        self._customProbeFunction = probeFunction if probeFunction else "linear"

    def __iter__(self):
        for i in range(len(self._table)):
            if not self._is_available(i):
                yield self._table[i]._key

    def __len__(self) -> int:
        return self._n

    def __contains__(self, k: str) -> bool:
        try:
            self[k]
            return True
        except KeyError:
            return False

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

    def getHashTrace(self):
        trace = []
        for i in range(len(self._table)):
            if not self._is_available(i):
                trace.append(f"{self._table[i]}")
        return trace

    def _hash_function(self, k):
        if self._customHashFunction:
            return self._customHashFunction(k, len(self._table))
        else:
            # default to python hash function and MAD (multiply, add, divide) compression function
            return (hash(k) * self._scale + self._shift) % self._prime % len(self._table)

    def _probe_function(self, j, k, type="linear", iterations=1):
        '''j is the hashed key, k  is the key'''

        if type == "linear":
            linearHash = (j+iterations) % len(self._table)

            return linearHash

        if type == "quadratic":
            return (j + pow(iterations, 2)) % len(self._table)

        if type == "double":
            '''Double hashing takes the hashed key j and hashes it again with a secondary hashing function: prime - (j mod len(hashTable))'''

            def primes(n):
                ''' 
                primes function builds a list of primes up to a number n, exclusive
                we use this function in double hashing to find the greatest prime that is less than the total length of the table
                '''
                # simple sieve of multiples
                odds = range(3, n, 2)
                sieve = set(sum([list(range(q*q, n+1, q+q))
                                 for q in odds], []))
                return [2] + [p for p in odds if p not in sieve]

            doubleFactor = 7 if len(self._table) == 11 else primes(
                len(self._table))[-1]

            def secondaryHash(j, iterations):
                '''Secondary hash function returns the number of iterations i * doubleFactor - (hash(k) % doubleFactor)'''
                return iterations * (doubleFactor - (j % doubleFactor))

            return (j + secondaryHash(j, iterations)) % len(self._table)

    def _resize(self, c):
        old = list(self.items())
        self._table = c * [None]
        self._n = 0
        for (k, v) in old:
            self[k] = v

    def _is_available(self, j):
        return self._table[j] is None or self._table[j] is ProbeHashMap._AVAIL

    def _find_slot(self, j, k):
        '''
        Probing search for key k in bucket at index j

        Used by set, get, and del methods

        Return (success, index) tuple, described as follows:
        If match was found, success is True and index denotes its location
        If no match was found, success is False and index denotes first available slot
        '''
        firstAvail = None
        iterations = 0

        while True:

            # iterations += 1
            # check to see if hashed index j is available
            if self._is_available(j):

                if firstAvail is None:
                    # mark j as first available
                    firstAvail = j

                if self._table[j] is None:
                    # no match found, when inserting this means that we'll insert a new item (even though success is FALSE here, this will happen if we try to insert a new item in an available location)

                    return (False, firstAvail, iterations)

            elif k == self._table[j]._key:
                # found a match, when inserting this means that our hash key already exists, and we are overwriting the value

                return (True, j, iterations)

            # collsion! keep probing
            # self.collisions += 1
            iterations += 1

            j = self._probe_function(
                j, k, type=f"{self._customProbeFunction}", iterations=iterations)

    def _bucket_getitem(self, j, k):
        found, s, collisions = self._find_slot(j, k)
        #
        if not found:
            raise KeyError("Key Error: " + repr(k))
        return self._table[s]._value

    def _bucket_setitem(self, j, k, v):

        found, hashedKey, collisions = self._find_slot(j, k)

        if not found:
            # insert new item

            self._table[hashedKey] = self._Item(k, v, hashedKey, collisions)
            print(f"NEW ITEM: {self._table[hashedKey]}")
            self._n += 1
        else:
            # else, overwrite existing
            self._table[hashedKey]._hashedKey = hashedKey
            self._table[hashedKey]._value = v
            self._table[hashedKey]._collisions = collisions

    def _bucket_delitem(self, j, k):
        found, s = self._find_slot(j, k)

        if not found:
            raise KeyError("Key Error: " + repr(k))
        # mark as vacated / available
        self._table[s] = ProbeHashMap._AVAIL

    def setdefault(self, k: str, d: any) -> any:
        try:
            return self[k]
        except KeyError:
            self[k] = d
            return d


def customHashFunction(key, table_size):
    '''Custom hash function for exercise 3 (from Spring 2021 as described in the example document)
    This hash function should produce more collisions than the ProbeHashMap hashing functions
    '''

    return key % table_size


test = ProbeHashMap(probeFunction="linear"
                    )

l = [89, 18, 51, 62, 73, 75, 40]

for i in l:
    test[i] = i

print(test.getHashTrace())
