def main():

    class Node(object):
        '''represents singly linked node'''

        def __init__(self, data, next=None) -> None:
            super().__init__()
            self.data = data
            self.next = next

        def __repr__(self) -> str:
            def buildString(lyst):
                if isEmpty(rest(lyst)):
                    return str(first(lyst))
                else:
                    return str(first(lyst)) + " " + buildString(rest(lyst))
            return "(" + buildString(self) + ")"

    THE_EMPTY_LIST = None

    def isEmpty(lyst):
        return lyst is THE_EMPTY_LIST

    def first(lyst):
        '''returns item at head of list'''
        return lyst.data

    def rest(lyst):
        '''returns list of items after the head of lyst'''
        return lyst.next

    def cons(data, lyst):
        ''' returns a list whose head is item and whose tail is lyst'''
        return Node(data, lyst)

    def contains(self, item, lyst):
        if isEmpty(lyst):
            return False
        elif item == first(lyst):
            return True
        else:
            return contains(item, rest(lyst))

    def get(index, lyst):
        if index == 0:
            return first(lyst)
        else:
            return get(index-1, rest(lyst))

    def length(lyst):
        if isEmpty(lyst):
            return 0
        else:
            return 1 + length(rest(lyst))

    def buildRange(lower, upper):
        '''precondition, lower <= upper
        returns a list contains the numbers from lower through upper
        '''
        if lower == upper:
            return cons(lower, THE_EMPTY_LIST)
        else:
            return cons(lower, buildRange(lower + 1, upper))

    def remove(index, lyst):
        '''precondition: 0 <= index < length(lyst)
        returns a list with item at index removed
        '''
        if index == 0:
            return rest(lyst)
        else:
            return cons(first(lyst), remove(index - 1, rest(lyst)))

    # Lisp lists don't have mutators... so, we can remove an item from A and it'll stay the same
    A = buildRange(1, 3)
    print(A)
    B = remove(0, A)
    print(B)
    print(A)


if __name__ == "__main__":
    main()
