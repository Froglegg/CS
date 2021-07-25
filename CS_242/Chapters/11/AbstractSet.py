
class AbstractSet(object):
    ''' generic set method implementations'''

    def __or__(self, other):
        '''Union a | b '''

        return self + other

    def __and__(self, other):
        '''intersection, a & b'''
        # type(self)() is essentially the same as returning a new AbstractSet() instance
        intersection = type(self)()
        for item in self:
            if item in other:
                intersection.add(item)
        return intersection

    def __sub__(self, other):
        '''difference, a - b '''
        difference = type(self)()
        for item in self:
            if not item in other:
                difference.add(item)
        return difference

    def __eq__(self, other):
        for item in self:
            if item not in other:
                return False
        return True

    def isSubset(self, other):
        ''' returns true if set is subset of other, else false'''
        for item in self:
            if not item in other:
                return False
        return True
