''' 
Array data structure
An array is like a list, but the client can use only [], len, iter and str
'''


class Array(object):
    '''Represents an array'''

    def __init__(self, capacity, fillValue=None) -> None:
        ''' capacity is the static size of the array'''
        super().__init__()
        self.items = list()
        for count in range(capacity):
            self.items.append(fillValue)

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, newItem):
        self.items[index] = newItem


# a = Array(5, "")
# print(a)

# for i in range(len(a)):
#     a[i] = i + 1

# print(a)

# print(a[0])

# for item in a:
#     print(item)

# # operations on arrays
# DEFAULT_CAPACITY = 5
# logicalSize = 0
# b = Array(DEFAULT_CAPACITY)

# # increasing size of array

# if logicalSize == len(b):
#     # create new array and copy data from old array
#     # temp = Array(len(b)+1)
#     # double the size of the array instead of adding one new cell each time the array needs to be resized to ensure better performance
#     temp = Array(len(b)*2)
#     for i in range(logicalSize):
#         temp[i] = b[i]
#     # reset old array variable to new array, old arrays memory is left out for the garbage collector
#     b = temp


# # decreasing size of array

# # performant choice is, if logical size is less than or equal to the 1/4 the length of b and the length of b is greater than 2x the default capacity
# if logicalSize <= len(b) // 4 and len(b) >= DEFAULT_CAPACITY * 2:
#     temp = Array(len(b) // 2)
#     for i in range(logicalSize):
#         temp[i] = b[i]
#     b = temp

# # inserting item into an array
# # first increase physical size of array if necessary using operation above, and then shift items down by one position
# targetIndex = 3
# for i in range(logicalSize, targetIndex, -1):
#     b[i] = b[i-1]
# # add new item and increment logical size
# newItem = "hey"
# a[targetIndex] = newItem
# logicalSize += 1

# # removing item from array, inverse of inserting item
# # shift items up by one position
# for i in range(targetIndex, logicalSize-1):
#     b[i] = b[i+1]
# # decrement logical size
# logicalSize -= 1
# # decrease size of array if necessary using operations above
