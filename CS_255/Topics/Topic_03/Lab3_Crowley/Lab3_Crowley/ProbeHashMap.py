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
            if type(self) is not type(o):
                return False
            return self._key == o._key

        def __ne__(self, o: object) -> bool:
            return not (self == o)

        def __lt__(self, o: object) -> bool:
            return self._key < o._key

        def __str__(self) -> str:
            return f"(Key: {self._key}, Value: {self._value}, HashedKey: {self._hashedKey}, Collisions: {self._collisions})"

    def __init__(self,
                 probeFunction: str = "linear", sourceCollection: list = None) -> None:
        # Create empty hash table
        self._table = 11 * [None]
        # number of entries in map
        self._n = 0
        # set probe type
        self._customProbeFunction = probeFunction
        # Total collisions
        self.totalCollisions = 0
        # Trace array for collisions count output
        self.collisionTrace = []
        # trace array for probee
        self.probeTrace = []
        # if initializing with a source collection, go ahead and run inserting loop
        if sourceCollection:
            for k in sourceCollection:
                self.__setitem__(k, k)

    def __iter__(self):
        for i in range(len(self._table)):
            if not self._is_available(i):
                yield self._table[i]

    def __len__(self) -> int:
        return self._n

    def __str__(self):
        return f"{[f'{i}'for i in self._table]}"

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
        # if self._n > len(self._table) // 2:
        #     self._resize(2 * len(self._table)-1)

    def _resize(self, c):
        old = list(self.items())
        self._table = c * [None]
        self._n = 0
        for (k, v) in old:
            self[k] = v

    def __delitem__(self, k: str) -> None:
        j = self._hash_function(k)
        self._bucket_delitem(j, k)
        self._n -= 1

    def _is_available(self, j):
        return self._table[j] is None

    def size(self):
        return self._n

    def _hash_function(self, k):
        return k % len(self._table)
        # scramble = (k >> 8) | ((k & 0xff) << 16)
        # return scramble % len(self._table)

    def _probe_function(self, firstIndex, key, type="linear", iterations=1):

        if type == "linear":
            return (firstIndex+iterations) % len(self._table)

        if type == "quadratic":
            return (firstIndex + pow(iterations, 2)) % len(self._table)

        if type == "double":
            '''Double hashing takes the hashed key j and hashes it again with a secondary hashing function: prime - (j mod len(hashTable))'''

            def primes(n):
                ''' primes function builds a list of primes up to a number n, exclusive
                we use this function in double hashing to find the greatest prime that is less than the total length of the table'''
                # simple sieve of multiples
                odds = range(3, n, 2)
                sieve = set(sum([list(range(q*q, n+1, q+q))
                                 for q in odds], []))
                return [2] + [p for p in odds if p not in sieve]

            doubleFactor = 7 if len(self._table) == 11 else primes(
                len(self._table))[-1]

            def primaryHash(key):
                '''this is our normal hashing function without the indexing '''
                # return (key >> 8) | ((key & 0xff) << 16)
                return key

            def secondaryHash(key):
                '''Secondary hash function returns the doubleFactor - (hash(k) % doubleFactor), where the double factor is the largest prime number less then the length of the table'''
                return doubleFactor - (primaryHash(key) % doubleFactor)

            return ((iterations * secondaryHash(key)) + firstIndex) % len(self._table)

    def _find_slot(self, hashedKey, key):
        '''
        Probing search for key key in bucket at index hashedKey

        Used by set, get, and del methods

        Return (success, index) tuple, described as follows:
        If match was found, success is True and index denotes its location
        If no match was found, success is False and index denotes first available slot
        '''
        collisions = 0
        firstIndex = hashedKey

        while True:
            # check to see if hashed index j is available
            if self._table[hashedKey] is None:

                # empty bucket, inserting new item or raising keyError in getter
                return (False, hashedKey, collisions)

            elif key == self._table[hashedKey]._key:
                # found a match for bucket_getitem or bucket_setitem if we are updating a key/value pair
                return (True, hashedKey, collisions)

            # keep probing
            collisions += 1
            self.totalCollisions += 1

            hashedKey = self._probe_function(
                firstIndex, key, type=f"{self._customProbeFunction}", iterations=collisions)

    def _bucket_getitem(self, j, k):
        found, s, _ = self._find_slot(j, k)
        if not found:
            raise KeyError("Key Error: " + repr(k))
        return self._table[s]._value

    def _bucket_setitem(self, hashedKey, key, value):

        found, hashedKey, collisions = self._find_slot(hashedKey, key)

        self._appendToCollisionTrace(key, int(value*2), collisions)

        if not found:
            # insert new item
            self._table[hashedKey] = self._Item(
                key, int(value)*2, collisions, hashedKey)
            self._n += 1
        else:
            # else, overwrite existing
            self._table[hashedKey]._hashedKey = hashedKey
            self._table[hashedKey]._value = value * 2
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

    def _appendToCollisionTrace(self, key, value, collisions):
        # collisions * 2, since we are also counting collisions when accessing for the lab assignment
        collisionString = f"{key} : {value} -> {value}, collisions {collisions * 2}",

        self.collisionTrace.append(collisionString[0])

    def getCollisionTrace(self):
        # returns total collisions * 2, since we are also counting collisions when accessing for the lab assignment
        return (self.collisionTrace, self.totalCollisions * 2)

    def getProbeTrace(self):

        for i in self:
            index = i._hashedKey
            key = i._key
            value = i._value

            self.probeTrace.append(f"index={index} key={key} value={value}")
        return self.probeTrace
