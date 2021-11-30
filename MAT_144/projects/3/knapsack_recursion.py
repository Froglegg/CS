def knapsackRecursion(bookList: list, w: int, n: int):
    '''
    Inputs:
    Booklist of books that have weight and value
    w is weight capacity of knapsack
    n element which we will be processing

    Output: maximum possible profit within weight upper limit
    '''

    # Base case, no item is available or all weight capacity is exhausted (bag is full)
    if (n < 0 or w == 0):
        return 0

    # if current element weight is greater than weight capacity, skip it and recur
    if(book_dict[n]["Weight"] > w):
        return knapsackRecursion(bookList, w, n-1)

    # else, return decision tree of max(exclude, include)
    else:
        return max(knapsackRecursion(bookList, w, n-1),
                   bookList[n]["Value"] + knapsackRecursion(bookList, w-bookList[n]["Weight"], n-1))


book_dict = {
    0: {
        "Weight": 0,
        "Value": 0
    },
    1: {
        "Weight": 1,
        "Value": 1
    },
    2: {
        "Weight": 3,
        "Value": 3
    },
    3: {
        "Weight": 5,
        "Value": 2
    },
    4: {
        "Weight": 7,
        "Value": 4
    }
}

book_list = list(book_dict.values())
maxWeight = 10


test = knapsackRecursion(book_list, maxWeight, len(book_dict)-1, )
print(test)
