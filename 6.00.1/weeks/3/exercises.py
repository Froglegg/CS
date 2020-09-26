def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    length = 0
    for val in list(aDict.values()):
        length += len(val)
    return length


how_many({'B': [15], 'u': [10, 15, 5, 2, 6]})


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    dict_list = list(aDict.keys())
    biggest = {
        "length": 0,
        "key": ""
    }
    for k in dict_list:
        if len(aDict[k]) > biggest["length"]:
            biggest["key"] = k
            biggest["length"] = len(aDict[k])
    return biggest["key"]


biggest({'B': [15], 'u': [10, 15, 5, 2, 6]})
