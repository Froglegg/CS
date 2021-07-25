from HashDict import HashDict


def test(dict):
    d1 = dict((1, 2, 3), ("one", "two", "three"))
    d2 = dict(("two", "three", "four"), (2, 3, 4))
    # print(d1)
    # print(d2)

    # for i in d1:
    #     print(i)
    # for i in d1.keys():
    #     print(i)

    # for i in d1.values():
    #     print(i)

    # for i in d1.entries():
    #     print(i.key)
    #     print(i.value)
    #     print(i)

    # print(d1.get(1))
    # d1["test"]="testYo"
    # print(d1)
    # d1["test"] = "testYo"
    # print(d1)
    # d1.pop("test")
    # print(d1, d1.size)

    newDict = d1 + d2

    for i in newDict.keys():
        print(i)


test(HashDict)
