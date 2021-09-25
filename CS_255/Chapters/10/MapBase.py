from collections.abc import MutableMapping


class MapBase(MutableMapping):

    def __contains__(self, k: str) -> bool:
        try:
            self[k]
            return True
        except KeyError:
            return False

    def setdefault(self, k: str, d: any) -> any:
        try:
            return self[k]
        except KeyError:
            self[k] = d
            return d

    def __delitem__(self, v: str) -> None:
        return super().__delitem__(v)

    def __getitem__(self, k: str) -> any:
        return super().__getitem__(k)

    def __setitem__(self, k: str, v: any) -> None:
        return super().__setitem__(k, v)

    def __iter__(self) -> any:
        return super().__iter__()

    def __len__(self) -> int:
        return super().__len__()

    def __setitem__(self, k: str, v: any) -> None:
        return super().__setitem__(k, v)

    class _Item:
        __slots__ = '_key', '_value'

        def __init__(self, k, v) -> None:
            self._key = k
            self._value = v

        def __eq__(self, o: object) -> bool:
            return self._key == o._key

        def __ne__(self, o: object) -> bool:
            return not (self == o)

        def __lt__(self, o: object) -> bool:
            return self._key < o._key
