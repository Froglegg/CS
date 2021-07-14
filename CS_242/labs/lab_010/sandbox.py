# reversing a list using reversed()
def Reverse(lst):
    return [elem for elem in reversed(lst)]

# driver code


lst = [11, 12, 13, 14, 15, 16]
# lst = Reverse(lst)
Reverse(lst)
print(lst)
lst.pop(0)
print(lst)
