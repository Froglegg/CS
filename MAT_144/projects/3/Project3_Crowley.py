# The program should prompt me to enter the maximum weight that the knapsack can hold.

# The program should prompt me for the number of items I want to include.

# The program should prompt me for the weights of the items.

# The program should prompt me for the value or price of each item.

# Then...your program will decide which items I should include in my knapsack to maximize profit while still staying within the restriction of my weight limit.

# Use any algorithm you wish. You're just going through all possibilities of weights and profits and figuring out which one provides the max while still honoring the weight restriction that the user entered.

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
        "Weight": 2,
        "Value": 2
    },
    3: {
        "Weight": 3,
        "Value": 3
    },
    4: {
        "Weight": 4,
        "Value": 4
    }
}


def knapsackAlgorithm(weight_of_knapsack: int, book_dict: dict) -> list:
    ''''
    Knapsack algorithm takes in a weight integer and a dictionary of books with integer keys and book<dict> values, and outputs a list of best possible book lists, with the best possible book lists being not greater than the weight integer, with the best possible values / prices of books.

    Input: A weight integer that is an upper limit on the total weight of all books in each list, and a book_dict that is a dictionary with integer keys and book<dict> values, which has a type signature of {"Weight":int, "Value":int}

    Output: A list of lists of books that have the highest possible value while staying under or equal to the upper limit of the weight integer input.
    '''
    # declare variables in outer scope
    best_possible_book_list = []
    total_value = 0

    # iterate through books, using Python's enumerate method to access index of iteration
    for idx, _ in enumerate(book_dict.values()):
        temp_list = []
        temp_weight = 0
        temp_value = 0

        # nested loop, iterate through books starting at idx of outer loop
        for i in range(idx, len(book_dict.values())):

            # set variable for ease of access to book_dict item at index i
            book = book_dict[i]

            # accumulate weight
            temp_weight += book["Weight"]

            # if weight is less than or equal to weight of knapsack
            if temp_weight <= weight_of_knapsack:

                # accumulate value
                temp_value += book["Value"]

                if temp_value >= total_value:
                    # if temp value is greater than or equal to total_value, we have a contender for best possible book list; append to temp list
                    total_value = temp_value
                    temp_list.append(book)

            else:
                # else, break inner loop if weight exceeded
                if temp_list:
                    # if temp_list is not falsy, i.e., is not empty, append it to best possible book list.
                    best_possible_book_list.append(temp_list)
                break

    return best_possible_book_list


# print(knapsackAlgorithm(3, book_dict))


def knapsackProblem():
    weight_of_knapsack = 0
    number_of_items = 0
    book_dict = {}

    print("\n~*~*~*~ Knapsack Problem ~*~*~*~*\n")
    print("You are a well-known, ambitious, and rich book collector in Ancient Athens, trying to expand your library by any means necessary.\nYou've recently been introduced to a skilled cat burglar who has offered his services to you, however, he has only so much room in his knapsack and can only steal so many books for you.\nHe needs a list of all the books you might want, as well as their weights and estimated market value, so that he can make the best possible heist.")
    print("Aristotle and a time travelling computer programmer named Hayes Crowley have worked together to write you a program to help you craft this list. All you need to do is follow the instructions below (note: Please use integers for all inputs!)\n")
    print("~*~*~*~~*~* Begin User Input ~*~*~*~*~*~*\n")

    while True:
        try:
            weight_of_knapsack = int(
                input("How much weight can the knapsack carry?: "))
            number_of_items = int(
                input("How many books are you trying to acquire?: "))
            for item in range(number_of_items):
                book_dict[item] = {
                    "Name": f"Book {item + 1}"
                }
                book_dict[item]['Weight'] = int(
                    input(f"Please enter the weight of book {item + 1}: "))
                book_dict[item]['Value'] = int(input(
                    f"Please enter the value if book {item + 1} (in drachmas): "))

            best_possible_books_list = knapsackAlgorithm(
                weight_of_knapsack, book_dict)
            print("\n~*~*~~*~*~ Processing finished! ~*~*~*~*~*~")
            for i in range(len(best_possible_books_list)):
                print(f"\nBest possible book list {i+1}: ")
                print([book for book in best_possible_books_list[i]])

            break
        except ValueError:
            print("Please enter an integer!")

    pass


if __name__ == "__main__":
    knapsackProblem()
