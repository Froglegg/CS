
dictionary = {"a": 4, "b": 5, "c": [6, 7]}
dictionary_1 = {"a": 8, "m": 2, "v": 7}
# update dictionary method updates a dictionary with all the key/values in another dictionry, however it does not overwrite any existing key/value pairs
dictionary.update(dictionary_1)
# returns a key/value pair as a tuple. Pairs are returned in LIFO order.
x = dictionary.popitem()
# pops out a key/value pair based on key lookup
x = dictionary.pop("b")
# dict.keys() returns an iterator over the dictionary keys
# for key in dictionary.keys():
#     print(key)
# dict.values() returns an iterator over the dictionary values
# for value in dictionary.values():
#     print(value)
# dict.items() returns an iterator over the dictionary key/value pairs
# for key, value in dictionary.items():
#     print(key, "-", value)
# get returns the value at the key, here, it returns NONE because we popped out 'b'
x = dictionary.get("b")
# fromkeys creates a new dictionary from the keys in another dictionary or other iterable, and fills in a value
dictionary_1 = dict.fromkeys(dictionary, 1)
# copy returns a shallow copy of a dictionary
dictionary_1 = dictionary.copy()
# assignments uses the __set__ method, assigns a value to a key input
dictionary_1["b"] = 2
# clear clears the dictionary, returns empty {}
dictionary.clear()
# length returns the number of entries in a dict
length = len(dictionary)

# MISSING setdefault, setdefault returns a key if it's in the dictionary,
#  else will set the key/value pair with the given input
dictionary.setdefault("testDefaultKey", "test")

# summing all values of dictionary_1
sum = 0
for value in dictionary_1.values():
    if type(value) == list:
        for i in value:
            sum += 1
    else:
        sum += value

print(sum)
# returns 14


